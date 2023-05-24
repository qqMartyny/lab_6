import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем поле вывода результата
        self.result = QLineEdit()

        # Создаем кнопки с цифрами
        self.button_0 = QPushButton('0')
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')

        # Создаем кнопки с операциями
        self.button_plus = QPushButton('+')
        self.button_minus = QPushButton('-')
        self.button_multiply = QPushButton('*')
        self.button_divide = QPushButton('/')
        self.button_point = QPushButton('.')
        self.button_equal = QPushButton('=')
        self.button_clear = QPushButton('C')

        # Добавляем обработчики событий для кнопок
        self.button_0.clicked.connect(self.buttonClicked)
        self.button_1.clicked.connect(self.buttonClicked)
        self.button_2.clicked.connect(self.buttonClicked)
        self.button_3.clicked.connect(self.buttonClicked)
        self.button_4.clicked.connect(self.buttonClicked)
        self.button_5.clicked.connect(self.buttonClicked)
        self.button_6.clicked.connect(self.buttonClicked)
        self.button_7.clicked.connect(self.buttonClicked)
        self.button_8.clicked.connect(self.buttonClicked)
        self.button_9.clicked.connect(self.buttonClicked)
        self.button_plus.clicked.connect(self.buttonClicked)
        self.button_minus.clicked.connect(self.buttonClicked)
        self.button_multiply.clicked.connect(self.buttonClicked)
        self.button_divide.clicked.connect(self.buttonClicked)
        self.button_point.clicked.connect(self.buttonClicked)
        self.button_equal.clicked.connect(self.equalClicked)
        self.button_clear.clicked.connect(self.clearClicked)

        # Добавляем элементы на компоновщик 1
        line_1 = QHBoxLayout()
        line_1.addWidget(self.button_clear)
        line_1.addWidget(self.result)

        # Добавляем элементы на компоновщик 2
        line_2 = QHBoxLayout()
        line_2.addWidget(self.button_7)
        line_2.addWidget(self.button_8)
        line_2.addWidget(self.button_9)
        line_2.addWidget(self.button_plus)

        # Добавляем элементы на компоновщик 3
        line_3 = QHBoxLayout()
        line_3.addWidget(self.button_4)
        line_3.addWidget(self.button_5)
        line_3.addWidget(self.button_6)
        line_3.addWidget(self.button_minus)

        # Добавляем элементы на компоновщик 4
        line_4 = QHBoxLayout()
        line_4.addWidget(self.button_1)
        line_4.addWidget(self.button_2)
        line_4.addWidget(self.button_3)
        line_4.addWidget(self.button_multiply)

        # Добавляем элементы на компоновщик 5
        line_5 = QHBoxLayout()
        line_5.addWidget(self.button_0)
        line_5.addWidget(self.button_point)
        line_5.addWidget(self.button_equal)
        line_5.addWidget(self.button_divide)

        # Создаем вертикальный компоновщик
        vbox = QVBoxLayout()
        vbox.addLayout(line_1)
        vbox.addLayout(line_2)
        vbox.addLayout(line_3)
        vbox.addLayout(line_4)
        vbox.addLayout(line_5)

        # Устанавливаем компоновщик в окне
        self.setLayout(vbox)

    def buttonClicked(self):
        button = self.sender()
        value = button.text()
        current_value = self.result.text()
        self.result.setText(current_value + value)

    def clearClicked(self):
        self.result.setText('')

    def equalClicked(self):
        try:
            result = str(eval(self.result.text()))
        except:
            result = 'Error'
        self.result.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
