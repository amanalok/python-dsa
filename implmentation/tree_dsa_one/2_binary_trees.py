class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if type(self.data) != 'str':
            return str(self.data)

        return self.data


def _height(root):
    if root is None:
        return 0

    return max(_height(root.left), _height(root.right)) + 1


def is_balanced_binary_tree(root):
    '''
    Binary tree where difference between the left and the right
    subtree for any node is not more than one
    '''
    if root is None:
        return True

    lh = _height(root.left)
    rh = _height(root.right)

    if ((abs(lh - rh) <= 1) and
        is_balanced_binary_tree(root.left) and
        is_balanced_binary_tree(root.right)):

        return True

    return False


def _count_nodes(root):
    if root is None:
        return 0

    return (1 + _count_nodes(root.left) + _count_nodes(root.right))


def is_complete_binary_tree(root, index, number_of_nodes):
    '''
    Binary tree in which all levels are filled except possibly the
    lowest level which is filled from left to right
    '''
    if root is None:
        return True

    if index >= number_of_nodes:
        return False

    return (is_complete_binary_tree(root.left, 2*index+1, number_of_nodes) and
            is_complete_binary_tree(root.right, 2*index+2, number_of_nodes))


def _calculate_left_depth(root):
    left_depth = 0
    while(root is not None):
        left_depth += 1
        root = root.left

    return left_depth


def is_perfect_binary_tree(root, left_depth, level=0):
    '''
    Binary tree in which every internal node has exactly 2 child nodes and
    and all leaf nodes are at the same level is a perfect binary tree
    '''
    if root is None:
        return True

    if (root.left is None and root.right is None):
        return (left_depth == level + 1)

    if (root.left is None or root.right is None):
        return False

    return (is_perfect_binary_tree(root.left, left_depth, level+1) and
            is_perfect_binary_tree(root.right, left_depth, level+1))



def is_full_binary_tree(root):
    '''
    Binary tree with parent node and all internal nodes having either 2
    children nodes or no children nodes are called full binary tree.
    '''
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)

    return False


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
    root = Node(1)
    root.left = Node(12)
    root.right = Node(9)
    root.left.left = Node(5)
    root.left.right = Node(6)

    return root


def build_tree_three():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(13)
    root.right.right = Node(9)

    return root


if __name__ == '__main__':
    tree_one = build_tree_one()
    if is_full_binary_tree(tree_one):
        print('Tree One is full binary tree')
    else:
        print('Tree One is not full binary tree')

    if is_perfect_binary_tree(tree_one, _calculate_left_depth(tree_one)):
        print('Tree One is perfect binary tree')
    else:
        print('Tree One is not perfect binary tree')

    if is_complete_binary_tree(tree_one, 0, _count_nodes(tree_one)):
        print('Tree One is a complete binary tree')
    else:
        print('Tree One is not a complete binary tree')

    if is_balanced_binary_tree(tree_one):
        print('Tree One is balanced binary tree')
    else:
        print('Tree One is not a balanced binary tree')


    tree_two = build_tree_two()
    if is_full_binary_tree(tree_two):
        print('\nTree Two is full binary tree')
    else:
        print('\nTree Two is not full binary tree')

    if is_perfect_binary_tree(tree_two, _calculate_left_depth(tree_two)):
        print('Tree Two is perfect binary tree')
    else:
        print('Tree Two is not perfect binary tree')

    if is_complete_binary_tree(tree_two, 0, _count_nodes(tree_two)):
        print('Tree Two is a complete binary tree')
    else:
        print('Tree Two is not a complete binary tree')

    if is_balanced_binary_tree(tree_two):
        print('Tree Two is balanced binary tree')
    else:
        print('Tree Two is not a balanced binary tree')

    tree_three = build_tree_three()
    if is_full_binary_tree(tree_three):
        print('\nTree Three is full binary tree')
    else:
        print('\nTree Three is not full binary tree')

    if is_perfect_binary_tree(tree_three, _calculate_left_depth(tree_three)):
        print('Tree Three is perfect binary tree')
    else:
        print('Tree Three is not perfect binary tree')

    if is_complete_binary_tree(tree_three, 0, _count_nodes(tree_three)):
        print('Tree Three is a complete binary tree')
    else:
        print('Tree Three is not a complete binary tree')

    if is_balanced_binary_tree(tree_three):
        print('Tree Three is balanced binary tree')
    else:
        print('Tree Three is not a balanced binary tree')
