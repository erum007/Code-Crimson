import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter, QLinearGradient, QColor, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDialog,
    QTextBrowser,
)
import subprocess

from quiz import RBTreeVisualizer  # Import the class from your Python file
from Preorder import RBTreeVisualizerPreorder
from Postorder import RBTreeVisualizerPostorder
from Inorder import RBTreeVisualizerInorder

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Master")
        self.setGeometry(100, 100, 600, 400)
        width = 800
        height = 500
        self.setFixedSize(width, height)

        # Create an instance of the imported class
        self.pyqt_widget = RBTreeVisualizer()

        # Set the widget as the central widget
        self.setCentralWidget(self.pyqt_widget)

class MyWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preorder Traversal")
        self.setGeometry(100, 100, 600, 400)
        width = 800
        height = 500
        self.setFixedSize(width, height)

        # Create an instance of the imported class
        self.pyqt_widget = RBTreeVisualizerPreorder("Preorder")

        # Set the widget as the central widget
        self.setCentralWidget(self.pyqt_widget)

class MyWindow3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Postorder Traversal")
        self.setGeometry(100, 100, 600, 400)
        width = 800
        height = 500
        self.setFixedSize(width, height)

        # Create an instance of the imported class
        self.pyqt_widget = RBTreeVisualizerPostorder("Postorder")

        # Set the widget as the central widget
        self.setCentralWidget(self.pyqt_widget)

class MyWindow4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inorder Traversak")
        self.setGeometry(100, 100, 600, 400)
        width = 800
        height = 500
        self.setFixedSize(width, height)

        # Create an instance of the imported class
        self.pyqt_widget = RBTreeVisualizerInorder("Inorder")

        # Set the widget as the central widget
        self.setCentralWidget(self.pyqt_widget)


class ImageWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.initUI()

    def initUI(self):
        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)  # Scale the image to fit the label

        # Load the image
        pixmap = QPixmap(self.image_path)
        if pixmap.isNull():
            print("Failed to load image.")
            return

        # Set the image pixmap to the label
        self.image_label.setPixmap(pixmap)

        # Create a layout to add the label
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        # Set the layout for the image window
        self.setLayout(layout)

        self.setWindowTitle("Instructions")
        self.show()

class GameScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.traversal_window = None  # Initialize traversal_window as None
        self.init_ui()

    def close_all_windows(self):
        QApplication.closeAllWindows()
        sys.exit()

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomLeft())
        gradient.setColorAt(0, QColor(255, 0, 0))  # First color (white)
        gradient.setColorAt(0.5, QColor(0, 0, 0))  # Second color (black)
        gradient.setColorAt(1, QColor(0, 0, 0))  # Third color (red)
        painter.fillRect(self.rect(), gradient)

    def init_ui(self):
        self.setWindowTitle("Game Screen")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.text_label = QLabel("Welcome To Code Crimson!")
        self.text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text_label)
        self.text_label.setStyleSheet(
            "color:white;"
        )  # Set background color to light red

        font = QFont()
        font.setPointSize(35)  # Adjust the font size as needed
        font.setBold(True)
        self.text_label.setFont(font)

        # Quiz Champ Button
        quiz_champ_btn = QPushButton("Quiz Champ", self)
        quiz_champ_btn.setFont(font)
        quiz_champ_btn.setStyleSheet(
            "background-color: #4CAF50; color: white; border-radius: 10px;"
        )
        quiz_champ_btn.clicked.connect(self.start_quiz_champ)
        layout.addWidget(quiz_champ_btn)

        # Path Master Button
        path_master_btn = QPushButton("Path Master", self)
        path_master_btn.setFont(font)
        path_master_btn.setStyleSheet(
            "background-color: #FFC107; color: white; border-radius: 10px;"
        )
        path_master_btn.clicked.connect(self.show_path_master_options)
        layout.addWidget(path_master_btn)

        # Instructions Button
        instructions_btn = QPushButton("Rules", self)
        instructions_btn.setFont(font)
        instructions_btn.setStyleSheet(
            "background-color: #2196F3; color: white; border-radius: 10px;"
        )
        instructions_btn.clicked.connect(self.show_instructions)
        layout.addWidget(instructions_btn)

        # Exit Button
        exit_btn = QPushButton("Exit", self)
        exit_btn.setFont(font)
        exit_btn.setStyleSheet(
            "background-color: #F44336; color: white; border-radius: 10px;"
        )
        exit_btn.clicked.connect(self.close_all_windows)

        layout.addWidget(exit_btn)

        # Add some space at the bottom
        layout.addSpacing(50)

        self.setLayout(layout)

        # Load Background Image

    def start_quiz_champ(self):
        print("Starting Quiz Champ!")
        # Code to open quiz.py window here
        # subprocess.Popen(
        #     [
        #         "python",
        #         "C:\\Users\\User\\Desktop\\final-project\\final-project\\quiz.py",
        #     ]
        # )
        self.new_window=MyWindow()
        self.new_window.show()

    def show_path_master_options(self):
        print("Starting Path Master Options!")
        # Create a new window for traversal options
        self.traversal_window = TraversalOptionsWindow()
        self.traversal_window.show()

    def show_instructions(self):
        image_path = f"C:\\Users\\User\\Desktop\\Code Crimson Final Project - Erum Naushad and Aliza Fatima\\Code Crimson Final Project - Erum Naushad and Aliza Fatima (1)\\FInal Project With Suggested Changes\\final-project\\instructions.jpg"

        self.image_window = ImageWindow(image_path)
        self.image_window.show()


class TraversalOptionsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Traversal Options")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        # Preorder Traversal Button
        preorder_btn = QPushButton("Preorder Traversal", self)
        preorder_btn.setFont(QFont("Arial", 16))
        preorder_btn.clicked.connect(lambda: self.start_traversal("Preorder"))
        layout.addWidget(preorder_btn)

        # Postorder Traversal Button
        postorder_btn = QPushButton("Postorder Traversal", self)
        postorder_btn.setFont(QFont("Arial", 16))
        postorder_btn.clicked.connect(lambda: self.start_traversal("Postorder"))
        layout.addWidget(postorder_btn)

        # Inorder Traversal Button
        inorder_btn = QPushButton("Inorder Traversal", self)
        inorder_btn.setFont(QFont("Arial", 16))
        inorder_btn.clicked.connect(lambda: self.start_traversal("Inorder"))
        layout.addWidget(inorder_btn)

        self.setLayout(layout)

    def start_traversal(self, traversal_type):
        # Add code to open respective python files based on traversal_type
        print(f"Starting {traversal_type} traversal!")
        # file_name = f"C:\\Users\\User\\Desktop\\final-project\\final-project\\{traversal_type}.py"
        # try:
        #     subprocess.Popen(["python", file_name])
        # except FileNotFoundError:
        #     print(f"Error: File '{file_name}' not found.")
        if traversal_type=="Preorder":
            self.new_window=MyWindow2()
            self.new_window.show()
        elif traversal_type=="Postorder":
            self.new_window=MyWindow3()
            self.new_window.show()
        elif traversal_type=="Inorder":
            self.new_window=MyWindow4()
            self.new_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_screen = GameScreen()
    game_screen.show()
    sys.exit(app.exec_())
