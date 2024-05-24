import sys
from PyQt5.QtWidgets import QApplication

from RBTreeVisualizer import RBTreeVisualizer


class RBTreeVisualizerPostorder(RBTreeVisualizer):
    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.rb_tree.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node != self.rb_tree.NIL:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.key)

    def traversal(self):
        return self.postorder_traversal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    rb_tree_visualizer = RBTreeVisualizerPostorder("Postorder")
    rb_tree_visualizer.show()
    sys.exit(app.exec_())
