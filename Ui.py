from PyQt5 import QtWidgets, QtGui, QtCore


"""
    Классы для самих окон
"""


class StartWindowUi:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(473, 455)
        Form.setMinimumSize(QtCore.QSize(473, 455))
        Form.setMaximumSize(QtCore.QSize(473, 455))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 160, 160, 220))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.body = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.body.setContentsMargins(0, 0, 0, 0)
        self.body.setObjectName("body")
        self.RTE = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.RTE.setMinimumSize(QtCore.QSize(0, 50))
        self.RTE.setObjectName("RTE")
        self.body.addWidget(self.RTE)
        self.ETR = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ETR.setMinimumSize(QtCore.QSize(0, 50))
        self.ETR.setObjectName("ETR")
        self.body.addWidget(self.ETR)
        self.newWords = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.newWords.setMinimumSize(QtCore.QSize(0, 50))
        self.newWords.setObjectName("newWords")
        self.body.addWidget(self.newWords)
        self.settings = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settings.setMinimumSize(QtCore.QSize(0, 50))
        self.settings.setObjectName("settings")
        self.body.addWidget(self.settings)
        self.ETR.raise_()
        self.newWords.raise_()
        self.RTE.raise_()
        self.settings.raise_()
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 20, 291, 125))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.title = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.title.setContentsMargins(0, 0, 0, 0)
        self.title.setObjectName("title")
        self.r = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.r.setFont(font)
        self.r.setAlignment(QtCore.Qt.AlignCenter)
        self.r.setObjectName("r")
        self.title.addWidget(self.r)
        self.a = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.a.setFont(font)
        self.a.setAlignment(QtCore.Qt.AlignCenter)
        self.a.setObjectName("a")
        self.title.addWidget(self.a)
        self.m = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.m.setFont(font)
        self.m.setAlignment(QtCore.Qt.AlignCenter)
        self.m.setObjectName("m")
        self.title.addWidget(self.m)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(6, 410, 461, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Shark"))
        self.RTE.setText(_translate("Form", "Русский --> Английский"))
        self.ETR.setText(_translate("Form", "Английский --> Русский"))
        self.newWords.setText(_translate("Form", "Загрузка новых слов"))
        self.settings.setText(_translate("Form", "Настройки"))
        self.r.setText(_translate("Form", "REPEAT"))
        self.a.setText(_translate("Form", "AFTER"))
        self.m.setText(_translate("Form", "ME"))
        self.label.setText(_translate("Form", "TextLabel"))


class SettingWindowUi:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(346, 459)
        Form.setMinimumSize(QtCore.QSize(346, 459))
        Form.setMaximumSize(QtCore.QSize(346, 459))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 304, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sayRight = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.sayRight.setChecked(False)
        self.sayRight.setObjectName("sayRight")
        self.verticalLayout.addWidget(self.sayRight)
        self.passAnotherWork = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.passAnotherWork.setObjectName("passAnotherWork")
        self.verticalLayout.addWidget(self.passAnotherWork)
        self.deleteAll = QtWidgets.QPushButton(Form)
        self.deleteAll.setGeometry(QtCore.QRect(90, 210, 151, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 12, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.deleteAll.setPalette(palette)
        self.deleteAll.setAutoFillBackground(False)
        self.deleteAll.setStyleSheet("background-color: rgb(255, 12, 36);\n"
                                     "font-color:rgb(255, 255, 0)")
        self.deleteAll.setObjectName("deleteAll")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(100, 360, 141, 61))
        self.save.setObjectName("save")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(36, 310, 271, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.sayRight.setText(
            _translate("Form", "Говорить правильный ответ после каждого вопроса."))
        self.passAnotherWork.setText(_translate("Form", "Пропущенные слова, повторяются."))
        self.deleteAll.setText(_translate("Form", "Удалить все слова."))
        self.save.setText(_translate("Form", "Подтвердить"))
        self.label.setText(_translate("Form", "TextLabel"))


class CheckWindowUi:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 349)
        Form.setMinimumSize(QtCore.QSize(543, 349))
        Form.setMaximumSize(QtCore.QSize(543, 349))
        self.modeName = QtWidgets.QLabel(Form)
        self.modeName.setGeometry(QtCore.QRect(110, 30, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.modeName.setFont(font)
        self.modeName.setAlignment(QtCore.Qt.AlignCenter)
        self.modeName.setObjectName("modeName")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 120, 411, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.main.setContentsMargins(0, 0, 0, 0)
        self.main.setObjectName("main")
        self.question = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.question.setAutoFillBackground(False)
        self.question.setReadOnly(True)
        self.question.setObjectName("question")
        self.main.addWidget(self.question)
        self.cursor = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cursor.setFont(font)
        self.cursor.setObjectName("cursor")
        self.main.addWidget(self.cursor)
        self.answer = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.answer.setObjectName("answer")
        self.main.addWidget(self.answer)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 230, 211, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.menu = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.menu.setContentsMargins(0, 0, 0, 0)
        self.menu.setObjectName("menu")
        self.continueButtons = QtWidgets.QHBoxLayout()
        self.continueButtons.setObjectName("continueButtons")
        self.check = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.check.setObjectName("check")
        self.continueButtons.addWidget(self.check)
        self.passW = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.passW.setObjectName("passW")
        self.continueButtons.addWidget(self.passW)
        self.menu.addLayout(self.continueButtons)
        self.endButton = QtWidgets.QHBoxLayout()
        self.endButton.setObjectName("endButton")
        self.end = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.end.setObjectName("end")
        self.endButton.addWidget(self.end)
        self.menu.addLayout(self.endButton)
        self.words = QtWidgets.QLabel(Form)
        self.words.setGeometry(QtCore.QRect(10, 240, 91, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.words.setFont(font)
        self.words.setAlignment(QtCore.Qt.AlignCenter)
        self.words.setObjectName("words")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.modeName.setText(_translate("Form", "Русский --> Английский"))
        self.cursor.setText(_translate("Form", "--->"))
        self.check.setText(_translate("Form", "Проверить"))
        self.passW.setText(_translate("Form", "Пропустить"))
        self.end.setText(_translate("Form", "Закончить тест"))
        self.words.setText(_translate("Form", "0/0"))


class FinishWindowUi:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(659, 452)
        Form.setMinimumSize(QtCore.QSize(659, 452))
        Form.setMaximumSize(QtCore.QSize(659, 452))
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 70, 551, 301))
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.loadResult = QtWidgets.QPushButton(Form)
        self.loadResult.setGeometry(QtCore.QRect(490, 410, 141, 23))
        self.loadResult.setObjectName("loadResult")
        self.header = QtWidgets.QLabel(Form)
        self.header.setGeometry(QtCore.QRect(70, 20, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(30, 400, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.restart = QtWidgets.QPushButton(Form)
        self.restart.setGeometry(QtCore.QRect(280, 410, 181, 23))
        self.restart.setObjectName("restart")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Shark"))
        self.loadResult.setText(_translate("Form", "Загрузить результат"))
        self.header.setText(_translate("Form", "Тест завершен."))
        self.result.setText(_translate("Form", "Результат: 0/0"))
        self.restart.setText(_translate("Form", "Вернуться на главный экран"))


class ConfirmUi:
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(243, 132)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 90, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 231, 81))
        self.label.setMinimumSize(QtCore.QSize(231, 81))
        self.label.setMaximumSize(QtCore.QSize(231, 16777215))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "                          Вы уверены?"))