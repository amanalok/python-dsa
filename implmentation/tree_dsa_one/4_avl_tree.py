import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

    def __repr__(self):
        if type(self.data) != 'str':
            return str(self.data)

        return self.data


def _get_height(root):
    if root is None:
        return 0

    return root.height


def _get_balance(root):
    if root is None:
        return 0

    return _get_height(root.left) - _get_height(root.right)


def _rotate_right(z):
    y = z.left
    t3 = y.right

    # Perform rotation
    y.right = z
    z.left = t3

    # Update heights
    z.height = 1 + max(_get_height(z.left), _get_height(z.right))
    y.height = 1 + max(_get_height(y.left), _get_height(y.right))

    # Return the new root
    return y


def _rotate_left(z):
    y = z.right
    t2 = y.left

    # Perform rotation
    y.left = z
    z.right = t2

    # Update heights
    z.height = 1 + max(_get_height(z.left), _get_height(z.right))
    y.height = 1 + max(_get_height(y.left), _get_height(y.right))

    # Return the new root
    return y



def insert_node(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)

    root.height = 1 + max(_get_height(root.left), _get_height(root.right))
    balance = _get_balance(root)

    # Left-left case
    if balance > 1 and data < root.left.data:
        return _rotate_right(root)

    # Left-right case
    if balance > 1 and data > root.left.data:
        root.left = _rotate_left(root.left)
        return _rotate_right(root)

    # Right-right case
    if balance < -1 and data > root.right.data:
        return _rotate_left(root)

    # Right-left case
    if balance < -1 and data < root.right.data:
        root.right = _rotate_right(root.right)
        return _rotate_left(root)

    return root


def _get_min_value(root):

    while(root.left is not None):
        root = root.left

    return root


def delete_node(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete_node(root.left, data)
    elif data > root.data:
        root.right = delete_node(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = _get_min_value(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)

    root.height = 1 + max(_get_height(root.left), _get_height(root.right))
    balance = _get_balance(root)

    # Left left case
    if balance > 1 and _get_balance(root.left) >= 0:
        return _rotate_right(root)

    # Left right case
    if balance > 1 and _get_balance(root.left) < 0:
        root.left = _rotate_left(root.left)
        return _rotate_right(root)

    # Right right case
    if balance < -1 and _get_balance(root.right) <= 0:
        return _rotate_left(root)

    # Right left case
    if balance < -1 and _get_balance(root.right) > 0:
        root.right = _rotate_right(root.right)
        return _rotate_left(root)

    return root


def preorder(root):
    if root:
        print('{}'.format(root), end=' ')
        preorder(root.left)
        preorder(root.right)


def printHelper(currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.data)
            printHelper(currPtr.left, indent, False)
            printHelper(currPtr.right, indent, True)


def build_tree_one():
    root = None
    for item in [10, 20, 30, 40, 50, 25]:
        root = insert_node(root, item)

    return root


def build_tree_two():
    root = None
    for item in [9, 5, 10, 0, 6, 11, -1, 1, 2]:
        root = insert_node(root, item)

    return root


if __name__ == '__main__':
    tree_one = build_tree_one()
    print('Tree One: ', end='')
    preorder(tree_one)

    print('\nTree Two: ', end='')
    tree_two = build_tree_two()
    preorder(tree_two)

    print('\nDeleting 10 from Tree Two')
    tree_two = delete_node(tree_two, 10)
    print('Tree Two: ', end='')
    preorder(tree_two)
    print('\nDeleting -1 from Tree Two')
    tree_two = delete_node(tree_two, -1)
    print('Tree Two: ', end='')
    preorder(tree_two)

    print()
    printHelper(tree_two, '', True)
