import sys
import os

import pathlib
import re

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyCutPhrase")

        self.explainlabel = QLabel("This utility removed bracketed lines from"
                                   "the selected document.")
        self.explainlabel.setWordWrap(True)

        self.filefindbutton = QPushButton()
        self.filefindbutton.setObjectName("filefind")
        self.filefindbutton.setText("Select Document")
        self.filefindbutton.clicked.connect(self.filefind_button_click)

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

    def filefind_button_click(self):
        print("Filefile pressed")

        filedialogoutput = MainWindow.FilefindDialog.getOpenFileName()

        filedialogpath = filedialogoutput[0]

        print("Selected file path: ", filedialogpath)

        f = open(filedialogpath, 'r', encoding="utf8", errors='ignore')

        filepathmain = str(pathlib.Path(filedialogpath).stem)
        filepathext = str(pathlib.Path(filedialogpath).suffix)
        filepathdir = str(pathlib.Path(filedialogpath).parent)
        trailingslash = str(os.sep)
        newfilename = (filepathdir + trailingslash + filepathmain +
                       "_revised" + filepathext)

        copy = open(newfilename, "w", encoding="utf16", errors='ignore')

        bracketpattern = re.compile(r"((\[.*?\])|(\((edited)\)))")

        usertagpattern = re.compile(r"#\d{4}")

        for comparestring in f:
            if re.search(usertagpattern, comparestring):
                copy.write(comparestring)
                print(comparestring)
                pass

            if re.search(bracketpattern, comparestring):
                pass

            else:
                copy.write(comparestring)
                print(comparestring)

        f.close()
        copy.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
