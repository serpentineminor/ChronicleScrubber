import sys
import os

import configparser
import pathlib
import codecs, unicodedata

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)

config = configparser.ConfigParser()

iniexistcheck = pathlib.Path("settingsfortest1.ini").exists()

config.read("settingsfortest1.ini")


def checkconfigstructure():
    config.read("settingsfortest1.ini")

    if not 'TARGETSTRINGS' in config:
        config['TARGETSTRINGS'] = {"beginword": "",
                                   "endword": "",
                                   "filepath": ""}

        print("TARGETSTRINGS section was missing. New file created.")

        with open("settingsfortest1.ini", "w") as configfile:
            config.write(configfile)

    config.read("settingsfortest1.ini")

    targetstringsection = config['TARGETSTRINGS']

    if not "beginword" in targetstringsection:
        config['TARGETSTRINGS'] = {"beginword": "",
                                   "endword": "",
                                   "filepath": ""}

        print("Beginword key was missing. New file created.")

        with open("settingsfortest1.ini", "w") as configfile:
            config.write(configfile)

    if not "endword" in targetstringsection:
        config['TARGETSTRINGS'] = {"beginword": "",
                                   "endword": "",
                                   "filepath": ""}

        print("Endword key was missing. New file created.")

        with open("settingsfortest1.ini", "w") as configfile:
            config.write(configfile)

    if not "filepath" in targetstringsection:
        config['TARGETSTRINGS'] = {"beginword": "",
                                   "endword": "",
                                   "filepath": ""}

        print("Filepath key was missing. New file created.")

        with open("settingsfortest1.ini", "w") as configfile:
            config.write(configfile)

    else:
        pass
        print("Ini file structure appears valid.")

    print("Config structure check complete.")


checkconfigstructure()

# def print_config_to_console():
#     print("Beginning print config to console.")
#
#     config.read("settingsfortest1.ini")
#
#     sectionheader = config.sections()
#
#     print("Sections: ", sectionheader)
#
#     for key in config['TARGETSTRINGS']:
#         print("Has key ", key, " with value ", config['TARGETSTRINGS'][key])
#
#     print("Finished print config to console.")


# print_config_to_console()

sinput1 = config['TARGETSTRINGS']["beginword"]
sinput2 = config['TARGETSTRINGS']["endword"]
targetpathinput = config['TARGETSTRINGS']["filepath"]


def is_configinput_empty():
    print("Beginning check for empty config inputs.")
    if not sinput1:
        print("Beginword is empty.")
    if not sinput2:
        print("Endword is empty.")
    if not targetpathinput:
        print("Filepath is empty.")

    if sinput1 and sinput2 and targetpathinput:
        print("Config values are defined.")

    print("Check for empty config input is complete.")

    # print_config_to_console()


is_configinput_empty()


def scrubtext(self):
    # Checking existence of ini file, so that if there's not
    # an ini file for it to read, there will be.
    # I could probably carry the sinput1 etc etc variables
    # across instead of having them dump into the beginword
    # etc etc variables.
    # I'm not exactly sure why I'm doing it like this yet
    # but I think there's some reason for it.
    # print_config_to_console()
    config.read("settingsfortest1.ini")
    print("Beginning scrub text.")

    print("Printing user input to console.")
    print("Beginword: ", self.input1.text(), "\n", "Endword: ",
          self.input2.text(), "\n")

    print("Assigning sinput1 etc etc values from config.")
    sinput1 = config['TARGETSTRINGS']["beginword"]
    sinput2 = config['TARGETSTRINGS']["endword"]
    targetpathinput = config['TARGETSTRINGS']["filepath"]

    print("Printing sinput1 etc etc to console.")
    print("Beginword: ", sinput1, "\n", "Endword: ",
          sinput2, "\n", "Filepath: ", targetpathinput)

    print("Beginning ini exist check.")
    if not iniexistcheck:
        config['TARGETSTRINGS'] = {"beginword": sinput1,
                                   "endword": sinput2,
                                   "filepath": targetpathinput}

        with open("settingsfortest1.ini", "w") as configfile:
            config.write(configfile)

        print("Your .ini file has been created.")
        # print_config_to_console()
        # config.read("settingsfortest1.ini")

    with open("settingsfortest1.ini", "w") as configfile:
        config.set('TARGETSTRINGS', "beginword", sinput1)
        config.set('TARGETSTRINGS', "endword", sinput2)
        config.set('TARGETSTRINGS', "filepath", targetpathinput)

        print("Config values have been updated.")
        # print_config_to_console()
        # config.read("settingsfortest1.ini")

    print("Finished ini exist check.")
    print("Assigned beginword etc etc to sinput1 etc etc.")

    beginword = sinput1
    endword = sinput2
    filepath = targetpathinput

    print("Beginword: ", beginword, "\n", "Endword: ",
          endword, "\n", "Filepath: ", filepath)

    print("Variables assigned with sinput1, sinput2, and "
          "targetpathinput.")
    # print_config_to_console()
    config.read("settingsfortest1.ini")

    print("Beginword: ", beginword, "\n", "Endword: ",
          endword, "\n", "Filepath: ", filepath)

    config.read("settingsfortest1.ini")

    beginword = config['TARGETSTRINGS']["beginword"]
    endword = config['TARGETSTRINGS']["endword"]
    filepath = config['TARGETSTRINGS']["filepath"]

    print("Variables assigned with config values.")
    # print_config_to_console()

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

    # print_config_to_console()

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

    for comparestring in f:
        # unicodehandling = codecs.decode('utf-8').encode('utf-8', 'replace').decode('utf-8')
        # comparestring = f.readline()
        if beginword in comparestring:
            skipline = True
            print("Beginword was detected.")

        if skipline:
            print("-deleted-")

        else:
            copy.write(comparestring)
            print(comparestring)

        if endword in comparestring:
            skipline = False
            print("Endword was detected.")

    f.close()
    copy.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyCutPhrase")

        self.explainlabel = QLabel("This utility will remove text from "
                                   "a document that begins with a "
                                   "specific  phrase and all lines up "
                                   "to and including the line on which "
                                   "an end phrase exists")
        self.explainlabel.setWordWrap(True)

        self.label1 = QLabel("Beginning word line")
        self.label2 = QLabel("Ending word line")

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        self.filefindbutton = QPushButton()
        self.filefindbutton.setObjectName("filefind")
        self.filefindbutton.setText("Select Document")
        self.filefindbutton.clicked.connect(self.filefind_button_click)

        layout = QVBoxLayout()

        layout.addWidget(self.explainlabel)

        layout.addWidget(self.label1)
        layout.addWidget(self.input1)

        layout.addWidget(self.label2)
        layout.addWidget(self.input2)

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

    def filefind_button_click(self):
        print("Filefile pressed")

        filedialogoutput = MainWindow.FilefindDialog.getOpenFileName()

        filedialogpath = filedialogoutput[0]

        print("Selected file path: ", filedialogpath)

        config.read("settingsfortest1.ini")

        targetstringsed = config["TARGETSTRINGS"]

        targetstringsed["filepath"] = filedialogpath

        with open("settingsfortest1.ini", "w") as configfile:
            config.write(configfile)

        sinput1 = self.input1.text()
        sinput2 = self.input2.text()

        config.read("settingsfortest1.ini")

        targetstringsed = config["TARGETSTRINGS"]

        targetstringsed["beginword"] = sinput1
        targetstringsed["endword"] = sinput2

        with open("settingsfortest1.ini", "w") as configfile:
            config.write(configfile)

        print(sinput1)
        print(sinput2)
        print(targetpathinput)

        print(targetstringsed["beginword"])
        print(targetstringsed["endword"])
        print(targetstringsed["filepath"])

        scrubtext(self)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
