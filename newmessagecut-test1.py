import sys
import os

import configparser
import pathlib
import re

config = configparser.ConfigParser()

config.read("settingsfortest2.ini")

beginword = config['TARGETSTRINGS']["beginword"]
endword = config['TARGETSTRINGS']["endword"]
filepath = config['TARGETSTRINGS']["filepath"]

config.read("settingsfortest2.ini")

print("Beginword: ", beginword, "\n", "Endword: ",
      endword, "\n", "Filepath: ", filepath)

print("Variables assigned with sinput1, sinput2, and "
      "targetpathinput.")

config.read("settingsfortest2.ini")

print("Beginword: ", beginword, "\n", "Endword: ",
      endword, "\n", "Filepath: ", filepath)

config.read("settingsfortest2.ini")

beginword = config['TARGETSTRINGS']["beginword"]
endword = config['TARGETSTRINGS']["endword"]
filepath = config['TARGETSTRINGS']["filepath"]

print("Variables assigned with config values.")

print("Beginword: ", beginword, "\n", "Endword: ",
      endword, "\n", "Filepath: ", filepath)

inputexistcheck = pathlib.Path(filepath).exists()

if not inputexistcheck:
    print("Indicated file does not exist or submitted file path "
          "is invalid."
          "\n "
          "Check the file location and the path you have input.")

else:
    print("File is found. Reading...")

f = open(filepath, 'r', encoding="utf8", errors='ignore')

filepathmain = str(pathlib.Path(filepath).stem)
filepathext = str(pathlib.Path(filepath).suffix)
filepathdir = str(pathlib.Path(filepath).parent)
trailingslash = str(os.sep)
newfilename = (filepathdir + trailingslash + filepathmain +
               "_revised" + filepathext)

copy = open(newfilename, "w", encoding="utf16", errors='ignore')

skipline = False

# I'm not using this right now, this is
# inherited from the method used in the
# original Delphi program.
# Keeping it commented out for now.
# If I switch to searching only the
# beginning of lines, I will use them.
# Maybe.
# begincharcnt = len(beginword)
# endcharcnt = len(endword)

linedeletecount = 0
totlinedeletecount = 0


#bracketpattern = re.compile(r"((\[.*?])|(\((edited)\)))")
#usertagpattern = re.compile(r"#\d{4}")


for comparestring in f:

    if beginword in comparestring:
        skipline = True
        linedeletecount = 0
        print("Beginword was detected.")

    if skipline:
        linedeletecount += 1
        totlinedeletecount += 1

    if endword in comparestring:
        skipline = False
        print("Endword was detected.")
        print("Deleted %s lines." % linedeletecount)
        print("Total lines deleted: %s" % totlinedeletecount)

    else:
        copy.write(comparestring)
        print(comparestring)

print("Total lines deleted: %s" % totlinedeletecount)

f.close()
copy.close()
