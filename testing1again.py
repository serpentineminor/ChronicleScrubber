import sys
import os

import configparser
import pathlib
import re


config = configparser.ConfigParser()

config.read("settingsfortest2.ini")

filepath = config['TARGETSTRINGS']["filepath"]

f = open(filepath, 'r', encoding="utf8", errors='ignore')

filepathmain = str(pathlib.Path(filepath).stem)
filepathext = str(pathlib.Path(filepath).suffix)
filepathdir = str(pathlib.Path(filepath).parent)
trailingslash = str(os.sep)
newfilename = (filepathdir + trailingslash + filepathmain +
               "_revised" + filepathext)

copy = open(newfilename, "w", encoding="utf16", errors='ignore')

skipline = True
markerusertag = ""
plyrusertag = "SerpentineMinor#4434", "In_MyImagination#1364", \
             "MusicalOdyssey#6140"
botusertag = "Malkav#5442", "Avrae#6944", "Realm of Darkness#1857", \
             "[Tzimisce]#8330"

for comparestring in f:
    if any(x in comparestring for x in botusertag):
        skipline = True

    if any(x in comparestring for x in plyrusertag):
        skipline = False

    if skipline is False:
        copy.write(comparestring)
        print(comparestring)

    else:
        print("Deleted:", comparestring)

f.close()
copy.close()