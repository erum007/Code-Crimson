import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Load background image
        pixmap = QPixmap("background_image.jpg")
        # Create a label to display the background image
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        # Resize the label to cover the entire window
        self.background_label.resize(self.size())

        # Create buttons
        button1 = QPushButton("Button 1", self)
        button2 = QPushButton("Button 2", self)
        button3 = QPushButton("Button 3", self)

        # Create a vertical layout to arrange the buttons
        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        # Set the layout of the window
        self.setLayout(vbox)

        # Set the background label as the parent widget of the buttons
        button1.setParent(self.background_label)
        button2.setParent(self.background_label)
        button3.setParent(self.background_label)

        self.setWindowTitle("Game")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GameWindow()
    sys.exit(app.exec_())
