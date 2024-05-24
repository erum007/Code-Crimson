import pytest

from rbt import RBTree


@pytest.fixture
def filled_tree():
    rbt = RBTree()
    rbt.insert(10)
    rbt.insert(5)
    rbt.insert(15)
    rbt.insert(3)
    rbt.insert(7)
    rbt.insert(12)
    rbt.insert(18)
    return rbt


def test_insertion(filled_tree):
    assert filled_tree.search(10)
    assert filled_tree.search(5)
    assert filled_tree.search(15)
    assert filled_tree.search(3)
    assert filled_tree.search(7)
    assert filled_tree.search(12)
    assert filled_tree.search(18)

    assert not filled_tree.search(19)
    assert not filled_tree.search(4)
    assert not filled_tree.search(9)
    assert not filled_tree.search(17)


def test_deletion(filled_tree):
    filled_tree.delete(10)
    assert not filled_tree.search(10)
    filled_tree.delete(5)
    assert not filled_tree.search(5)
    filled_tree.delete(15)
    assert not filled_tree.search(15)
    filled_tree.delete(3)
    assert not filled_tree.search(3)
    filled_tree.delete(7)
    assert not filled_tree.search(7)
    filled_tree.delete(12)
    assert not filled_tree.search(12)
    filled_tree.delete(18)
    assert not filled_tree.search(18)


def test_search(filled_tree):
    assert filled_tree.search(10)
    assert filled_tree.search(5)
    assert filled_tree.search(15)
    assert filled_tree.search(3)
    assert filled_tree.search(7)
    assert filled_tree.search(12)
    assert filled_tree.search(18)

    assert not filled_tree.search(11)
    assert not filled_tree.search(14)
    assert not filled_tree.search(20)
    assert not filled_tree.search(102)


if __name__ == "__main__":
    pytest.main()
