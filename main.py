import sys
from random import choice

import sqlite3
import csv
import os
import xlrd

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem, QDialog
from PyQt5.QtCore import Qt

from Ui import *


sett = {'Say Right': 0,
        'Pass anotherWork': 0}


class WrongType(Exception):
    pass


class NotFiles(Exception):
    pass


class StartWindow(QWidget, StartWindowUi):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.setupUi(self)
        self.newWords.clicked.connect(self.load_new_words)
        self.RTE.clicked.connect(self.body_act)
        self.ETR.clicked.connect(self.body_act)
        self.settings.clicked.connect(self.settings_act)
        self.label.hide()

    def load_new_words(self):
        """
        Добавляет новые слова в формате Русские; Английские
        (Если вариантов РУССКОГО несколько, то принимаются через запятую
        (Английский не поддерживается))
        Принимается CSV SQlite XLSX
        """
        file_name = QFileDialog.getOpenFileName(self, 'Выберите таблицу с новыми словами',
                                                '', '(*.csv);;(*.db);;(*.xlsx)')
        try:
            if 'base' not in os.listdir():
                os.mkdir('base')
            if file_name[1] == '(*.csv)':
                with open(f'base/{file_name[0].split("/")[-1]}',
                          'w', encoding='utf-8') as csv_new_file:
                    with open(file_name[0], 'r', encoding='utf-8') as csv_file:
                        reader = csv.reader(csv_file, delimiter=';', quotechar='"')
                        writer = csv.writer(csv_new_file, delimiter=';',
                                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        for i in reader:
                            if i == []:
                                continue
                            if len(i) != 2:
                                raise WrongType
                            writer.writerow(i)
            elif file_name[1] == '(*.db)':
                con = sqlite3.connect(file_name[0])
                cur = con.cursor()
                with open(f'base/{file_name[0].split("/")[-1][:-3]}.csv',
                          'w', encoding='utf-8') as csv_new_file:
                    writer = csv.writer(csv_new_file, delimiter=';',
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for i in cur.execute("SELECT rus, eng FROM words").fetchall():
                        if len(i) != 2:
                            raise WrongType
                        writer.writerow(i)
            elif file_name[1] == '(*.xlsx)':
                lst = []
                rb = xlrd.open_workbook(file_name[0])
                sheet = rb.sheet_by_index(0)
                for row_num in range(sheet.nrows):
                    lst.append(sheet.row_values(row_num))
                with open(f'base/{file_name[0].split("/")[-1][:-5]}.csv',
                          'w', encoding='utf-8') as csv_file:
                    writer = csv.writer(csv_file, delimiter=';', quotechar='"')
                    for i in lst:
                        if len(i) != 2:
                            raise WrongType
                        writer.writerow(i)
        except WrongType:
            self.label.setText('Неправильный формат файла')
            self.label.setVisible(True)
            os.remove(f'base/{file_name[0].split("/")[-1][:-(len(file_name[1]) - 3)]}.csv')
        except Exception as e:
            print(e)

    def body_act(self):
        """
            Переход к решению тестов.
            Принимает сигнал от названия кнопок RTE (Rus To Eng) и противоположный ETR
        """
        try:
            if self.sender().objectName() == 'RTE':
                how_to_check = [0, 1]
            else:
                how_to_check = [1, 0]
            if not os.listdir('base'):
                raise NotFiles
            self.new_window = CheckWindow(how_to_check, self.sender().text())
            self.new_window.show()
            self.close()
            self.wind.close()
        except AttributeError:
            pass
        except NotFiles:
            self.label.setText('Отсутсвуют слова')
            self.label.setVisible(True)

    def settings_act(self):
        self.wind = SettingsWindow()
        self.wind.show()


class SettingsWindow(QWidget, SettingWindowUi):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.setupUi(self)
        self.label.hide()
        self.save.clicked.connect(self.save_act)
        self.deleteAll.clicked.connect(self.delete_act)
        if sett['Pass anotherWork']:
            self.passAnotherWork.setChecked(True)
        if sett['Say Right']:
            self.sayRight.setChecked(True)

    def save_act(self):
        """
        Настройки
        Pass anotherWork => Повтор пропущенных слов
        sayRight => Вывод правильных ответов
        """
        if self.passAnotherWork.isChecked():
            sett['Pass anotherWork'] = True
        else:
            sett['Pass anotherWork'] = False
        if self.sayRight.isChecked():
            sett['Say Right'] = True
        else:
            sett['Say Right'] = False
        self.close()

    def delete_act(self):
        self.wind = Confirm()
        self.wind.show()
        k = self.wind.exec_()
        if k:
            directory_files = os.listdir('base')
            for i in directory_files:
                os.remove(f'base/{i}')


class CheckWindow(QWidget, CheckWindowUi):
    def __init__(self, how_to_check, text):
        super(CheckWindow, self).__init__()
        self.setupUi(self)
        self.modeName.setText(text)
        self.check.clicked.connect(self.check_act)
        self.passW.clicked.connect(self.check_act)
        self.end.clicked.connect(self.finish_act)
        self.load_words(how_to_check)
        self.answers = list()
        self.choose_new_word()

    def load_words(self, how_to_check):
        """
        Загрузка всех слов из файлов из папки base
        """
        try:
            lst_of_words = []
            directory_files = os.listdir('base')
            for names in directory_files:
                with open(f'base/{names}', encoding='utf-8') as csv_file:
                    reader = csv.reader(csv_file, delimiter=';', quotechar=';')
                    for row in reader:
                        if not row:
                            continue
                        now_lst = []
                        if how_to_check[0] == 1:
                            now_lst.append(row[1])
                            now_lst.append(row[0].split(','))
                        else:
                            now_lst.append(row[0])
                            now_lst.append([row[1]])
                        lst_of_words.append(tuple(now_lst))
            self.lst_of_words = lst_of_words
        except Exception as e:
            print(e)

    def choose_new_word(self):
        new_turn = choice(self.lst_of_words)
        del self.lst_of_words[self.lst_of_words.index(new_turn)]
        self.current_answer = new_turn[1]
        self.question.setText(new_turn[0])
        self.words.setText(f'{len(self.answers) + 1}/'
                           f'{len(self.lst_of_words) + 1 + len(self.answers)}')

    def check_act(self):
        """Cрабатывает при нажатии любой кнопки в интерфейсе (или Enter = Проверка)"""
        if sett['Say Right']:
            self.wind = Confirm(self.current_answer)
            self.wind.show()
            self.wind.exec_()
        if self.sender().objectName() == 'check':
            k = True
            if not self.answer.text():
                self.wind = Confirm()
                self.wind.show()
                k = self.wind.exec_()
            if k:
                self.answers.append((self.question.text(), self.current_answer, self.answer.text()))
        elif self.sender().objectName() == 'passW':
            if sett['Pass anotherWork']:
                self.lst_of_words.append((self.question.text(), self.current_answer))
            else:
                self.answers.append((self.question.text(), self.current_answer, ''))
        else:
            self.answers.append((self.question.text(), self.current_answer, ''))
        self.answer.setText('')
        if self.lst_of_words:
            self.choose_new_word()
        else:
            self.final()

    def finish_act(self):
        "Принудительное завершение"
        self.wind = Confirm()
        self.wind.show()
        k = self.wind.exec_()
        if k:
            f = sett['Say Right']
            sett['Say Right'] = 0
            while self.lst_of_words:
                self.check_act()
            self.check_act()
            sett['Say Right'] = f
            self.final()

    def final(self):
        self.wind = FinishWindow(self.answers, len(self.answers))
        self.wind.show()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.check.click()


class FinishWindow(QWidget, FinishWindowUi):
    def __init__(self, res, le):
        super(FinishWindow, self).__init__()
        self.setupUi(self)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.right = 0
        self.res = res
        self.le = le
        self.load_table(self.res)
        self.result.setText(f'Результат: {self.right}/{self.le}')
        self.restart.clicked.connect(self.restart_act)
        self.loadResult.clicked.connect(self.load_result)

    def load_table(self, result):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Вопрос', 'Ответ', 'Ваш ответ'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(1)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if type(elem) is list:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(','.join(elem)))
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
            if row[2] in row[1]:
                self.right += 1
                self.color_row(i, QtGui.QColor(0, 255, 0))
            else:
                self.color_row(i, QtGui.QColor(255, 0, 0))

    def restart_act(self):
        self.wind = StartWindow()
        self.wind.show()
        self.close()

    def load_result(self):
        """Загружает результыты в виде csv В формате
        Русское слово; Английское слово; Ответ
        В конце колл-во правильных ответов"""
        with open('result.csv', 'w', encoding='utf-8') as csv_new_file:
            writer = csv.writer(csv_new_file, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in self.res:
                writer.writerow(i)
            writer.writerow(['Результат', self.right, self.le])

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)


class Confirm(QDialog, ConfirmUi):
    def __init__(self, label=''):
        super(Confirm, self).__init__()
        self.setupUi(self)
        if label:
            self.label.setText(f'Правильный ответ: {label[0]}')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
