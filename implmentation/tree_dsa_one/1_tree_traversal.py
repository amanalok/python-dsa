class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if type(self.data) != 'str':
            return str(self.data)

        return self.data


def inorder(root, is_last_node=False):
    if root:
        inorder(root.left)
        print('{}->'.format(root), end='')
        inorder(root.right)

    return


def preorder(root):
    if root:
        print('{}->'.format(root), end='')
        preorder(root.left)
        preorder(root.right)

    return


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print('{}->'.format(root), end='')

    return


def level_order(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while(len(queue) > 0):
        print(queue[0].data, end=' ')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return


def build_tree_one():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    return root


def build_tree_two():
    root = Node(1)
    root.left = Node(12)
    root.right = Node(9)
    root.left.left = Node(5)
    root.left.right = Node(6)

    return root


if __name__ == '__main__':
    tree_one = build_tree_one()
    print('*** Tree One ***')
    print('Inorder Traversal')
    inorder(tree_one)
    print('\nPreorder Traversal')
    preorder(tree_one)
    print('\nPostorder Traversal')
    postorder(tree_one)
    print('\nLevel Order Traversal')
    level_order(tree_one)

    tree_two = build_tree_two()
    print('\n\n*** Tree Two ***')
    print('Inorder Traversal')
    inorder(tree_two)
    print('\nPreorder Traversal')
    preorder(tree_two)
    print('\nPostorder Traversal')
    postorder(tree_two)
    print('\nLevel Order Traversal')
    level_order(tree_two)
