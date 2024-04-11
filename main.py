# запрограммируй сложный тест
# подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox,
                             QRadioButton, QGroupBox, QButtonGroup)
from random import *

app = QApplication([])
main_win = QWidget()
main_win.resize(300, 200)
main_win.setWindowTitle("Memory card")


# создание виджетов главного окна

class Question():
    def __init__(self, question, ans_verno, ans2, ans3, ans4):
        self.question = question
        self.ans_verno = ans_verno
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4


questions = []
questions.append(Question("Какой сейчас год?", "2023", "2000", "3023", "2018"))
questions.append(Question("Сколько будет 77 + 33?", "110", "100", "90", "8"))
questionsLen = len(questions) + 1

group = QGroupBox("Варианты ответов")

question = QLabel("Какой национальности не существует?")
ans1 = QRadioButton("Энцы")
ans2 = QRadioButton("Чулымцы")
ans3 = QRadioButton("Смурфы")
ans4 = QRadioButton("Алеуты")

gropuWid = QButtonGroup()
gropuWid.addButton(ans1)
gropuWid.addButton(ans2)
gropuWid.addButton(ans3)
gropuWid.addButton(ans4)

answers = [ans3, ans1, ans2, ans4]

button1 = QPushButton("Ответить")

hbox = QVBoxLayout()

question_box = QHBoxLayout()
group_box = QHBoxLayout()
butt_box = QHBoxLayout()

hbox.addLayout(question_box)
hbox.addLayout(group_box)
hbox.addLayout(butt_box)

question_box.addWidget(question)
butt_box.addWidget(button1)

ans_layout = QVBoxLayout()
ans_layout1 = QHBoxLayout()
ans_layout2 = QHBoxLayout()

ans_layout1.addWidget(ans1)
ans_layout1.addWidget(ans3)
ans_layout2.addWidget(ans2)
ans_layout2.addWidget(ans4)

ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)
group.setLayout(ans_layout)

group_box.addWidget(group)

group_otvet = QGroupBox("Результат теста")
texts = QVBoxLayout()
pravilno = QLabel("Правильно/Неправильно")
otvet = QLabel("Ответ")

printText1 = QHBoxLayout()
printText1.addWidget(pravilno)
printText2 = QHBoxLayout()
printText2.addWidget(otvet)

texts.addLayout(printText1)
texts.addLayout(printText2)
group_otvet.setLayout(texts)
group_box.addWidget(group_otvet)
group_otvet.hide()

count = 0


def show_correct(x):
    if x:
        pravilno.setText("Правильно")
        global count
        count += 1
        otvet.setText(answers[0].text())
        group.hide()
        group_otvet.show()
        button1.setText("Следующий вопрос")
    else:
        pravilno.setText("Неправильно")
        otvet.setText(answers[0].text())
        group.hide()
        group_otvet.show()
        button1.setText("Следующий вопрос")


def next_question():
    if len(questions) == 0:
        button1.setText("Результат")
        result(count)
    else:
        ask(questions[randint(0, len(questions) - 1)])


def ask(x):
    shuffle(answers)
    answers[0].setText(x.ans_verno)
    answers[1].setText(x.ans2)
    answers[2].setText(x.ans3)
    answers[3].setText(x.ans4)
    question.setText(x.question)
    show_question()
    button1.setText("Ответить")
    questions.remove(x)


def result(count):
    lose = QMessageBox()
    lose.setText("Вы ответили на " + str(count) + " вопрос(а) из " + str(questionsLen))
    lose.exec_()


def show_question():
    group_otvet.hide()
    group.show()
    gropuWid.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    gropuWid.setExclusive(True)


def check_answer():
    if answers[0].isChecked():
        show_correct(True)

    else:
        for i in range(1, len(answers)):
            if answers[i].isChecked():
                show_correct(False)
                break


def button_click():
    if button1.text() == "Ответить":
        check_answer()
    elif button1.text() == "Результат":
        result(count)
    else:
        next_question()


button1.clicked.connect(button_click)

main_win.setLayout(hbox)

main_win.show()
app.exec_()
