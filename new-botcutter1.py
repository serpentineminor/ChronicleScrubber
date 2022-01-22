import sys
import os
import codecs

import configparser
import pathlib
import re

import urllib.parse

import emoji

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)

config = configparser.ConfigParser()

iniexistcheck = pathlib.Path("settingsfortest2.ini").exists()


def checkconfigstructure():
    config.read("settingsfortest2.ini", encoding="utf8")

    if not 'TARGETSTRINGS' in config:
        config['TARGETSTRINGS'] = {"filepath": ""}

        print("TARGETSTRINGS section was missing. New file created.")

        with open("settingsfortest2.ini", "w", encoding="utf8") as configfile:
            config.write(configfile)

    config.read("settingsfortest2.ini", encoding="utf8")

    targetstringsection = config['TARGETSTRINGS']

    if "filepath" in targetstringsection:
        print("Ini file structure appears valid.")

    else:
        config['TARGETSTRINGS'] = {"filepath": ""}

        print("Filepath key was missing. New file created.")

        with open("settingsfortest2.ini", "w", encoding="utf8") as configfile:
            config.write(configfile)

    print("Config structure check complete.")


checkconfigstructure()
filepathcfg = config['TARGETSTRINGS']["filepath"]


def is_configinput_empty():
    print("Beginning check for empty config inputs.")
    if not filepathcfg:
        print("Filepath is empty.")

    if filepathcfg:
        print("Config values are defined.")

    print("Check for empty config input is complete.")


def scrubtext():
    config.read("settingsfortest2.ini", encoding="utf8")

    filepathcfg = config['TARGETSTRINGS']["filepath"]

    filepath = filepathcfg
    print("pulled from cfg:", filepath)
    filepath = filepath.encode("utf8")
    print("encoded with utf8:", filepath)
    filepath = filepath.decode("utf8")
    print("decoded to utf8:", filepath)

    inputexistcheck = pathlib.Path(filepath).exists()

    if inputexistcheck:
        print("File is found. Reading...")

    else:
        print("Indicated file does not exist or submitted file path "
              "is invalid."
              "\n "
              "Check the file location and the path you have input.")

    f = open(filepath, 'r', encoding="utf8", errors='ignore')

    filepathmain = str(pathlib.Path(filepath).stem)
    filepathext = str(pathlib.Path(filepath).suffix)
    filepathdir = str(pathlib.Path(filepath).parent)
    trailingslash = str(os.sep)
    newfilename = (filepathdir + trailingslash + filepathmain +
                   "_revised" + filepathext)

    copy = open(newfilename, "w", encoding="utf8", errors='ignore')

    skipline = True

    bracketpattern = re.compile(r"\[.*?\]")
    usertagpattern = re.compile(r"\#\d{4}")

    plyrusertag = "SerpentineMinor#4434", "In_MyImagination#1364", \
                  "MusicalOdyssey#6140"
    botusertag = "Malkav#5442", "Avrae#6944", "Realm of Darkness#1857", \
                 "[Tzimisce]#8330"

    totlinedeletecount = 0

    for comparestring in f:
        if any(x in comparestring for x in botusertag):
            skipline = True

        if any(x in comparestring for x in plyrusertag):
            skipline = False

        if skipline is False:
            if bool(re.search(usertagpattern, comparestring)) is False and \
                    bool(re.search(bracketpattern, comparestring)) is True:
                print("Deleted:", comparestring)

            else:
                copy.write(comparestring)
                print(comparestring)

        else:
            print("Deleted:", comparestring)
            totlinedeletecount += 1

    print("Total lines deleted: %s" % totlinedeletecount)

    f.close()
    copy.close()


def filefind_button_click():
    print("Filefile pressed")

    filedialogoutput = MainWindow.FilefindDialog.getOpenFileName()

    print(filedialogoutput)

    filedialogpath = pathlib.Path(os.fsdecode(filedialogoutput[0]))

    print("Selected file path: ", filedialogpath)

    filedialogpath = str(filedialogpath)
    print("repr:", filedialogpath)
    filedialogpath = filedialogpath.encode(encoding="utf8", errors="surrogateescape")
    print("encode:", filedialogpath)
    filedialogpath = filedialogpath.decode(encoding="utf8",
                                           errors="surrogateescape")
    print("decode:", repr(filedialogpath))
    #print("decode:", filedialogpath)

    config.read("settingsfortest2.ini", encoding="utf8")

    targetstringsed = config["TARGETSTRINGS"]

    targetstringsed["filepath"] = filedialogpath

    #print(targetstringsed["filepath"])
    #print(repr(filedialogpath))
    #print(filedialogpath)

    with open("settingsfortest2.ini", "w", encoding="utf8", errors="surrogateescape") \
            as configfile:
        config.write(configfile)

    config.read("settingsfortest2.ini", encoding="utf8")

    with open("settingsfortest2.ini", "w", encoding="utf8", errors="surrogateescape") as configfile:
        config.write(configfile)

    scrubtext()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyCutPhrase")

        self.explainlabel = QLabel("This utility will remove any text from "
                                   "Discord chat text file exports that is "
                                   "a message sent by the specified bots.")
        self.explainlabel.setWordWrap(True)

        self.filefindbutton = QPushButton()
        self.filefindbutton.setObjectName("filefind")
        self.filefindbutton.setText("Select Document")
        self.filefindbutton.clicked.connect(filefind_button_click)

        layout = QVBoxLayout()

        layout.addWidget(self.explainlabel)

        layout.addWidget(self.filefindbutton)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    class FilefindDialog(QFileDialog):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Select Input File")

            self.layout = QVBoxLayout()
            self.setLayout(self.layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
