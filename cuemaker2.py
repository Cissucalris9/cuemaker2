import os
import glob
import subprocess
import re
import argparse

def pad_number(number, length=2, padding="0"):
    str_number = str(number)
    if len(str_number) < length:
        str_number = padding + str_number
    return str_number

def make_cue_tracks(inp, pattern="(\[)?((\\d{1,2}):)?(\\d{1,2}):(\\d{1,2})(\])? (.*)",
                    hr=2, m=3, s=4, title=6, artist=None):

    matcher = re.compile(pattern)
    output = ""
    lines = inp.strip("\n").split("\n")
    if len(lines) > 999:
        raise ValueError("A cue sheet cannot contain more than 999 tracks!")

    for line in range(len(lines)):
        lines[line] = lines[line].strip()
        str_track = pad_number(line + 1)

        match = matcher.match(lines[line])
        groups = list(match.groups())

        if groups[hr] is None:
            groups[hr] = "00"

        output += f"\n    TRACK {str_track} AUDIO\n"
        output += f"        TITLE \"{groups[title]}\"\n"
        if isinstance(artist, int):
            output += f"        PERFORMER {groups[artist]}\n"
        output += f"        INDEX 01 {pad_number(int(groups[hr]) * 60 + int(groups[m]))}:{pad_number(groups[s])}:00"

    return output

def make_cue(inp, performer, album, filename, ext, rems={}, *args, **kwargs):
    output = f"PERFORMER \"{performer}\"\nTITLE \"{album}\"\n"

    for key, item in rems.items():
        output += f"REM {key} {item}\n"

    output += f"FILE \"{filename}.{ext}\" WAVE"
    output += make_cue_tracks(inp, *args, **kwargs)
    output += "\n"
    return output

def read_description(path):
    with open(path, "r") as f:
        description = f.read()
    return description

def save_cue(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)
    return True

def generate_cue_files(directory, album, performer, ext="m4a"):
    current_directory = os.getcwd()
    search_pattern = os.path.join(current_directory, "**", f"*.{ext}")
    files = glob.glob(search_pattern, recursive=True)

    for file in files:
        txt_file = os.path.splitext(os.path.basename(file))[0] + ".txt"
        txt_file_path = os.path.join(current_directory, txt_file)
        if os.path.exists(txt_file_path):
            filename = os.path.splitext(os.path.basename(file))[0]
            description = read_description(txt_file_path)
            output = make_cue(description, performer, album, filename, ext)
            cue_file_path = os.path.join(current_directory, f"{filename}.cue")
            save_cue(cue_file_path, output)
            print(f"Generated CUE file: {cue_file_path}")

    print("Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ext", default="m4a", help="Extension of your audio file. Defaults to \"m4a\"")
    args = parser.parse_args()

    album = "Album Name"
    performer = "Performer Name"

    generate_cue_files(os.getcwd(), album, performer, args.ext)
