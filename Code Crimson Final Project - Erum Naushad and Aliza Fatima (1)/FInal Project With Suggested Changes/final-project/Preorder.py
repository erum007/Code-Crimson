import sys
from PyQt5.QtWidgets import QApplication

from RBTreeVisualizer import RBTreeVisualizer


class RBTreeVisualizerPreorder(RBTreeVisualizer):
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.rb_tree.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node != self.rb_tree.NIL:
            result.append(node.key)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def traversal(self):
        return self.preorder_traversal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rb_tree_visualizer = RBTreeVisualizerPreorder("Preorder")
    rb_tree_visualizer.show()
    sys.exit(app.exec_())
