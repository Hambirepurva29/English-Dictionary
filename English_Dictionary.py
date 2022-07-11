from PyQt5 import QtCore, QtGui, QtWidgets
from pydictionary import PyDictionary as Eng_dict
from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 550)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 3)

        self.Search_Box = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_Box.setText("")
        self.Search_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.Search_Box.setObjectName("Search_Box")
        self.gridLayout.addWidget(self.Search_Box, 2, 0, 1, 3)

        self.Meaning_button = QtWidgets.QPushButton(self.centralwidget)
        self.Meaning_button.setObjectName("Meaning_button")
        self.gridLayout.addWidget(self.Meaning_button, 3, 0, 1, 1)
        self.Meaning_button.clicked.connect(self.clicked_search_meaning)

        self.Synonym_button = QtWidgets.QPushButton(self.centralwidget)
        self.Synonym_button.setObjectName("Synonym_button")
        self.gridLayout.addWidget(self.Synonym_button, 3, 1, 1, 1)
        self.Synonym_button.clicked.connect(self.clicked_search_synonym)

        self.Antonym_button = QtWidgets.QPushButton(self.centralwidget)
        self.Antonym_button.setObjectName("Antonym_button")
        self.gridLayout.addWidget(self.Antonym_button, 3, 2, 1, 1)
        self.Antonym_button.clicked.connect(self.clicked_search_antonym)

        self.Enter_Statement = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Enter_Statement.setFont(font)
        self.Enter_Statement.setAlignment(QtCore.Qt.AlignCenter)
        self.Enter_Statement.setObjectName("Enter_Statement")
        self.gridLayout.addWidget(self.Enter_Statement, 1, 0, 1, 3)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 320, 335))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.Answer_window = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Answer_window.setFont(font)
        self.Answer_window.setText("")
        self.Answer_window.setWordWrap(True)
        self.Answer_window.setObjectName("Answer_window")
        self.gridLayout_2.addWidget(self.Answer_window, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dictionary App"))
        self.Synonym_button.setText(_translate("MainWindow", "Synonym"))
        self.Title.setText(_translate("MainWindow", "English Dictoinary"))
        self.Meaning_button.setText(_translate("MainWindow", "Meaning"))
        self.Enter_Statement.setText(_translate("MainWindow", "Enter Word:"))
        self.Antonym_button.setText(_translate("MainWindow", "Antonym"))
    def is_internet_available(self):
        try:
            urlopen('http://google.com', timeout=1)
            return True
        except:
            return False
    print(is_internet_available)

    def clicked_search_meaning(self):
        try:
            if self.is_internet_available():
                print(self.Search_Box.text().casefold())
                self.Eng_meaning = Eng_dict.meaning(self.Search_Box.text().casefold())
                self.mean = ""
                for k, v in self.Eng_meaning.items():
                    c = 0
                    if k == 'Noun' or k == 'Verb' or k == 'Adjective' or k == 'Adverb':
                        self.mean = self.mean + "\n" + k + ":\n"
                    for m in v:
                        c += 1
                        self.mean = self.mean + str(c) + ". " + m.capitalize() + "\n"
                self.Answer_window.setText(self.mean)
                print(self.mean)
                print(self.Eng_meaning)
            else:
                self.Answer_window.setText("You are not connected to internet!")
        except:
            self.Answer_window.setText("Your word is not present in the Dictionary!")

    def clicked_search_synonym(self):
        try:
            if self.is_internet_available():
                self.Eng_synonym = Eng_dict.synonym(self.Search_Box.text().casefold())
                self.syn = "Synonym:\n"
                c = 0
                for s in self.Eng_synonym:
                    c += 1
                    self.syn = self.syn + str(c) + ". " + s.capitalize() + "\n"
                self.Answer_window.setText(self.syn)
                print(self.syn)
                print(self.Eng_synonym)
            else:
                self.Answer_window.setText("You are not connected to internet!")
        except:
            self.Answer_window.setText("Your word is not present in the Dictionary!")

    def clicked_search_antonym(self):
        try:
            if self.is_internet_available():
                self.Eng_antonym = Eng_dict.antonym(self.Search_Box.text().casefold())
                self.ant = "Antonym:\n"
                c = 0
                for a in self.Eng_antonym:
                    c += 1
                    self.ant = self.ant + str(c) + ". " + a.capitalize() + "\n"
                self.Answer_window.setText(self.ant)
                print(self.ant)
                print(self.Eng_antonym)
            else:
                self.Answer_window.setText("You are not connected to internet!")
        except:
            self.Answer_window.setText("Your word is not present in the Dictionary!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
