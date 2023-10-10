# cuemaker2
Fork of 
A script for automatically generating CUE files from a list of timestamps and titles, like
those commonly seen in YouTube descriptions.
Original Author: JoshBarrass
Contributing Authors: TheScienceOtter (https://gitlab.com/TheScienceOtter/cuemaker)), r-a-y
Last Edit: 05/25/2022

This version automatically finds, writes filenames and arguments and scans for subfolders. So all you have to do is just lauch it before setting up .txt with timestamps.
For extension .m4a .

If you want to sort timestamps for some videos that have them different order you might want to use notepad++.
Ctrl+f> replace> tick regular expressions box and in FIND paste this (.*) - (.*) (\d{2}:\d{2}:\d{2}) in REPLACE this \3 \1 - \2
e.g. https://www.youtube.com/watch?v=TzSXTZs2a3s

Spot Goes To Hollywood - Watery Grave 00:00:00
To
00:00:00 Spot Goes To Hollywood - Watery Grave

This should sort timestamps in order that this script can process.
