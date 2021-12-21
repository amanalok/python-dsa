import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if type(self.data) != 'str':
            return str(self.data)

        return self.data


def insert_node(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)

    return root


def search_node(root, data):
    if root is None or root.data == data:
        return root

    if data < root.data:
        return search_node(root.left, data)

    return search_node(root.right, data)


def _min_value_node(root):
    temp = root
    while (temp.left is not None):
        temp = temp.left

    return temp


def delete_node_recursive(root, target_node_data):
    if root is None:
        return root

    if target_node_data < root.data:
        root.left = delete_node_recursive(root.left, target_node_data)
    elif target_node_data > root.data:
        root.right = delete_node_recursive(root.right, target_node_data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = _min_value_node(root.right)
        root.data = temp.data
        root.right = delete_node_recursive(root.right, temp.data)

    return root


def is_bst(root):
    return is_bst_util(root, -sys.maxsize, sys.maxsize)


def is_bst_util(root, min, max):
    if root is None:
        return True

    if root.data < min or root.data > max:
        return False

    return (is_bst_util(root.left, min, root.data) and
            is_bst_util(root.right, root.data, max))


def inorder(root):
    if root:
        inorder(root.left)
        print(root, end=' ')
        inorder(root.right)


def build_tree_one():
    root = Node(1)
    root.right = Node(3)
    root.left = Node(2)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)
    root.left.right.right = Node(7)

    return root


def build_tree_two():
    all_data = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for data in all_data:
        root = insert_node(root, data)

    return root


if __name__ == '__main__':
    tree_one = build_tree_one()
    if is_bst(tree_one):
        print('Tree One is binary search tree')
    else:
        print('Tree One is not binary search tree')

    tree_two = build_tree_two()
    if is_bst(tree_two):
        print('Tree Two is binary search tree')
    else:
        print('Tree Two is not binary search tree')

    print('Tree Two: ', end='')
    inorder(tree_two)
    print('\nDeleting 15 from Tree Two')
    print('Tree Two: ', end='')
    tree_two = delete_node_recursive(tree_two, 15)
    inorder(tree_two)
    print('\nDeleting 8 from Tree Two')
    print('Tree Two: ', end='')
    tree_two = delete_node_recursive(tree_two, 8)
    inorder(tree_two)
    print('\nDeleting 25 from Tree Two')
    print('Tree Two: ', end='')
    tree_two = delete_node_recursive(tree_two, 25)
    inorder(tree_two)
    print()
    print(search_node(tree_two, 10))
    print(search_node(tree_two, 45))
