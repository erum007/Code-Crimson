import random
import sys
import ast

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsLineItem,
    QGraphicsScene,
    QGraphicsSimpleTextItem,
    QGraphicsView,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
)
from PyQt5.QtGui import QPixmap
from rbt import RBTree


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

        self.setWindowTitle("Image Display")
        self.show()


class RBTreeVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_window = None
        self.setWindowTitle("Red-Black Tree Visualizer")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.graphics_view = QGraphicsView()
        layout.addWidget(self.graphics_view)

        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)

        self.rb_tree = RBTree()

        global file_name
        global b
        a = str(random.randint(1, 5))
        b = a
        file_name = f"C:\\Users\\User\\Desktop\\Code Crimson Final Project - Erum Naushad and Aliza Fatima\\Code Crimson Final Project - Erum Naushad and Aliza Fatima (1)\\FInal Project With Suggested Changes\\final-project\\Quiz{b}.txt"
        with open(file_name) as f:
            s = f.readline()
            lst = ast.literal_eval(s)
        self.insert_nodes(lst)

        # Add quiz buttons
        self.quiz_button1 = QPushButton("Question 1")
        self.quiz_button1.clicked.connect(self.show_quiz1)
        layout.addWidget(self.quiz_button1)
        self.quiz_button2 = QPushButton("Question 2")
        self.quiz_button2.clicked.connect(self.show_quiz2)
        layout.addWidget(self.quiz_button2)
        self.quiz_button3 = QPushButton("Question 3")
        self.quiz_button3.clicked.connect(self.show_quiz3)
        layout.addWidget(self.quiz_button3)
        self.quiz_button4 = QPushButton("Question 4")
        self.quiz_button4.clicked.connect(self.show_quiz4)
        layout.addWidget(self.quiz_button4)
        self.quiz_button5 = QPushButton("Question 5")
        self.quiz_button5.clicked.connect(self.show_quiz5)
        layout.addWidget(self.quiz_button5)

        # Add score label
        self.score_label = QLabel()
        layout.addWidget(self.score_label, alignment=Qt.AlignRight)
        self.score_label.setText("Score: 0")

        # Initialize score counter
        self.score = 0

    def insert_nodes(self, keys):
        for key in keys:
            self.rb_tree.insert(key)
            self.draw_tree()

    def draw_tree(self):
        self.scene.clear()
        self._draw_node(self.rb_tree.root, 400, 50, 200)

    def _draw_node(self, node, x, y, h_spacing):
        if node != self.rb_tree.NIL:
            ellipse_item = QGraphicsEllipseItem(x - 15, y - 15, 30, 30)
            color = Qt.red if node.color == "red" else Qt.black
            ellipse_item.setBrush(color)
            self.scene.addItem(ellipse_item)

            text_item = QGraphicsSimpleTextItem(str(node.key))
            text_item.setPos(x - 5, y - 5)
            text_color = Qt.white if node.color == "black" else Qt.black
            text_item.setBrush(text_color)
            self.scene.addItem(text_item)

            if node.left != self.rb_tree.NIL:
                left_x = x - h_spacing
                left_y = y + 80
                self.scene.addItem(QGraphicsLineItem(x, y, left_x, left_y))
                self._draw_node(node.left, left_x, left_y, h_spacing / 2)

            if node.right != self.rb_tree.NIL:
                right_x = x + h_spacing
                right_y = y + 80
                self.scene.addItem(QGraphicsLineItem(x, y, right_x, right_y))
                self._draw_node(node.right, right_x, right_y, h_spacing / 2)

    def show_quiz1(self):
        with open(file_name) as f:
            s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].strip()
        question1 = s[1]
        answer1 = s[5]
        color = self._get_expected_color()
        message = question1
        reply = QMessageBox.question(
            self, "Quiz", message, QMessageBox.Yes | QMessageBox.No
        )
        if answer1 == "Yes" and reply == QMessageBox.Yes:
            user_answer = "black"
        elif answer1 == "No" and reply == QMessageBox.No:
            user_answer = "black"
        else:
            user_answer = "red"
        if user_answer == color:
            image_path = f"C:\\Users\\User\\Desktop\\Code Crimson Final Project - Erum Naushad and Aliza Fatima\\Code Crimson Final Project - Erum Naushad and Aliza Fatima (1)\\FInal Project With Suggested Changes\\final-project\\Answer-Images\\{b}_1.png"
            self.image_window = ImageWindow(image_path)
            self.image_window.show()
            self.score += 1
            self.quiz_button1.setEnabled(False)
        else:
            QMessageBox.warning(self, "Quiz Result", "Oops! That was wrong.")
            self.quiz_button1.setEnabled(False)
        self.update_score()

    def show_quiz2(self):
        with open(file_name) as f:
            s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].strip()
        question2 = s[2]
        answer2 = s[6]
        color = self._get_expected_color()
        message = question2
        reply = QMessageBox.question(
            self, "Quiz", message, QMessageBox.Yes | QMessageBox.No
        )
        if answer2 == "Yes" and reply == QMessageBox.Yes:
            user_answer = "black"
        elif answer2 == "No" and reply == QMessageBox.No:
            user_answer = "black"
        else:
            user_answer = "red"
        if user_answer == color:
            image_path = f"C:\\Users\\User\\Desktop\\Code Crimson Final Project - Erum Naushad and Aliza Fatima\\Code Crimson Final Project - Erum Naushad and Aliza Fatima (1)\\FInal Project With Suggested Changes\\final-project\\Answer-Images\\{b}_2.png"
            self.image_window = ImageWindow(image_path)
            self.image_window.show()
            self.score += 1
            self.quiz_button2.setEnabled(False)
        else:
            QMessageBox.warning(self, "Quiz Result", "Oops! That was wrong.")
            self.quiz_button2.setEnabled(False)
        self.update_score()

    def show_quiz3(self):
        with open(file_name) as f:
            s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].strip()
        question3 = s[3]
        answer3 = s[7]
        color = self._get_expected_color()
        message = question3
        reply = QMessageBox.question(
            self, "Quiz", message, QMessageBox.Yes | QMessageBox.No
        )
        if answer3 == "Yes" and reply == QMessageBox.Yes:
            user_answer = "black"
        elif answer3 == "No" and reply == QMessageBox.No:
            user_answer = "black"
        else:
            user_answer = "red"
        if user_answer == color:
            image_path = f"C:\\Users\\User\\Desktop\\Code Crimson Final Project - Erum Naushad and Aliza Fatima\\Code Crimson Final Project - Erum Naushad and Aliza Fatima (1)\\FInal Project With Suggested Changes\\final-project\\Answer-Images\\{b}_3.png"
            self.image_window = ImageWindow(image_path)
            self.image_window.show()
            self.score += 1
            self.quiz_button3.setEnabled(False)
        else:
            QMessageBox.warning(self, "Quiz Result", "Oops! That was wrong.")
            self.quiz_button3.setEnabled(False)
        self.update_score()

    def show_quiz4(self):
        with open(file_name) as f:
            s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].strip()
        question4 = s[4]
        answer4 = s[8]
        color = self._get_expected_color()
        message = question4
        reply = QMessageBox.question(
            self, "Quiz", message, QMessageBox.Yes | QMessageBox.No
        )
        if answer4 == "Yes" and reply == QMessageBox.Yes:
            user_answer = "black"
        elif answer4 == "No" and reply == QMessageBox.No:
            user_answer = "black"
        else:
            user_answer = "red"
        if user_answer == color:
            image_path = f"C:\\Users\\User\\Desktop\\Code Crimson Final Project - Erum Naushad and Aliza Fatima\\Code Crimson Final Project - Erum Naushad and Aliza Fatima (1)\\FInal Project With Suggested Changes\\final-project\\Answer-Images\\{b}_4.png"
            self.image_window = ImageWindow(image_path)
            self.image_window.show()
            self.score += 1
            self.quiz_button4.setEnabled(False)
        else:
            QMessageBox.warning(self, "Quiz Result", "Oops! That was wrong.")
            self.quiz_button4.setEnabled(False)
        self.update_score()

    def show_quiz5(self):
        val = self.rb_tree.get_root()
        val_key = val.get_key()
        successor = self.rb_tree._successor(val)
        successor_key = successor.get_key()
        wrong = val.right if successor == val.left else val.left
        wrong_key = wrong.get_key()
        message = f"What is the successor of {val_key}? (Yes for {successor_key}, No for {wrong_key})"
        reply = QMessageBox.question(
            self, "Quiz", message, QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            user_answer = successor_key
        else:
            user_answer = wrong_key

        if user_answer == successor_key:
            QMessageBox.information(
                self, "Quiz Result", "Congratulations! You got it right."
            )
            self.score += 1
            self.quiz_button5.setEnabled(False)
        else:
            QMessageBox.warning(
                self, "Quiz Result", f"No, that's wrong! The answer is {successor_key}."
            )
            self.quiz_button5.setEnabled(False)
        self.update_score()

    def _get_expected_color(self):
        return "black"

    def update_score(self):
        self.score_label.setText(f"Score: {self.score}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rb_tree_visualizer = RBTreeVisualizer()
    rb_tree_visualizer.show()
    sys.exit(app.exec_())
