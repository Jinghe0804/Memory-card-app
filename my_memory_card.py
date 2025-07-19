from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QButtonGroup,
    QPushButton, QLabel)

from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Which of the option is not part of human's blood", 'Bacteriophage', 'Red blood cell', 'Platlets', 'Plasma'))
question_list.append(Question("What factor changes the growth rate of microorganisms", 'Temperature', 'Object', 'Enemies', 'Immune system'))
question_list.append(Question("How many races are there in Malaysia", 'Five', 'Eight', 'Three', 'Chinese'))
question_list.append(Question("What is the biggest country in the world(size wise)", "Russia", "China", "India", 'United States'))
question_list.append(Question("How many days are in a year", "365 days 1/4 hours", "365 days", "300 days", "400 days"))
question_list.append(Question("What are the causes of global warming", "Pollution", "Earth is rotating faster", "The moon is getting further from earth", "Replanting trees"))
question_list.append(Question("What newest event collab in Fortnite", "Miku collab", "Skibidi toilet collab", "Rocket league collab", "Fornite x Fornite event"))
question_list.append(Question("Who is the friendly neighbourhood hero", "Spiderman", "Iron Man", "Thor", "Groot"))
question_list.append(Question("Why did the skibidi invade cameraheads?","To conquer the world", "to find the Eye of rah", "To steal bidets", "To buy a property in egypt"))
question_list.append(Question("What do they do if you buy a property in egypt?", "They give you the property", "To give you eye of rah", "To reclaim the lost cheeto dread", "A mummy"))

app = QApplication([])

btn_OK = QPushButton('Answer')

lb_Question = QLabel('The most difficult question in the world!! (Scary!!)')

RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

vertical_layout1 = QVBoxLayout()
vertical_layout1.addWidget(rbtn_1)
vertical_layout1.addWidget(rbtn_2)

vertical_layout2 = QVBoxLayout()
vertical_layout2.addWidget(rbtn_3)
vertical_layout2.addWidget(rbtn_4)

horizontal_layout = QHBoxLayout()
horizontal_layout.addLayout(vertical_layout1)
horizontal_layout.addLayout(vertical_layout2)

RadioGroupBox.setLayout(horizontal_layout)

label_result = QLabel('Are you correct or not??')
label_correct = QLabel('Ready for the next question?')

result_layout = QVBoxLayout()
result_layout.addWidget(label_result, alignment=Qt.AlignLeft)
result_layout.addWidget(label_correct, alignment=Qt.AlignCenter)

ResultGroupBox = QGroupBox("Test result")
ResultGroupBox.setLayout(result_layout)

main_layout1 = QHBoxLayout()
main_layout2 = QHBoxLayout()
main_layout3 = QHBoxLayout()

main_layout1.addWidget(lb_Question, alignment=Qt.AlignHCenter)

main_layout2.addWidget(RadioGroupBox)
main_layout2.addWidget(ResultGroupBox)
ResultGroupBox.hide()

main_layout3.addStretch(1)
main_layout3.addWidget(btn_OK, stretch=1)
main_layout3.addStretch(1)

window_layout_card = QVBoxLayout()

window_layout_card.addLayout(main_layout1, stretch=2)
window_layout_card.addLayout(main_layout2, stretch=8)
window_layout_card.addStretch(1)
window_layout_card.addLayout(main_layout3, stretch=1)
window_layout_card.addStretch(1)
window_layout_card.setSpacing(20)

def show_result():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    ResultGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    ''' the function writes the value of the question and answers into the corresponding widgets while distributing the answer options randomly '''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    label_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    ''' show result - put the written text into "result" and show the corresponding panel '''
    label_result.setText(res)
    show_result()

def check_answer():
    ''' if an answer option was selected, check and show answer panel ''' 
    if answers[0].isChecked():
        show_correct('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0 
    q = question_list[window.cur_question]
    ask(q)

def click_Ok():
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(window_layout_card)
window.setWindowTitle('Memory Card')
window.cur_question = -1
btn_OK.clicked.connect(click_Ok)
next_question()
window.show()
app.exec()