import random
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsEllipseItem,
    QGraphicsSimpleTextItem,
    QGraphicsLineItem,
    QVBoxLayout,
    QWidget,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QLabel

from abc import abstractmethod

from rbt import RBTree


class RBTreeVisualizer(QMainWindow):
    def __init__(self, order_type):
        super().__init__()
        self.setWindowTitle("Path Master")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.graphics_view = QGraphicsView()
        layout.addWidget(self.graphics_view)

        self.text_label = QLabel(f"Your Traversal Type is {order_type}!")
        self.text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text_label)

        font = QFont()
        font.setPointSize(20)  # Adjust the font size as needed
        font.setBold(True)
        self.text_label.setFont(font)

        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)

        self.rb_tree = RBTree()

        lst = []
        for i in range(17):
            a = random.randint(1, 109)
            if a not in lst:
                lst.append(a)
        self.insert_nodes(lst)

        # Array to store clicked node elements
        self.clicked_nodes = []

        self.message_label = QLabel()
        layout.addWidget(self.message_label)

    def insert_nodes(self, keys):
        for key in keys:
            self.rb_tree.insert(key)
            self.draw_tree()

    @abstractmethod
    def traversal(self):
        pass

    def draw_tree(self):
        self.scene.clear()
        self._draw_node(self.rb_tree.root, 400, 50, 200)

    def _draw_node(self, node, x, y, h_spacing):
        if node != self.rb_tree.NIL:
            radius = 20
            ellipse_item = QGraphicsEllipseItem(
                x - radius, y - radius, 2 * radius, 2 * radius
            )
            color = Qt.red if node.color == "red" else Qt.black
            ellipse_item.setBrush(color)
            # Store element in array when clicked
            ellipse_item.mousePressEvent = (
                lambda event, key=node.key: self.store_clicked_node(key)
            )
            self.scene.addItem(ellipse_item)

            text_item = QGraphicsSimpleTextItem(str(node.key))
            text_item.setPos(x - 5, y - 5)
            text_color = Qt.white if node.color == "black" else Qt.black
            text_item.setBrush(text_color)
            font = QFont()
            font.setBold(True)
            text_item.setFont(font)
            self.scene.addItem(text_item)

            if node.left != self.rb_tree.NIL:
                left_x = x - h_spacing
                left_y = y + 80
                self.scene.addItem(
                    QGraphicsLineItem(x, y + radius, left_x, left_y - radius)
                )
                self._draw_node(node.left, left_x, left_y, h_spacing / 2)

            if node.right != self.rb_tree.NIL:
                right_x = x + h_spacing
                right_y = y + 80
                self.scene.addItem(
                    QGraphicsLineItem(x, y + radius, right_x, right_y - radius)
                )
                self._draw_node(node.right, right_x, right_y, h_spacing / 2)

    def store_clicked_node(self, key):
        lst = self.traversal()
        self.clicked_nodes.append(key)
        ind = len(self.clicked_nodes) - 1
        path = "C:\\Users\\User\\Desktop\\Code Crimson Final Project - Erum Naushad and Aliza Fatima\\Code Crimson Final Project - Erum Naushad and Aliza Fatima (1)\\FInal Project With Suggested Changes\\final-project\\voice.wav"
        if len(self.clicked_nodes) == len(lst):
            print(lst)
            print(self.clicked_nodes)
            print("I have to say, you are a genius!")
            QMessageBox.information(self, "Notification", "I have to say, you are a genius!")
            QApplication.instance().activeWindow().close()
        elif len(self.clicked_nodes) < len(lst):
            if self.clicked_nodes[ind] == lst[ind]:
                QSound.play(path)
                print(lst)
                print(self.clicked_nodes)
                print("continue")
                self.message_label.setText("Keep going, you're on the right path! (pun intended)")
            elif self.clicked_nodes[ind] != lst[ind]:
                print(lst)
                print(self.clicked_nodes)
                print("no")
                self.clicked_nodes = []
                self.message_label.setText("Oops! You're gonna have to restart!")
