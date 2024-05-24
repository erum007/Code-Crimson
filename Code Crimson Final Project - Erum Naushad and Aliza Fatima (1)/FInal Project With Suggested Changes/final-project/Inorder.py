import sys
from PyQt5.QtWidgets import QApplication

from RBTreeVisualizer import RBTreeVisualizer


class RBTreeVisualizerInorder(RBTreeVisualizer):
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.rb_tree.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node != self.rb_tree.NIL:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def traversal(self):
        return self.inorder_traversal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rb_tree_visualizer = RBTreeVisualizerInorder("Inorder")
    rb_tree_visualizer.show()
    sys.exit(app.exec_())

