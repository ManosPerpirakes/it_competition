from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from random import randint, shuffle

def frb1():
    global a1
    global a2
    global a3
    a1 = True
    a2 = False
    a3 = False

def frb2():
    global a1
    global a2
    global a3
    a1 = False
    a2 = True
    a3 = False

def frb3():
    global a1
    global a2
    global a3
    a1 = False
    a2 = False
    a3 = True

def show_q():
    global keys
    global w
    global correct_ans_index
    if len(keys) == 0:
        w.hide()
        w = QWidget()
        w.resize(400, 400)
        w.setWindowTitle("Quiz")
        label = QLabel("Τέλος του quiz!\nΠόντοι: " + str(points))
        label.setFont(QFont('Arial', 15))
        layout = QVBoxLayout()
        layout.addWidget(label, alignment = Qt.AlignmentFlag.AlignHCenter)
        w.setLayout(layout)
        w.show()
    else:
        index = randint(0, len(keys)-1)
        key = keys[index]
        l1.setText(key)
        shuffle(dictionary[key])
        lcounter = 0
        for i in dictionary[key]:
            if len(i[0]) > 1:
                radiobuttons[lcounter].setText(i[0])
                correct_ans_index = lcounter
            else:
                radiobuttons[lcounter].setText(i)
            lcounter += 1
        keys.remove(keys[index])

def nq():
    global points
    global correct_ans_index
    if a1 and correct_ans_index == 0:
        points += 1
    elif a2 and correct_ans_index == 1:
        points += 1
    elif a3 and correct_ans_index == 2:
        points += 1
    show_q()

app = QApplication([])
w = QWidget()
w.resize(400, 400)
w.setWindowTitle("Quiz")
l1 = QLabel()
l1.setFont(QFont('Arial', 15))
rb1 = QRadioButton()
rb1.setFont(QFont('Arial', 15))
rb2 = QRadioButton()
rb2.setFont(QFont('Arial', 15))
rb3 = QRadioButton()
rb3.setFont(QFont('Arial', 15))
pb1 = QPushButton("Υποβολή")
pb1.setFont(QFont('Arial', 15))
lv1 = QVBoxLayout()
lv1.addWidget(l1, alignment = Qt.AlignmentFlag.AlignHCenter)
radiobuttons = [rb1, rb2, rb3]
for i in radiobuttons:
    lv1.addWidget(i, alignment = Qt.AlignmentFlag.AlignHCenter)
lv1.addWidget(pb1, alignment = Qt.AlignmentFlag.AlignHCenter)
w.setLayout(lv1)
w.show()
keys = ["Ερώτηση 1", "Ερώτηση 2", "Ερώτηση 3", "Ερώτηση 4"]
dictionary = {
    "Ερώτηση 1": ["απάντηση 1_1", ["απάντηση 1_2"], "απάντηση 1_3"],
    "Ερώτηση 2": ["απάντηση 2_1", "απάντηση 2_2", ["απάντηση 2_3"]],
    "Ερώτηση 3": [["απάντηση 3_1"], "απάντηση 3_2", "απάντηση 3_3"],
    "Ερώτηση 4": ["απάντηση 4_1", ["απάντηση 4_2"], "απάντηση 4_3"]
}
show_q()
a1 = False
a2 = False
a3 = False
points = 0
rb1.clicked.connect(frb1)
rb2.clicked.connect(frb2)
rb3.clicked.connect(frb3)
pb1.clicked.connect(nq)
app.exec()