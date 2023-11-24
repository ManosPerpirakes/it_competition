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
        w.resize(1000, 600)
        w.setWindowTitle("Quiz")
        label = QLabel("Τέλος του quiz!\nΠόντοι: " + str(points) + "\n")
        labeltext = label.text()
        for i in answers_db:
            labeltext += '\n'
            labeltext += i + " "
            labeltext += answers_db[i]
            labeltext += "\n"
        label.setText(labeltext)
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
w.resize(1000, 600)
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
keys = [
    "Αν κάποιος δημοσιεύσει προσωπικά μου στοίχεια παρά τη θελήση μου\n (φωτογραφικό υλικό ή γραπτό μύνημα) πώς πρέπει να δράσω;",
    "Κάποιος γνωστός μου, μου στέλνει προσωπικά στοιχεία όπως τηλέφωνο\n, pin καρτών, κτλ πώς αντιδρώ;",
    "Υπάρχουν διάφοροι χρήστες που εκφράζουν την άποψή τους πάνω σε ένα\n θέμα που είτε συμφωνώ είτε διαφωνώ, τι κάνω;",
    "Όταν θέλω να κάνω εγγραφή σε έναν ιστότοπο και μου λέει να κοινοποιήσω\n τα στοιχεία μου, τι κάνω;",
    "Λαμβάνω ένα mail από άγνωστο αποστολέα με έναν ιστότοπο παροτρύνοντας με\n να μπω, τι κάνω;",
    "Πώς καταλαβαίνω ότι ένας ιστότοπος είναι ασφαλής;"
]
dictionary = {
    "Αν κάποιος δημοσιεύσει προσωπικά μου στοίχεια παρά τη θελήση μου\n (φωτογραφικό υλικό ή γραπτό μύνημα) πώς πρέπει να δράσω;": ["Να ειδοποιήσω έναν φίλο μου", "Να στείλω σε αυτόν τον χρήστη μύνημα ώστε να το διαγράψει", ["Να ενημερώσω τους γονείς μου άμεσα"]],
    "Κάποιος γνωστός μου, μου στέλνει προσωπικά στοιχεία όπως τηλέφωνο\n, pin καρτών, κτλ πώς αντιδρώ;": ["Τα διαβάζω και του δίνω και δικά μου", "τα δημοσιεύω για πλάκα", ["του επισημαίνω να τα σβήσει και να τ' αλλάζει"]],
    "Υπάρχουν διάφοροι χρήστες που εκφράζουν την άποψή τους πάνω σε ένα\n θέμα που είτε συμφωνώ είτε διαφωνώ, τι κάνω;": ["Τους προσβάλω και τους αντιμιλάω", ["Εκφράζω την άποψή μου, με ευγένεια και επιχειρήματα"], "δεν ασχολούμαι καθόλου"],
    "Όταν θέλω να κάνω εγγραφή σε έναν ιστότοπο και μου λέει να κοινοποιήσω\n τα στοιχεία μου, τι κάνω;": ["Τα κοινοποιώ", "Δεν τα κοινοποιώ", ["Δεν κάνω πλήρη εγγραφή και δεν κοινοποιώ τα στοιχεία μου"]],
    "Λαμβάνω ένα mail από άγνωστο αποστολέα με έναν ιστότοπο παροτρύνοντας με\n να μπω, τι κάνω;": ["Τον ανοίγω και τον ακολουθώ", ["Δεν το ανοίγω"], "προωθώ το mail σε εναν φίλο μου"],
    "Πώς καταλαβαίνω ότι ένας ιστότοπος είναι ασφαλής;": [["Στα αρχικά HTTPS το γράμμα S σημαίνει secure οπότε μπορώ να επισκεφτώ αυτόν τον ιστότοπο"], "Μου το είπε ένας φίλος μου", "Δεν με νοιάζει αν ένας ιστότοπος είναι ασφαλής"]
}
answers_db = {
    "Αν κάποιος δημοσιεύσει προσωπικά μου στοίχεια παρά τη θελήση μου (φωτογραφικό υλικό ή γραπτό μύνημα) πώς πρέπει να δράσω;": "Να ενημερώσω τους γονείς μου άμεσα",
    "Κάποιος γνωστός μου, μου στέλνει προσωπικά στοιχεία όπως τηλέφωνο, pin καρτών, κτλ πώς αντιδρώ;": "του επισημαίνω να τα σβήσει και να τ' αλλάζει",
    "Υπάρχουν διάφοροι χρήστες που εκφράζουν την άποψή τους πάνω σε ένα θέμα που είτε συμφωνώ είτε διαφωνώ, τι κάνω;": "Εκφράζω την άποψή μου, με ευγένεια και επιχειρήματα",
    "Όταν θέλω να κάνω εγγραφή σε έναν ιστότοπο και μου λέει να κοινοποιήσω τα στοιχεία μου, τι κάνω;": "Δεν κάνω πλήρη εγγραφή και δεν κοινοποιώ τα στοιχεία μου",
    "Λαμβάνω ένα mail από άγνωστο αποστολέα με έναν ιστότοπο παροτρύνοντας με να μπω, τι κάνω;": "Δεν το ανοίγω",
    "Πώς καταλαβαίνω ότι ένας ιστότοπος είναι ασφαλής;": "Στα αρχικά HTTPS το γράμμα S σημαίνει secure οπότε μπορώ να επισκεφτώ αυτόν τον ιστότοπο"        
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