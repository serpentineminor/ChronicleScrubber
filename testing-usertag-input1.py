import sys
import os

import configparser
import pathlib
import re

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
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
        config['TARGETSTRINGS'] = {"filepath": "",
                                   "usertags": "",
                                   "bottags": ""}

        print("TARGETSTRINGS section was missing. New file created.")

        with open("settingsfortest2.ini", "w", encoding="utf8") as configfile:
            config.write(configfile)

    config.read("settingsfortest2.ini", encoding="utf8")

    targetstringsection = config['TARGETSTRINGS']

    if "filepath" in targetstringsection:
        print("Ini file structure appears valid.")

    else:
        config['TARGETSTRINGS'] = {"filepath": "",
                                   "usertags": "",
                                   "bottags": ""}

        print("Filepath key was missing. New file created.")

        with open("settingsfortest2.ini", "w", encoding="utf8") as configfile:
            config.write(configfile)

    if "usertags" in targetstringsection:
        print("Ini file structure appears valid.")

    else:
        config['TARGETSTRINGS'] = {"filepath": "",
                                   "usertags": "",
                                   "bottags": ""}

        print("Usertags key was missing. New file created.")

        with open("settingsfortest2.ini", "w", encoding="utf8") as configfile:
            config.write(configfile)

    if "bottags" in targetstringsection:
        print("Ini file structure appears valid.")

    else:
        config['TARGETSTRINGS'] = {"filepath": "",
                                   "usertags": "",
                                   "bottags": ""}

        print("Bottags key was missing. New file created.")

        with open("settingsfortest2.ini", "w", encoding="utf8") as configfile:
            config.write(configfile)

    print("Config structure check complete.")


checkconfigstructure()
filepathcfg = config['TARGETSTRINGS']["filepath"]
usertagcfg = config['TARGETSTRINGS']["usertags"]
bottagcfg = config['TARGETSTRINGS']["bottags"]


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
    usertagcfg = config['TARGETSTRINGS']["usertags"]
    bottagcfg = config['TARGETSTRINGS']["bottags"]

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

    bracketpattern = re.compile(r"(\[|\]).*?(\[|\])")
    usertagpattern = re.compile(r"\#\d{4}")

    plyrusertag = usertagcfg.split(":")
    botusertag = bottagcfg.split(":")

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyCutPhrase")

        self.explainlabel = QLabel("This utility will remove any text from "
                                   "Discord chat text file exports that is "
                                   "a message sent by the specified users."
                                   "\n"
                                   "Input all usernames as their exact "
                                   "Discord usernames, including the "
                                   "four character number tags (i.e., #0001) "
                                   "separated by a colon (:) and no spaces.")
        self.explainlabel.setWordWrap(True)

        self.usertaglabel = QLabel("Keep messages from these users:")
        self.explainlabel.setWordWrap(True)

        self.bottaglabel = QLabel("Remove messages from these users:")
        self.explainlabel.setWordWrap(True)

        self.filefindbutton = QPushButton()
        self.filefindbutton.setObjectName("filefind")
        self.filefindbutton.setText("Select Document")
        self.filefindbutton.clicked.connect(self.filefind_button_click)

        self.usertaginputbox = QLineEdit(usertagcfg)

        self.bottaginputbox = QLineEdit(bottagcfg)

        layout = QVBoxLayout()

        layout.addWidget(self.explainlabel)

        layout.addWidget(self.usertaglabel)
        layout.addWidget(self.usertaginputbox)

        layout.addWidget(self.bottaglabel)
        layout.addWidget(self.bottaginputbox)

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

    def print_thing(self, text):
        print(text)


    def filefind_button_click(self):
        print("Filefile pressed")

        filedialogoutput = MainWindow.FilefindDialog.getOpenFileName()

        usertaginput = self.usertaginputbox.text()
        bottaginput = self.bottaginputbox.text()

        print(filedialogoutput)
        print(usertaginput)
        print(bottaginput)

        filedialogpath = pathlib.Path(os.fsdecode(filedialogoutput[0]))

        print("Selected file path: ", filedialogpath)

        filedialogpath = str(filedialogpath)
        print("repr:", filedialogpath)
        filedialogpath = filedialogpath.encode(encoding="utf8", errors="surrogateescape")
        print("encode:", filedialogpath)
        filedialogpath = filedialogpath.decode(encoding="utf8",
                                               errors="surrogateescape")
        print("decode:", repr(filedialogpath))

        config.read("settingsfortest2.ini", encoding="utf8")

        targetstringsed = config["TARGETSTRINGS"]

        targetstringsed["filepath"] = filedialogpath
        targetstringsed["usertags"] = usertaginput
        targetstringsed["bottags"] = bottaginput

        with open("settingsfortest2.ini", "w", encoding="utf8", errors="surrogateescape") \
                as configfile:
            config.write(configfile)

        config.read("settingsfortest2.ini", encoding="utf8")

        with open("settingsfortest2.ini", "w", encoding="utf8", errors="surrogateescape") as configfile:
            config.write(configfile)

        scrubtext()


app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()
