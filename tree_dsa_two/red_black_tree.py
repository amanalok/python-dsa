import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.parent  = None
        self.left = None
        self.right = None
        # 1 refers to color 'RED' and 0 refers to color 'BLACK'
        self.color = 1


class RedBlackTree:
    # 1 refers to color 'RED' and 0 refers to color 'BLACK'
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = 0
        self.root = self.NIL


    def _left_rotate(self, x):
        y = x.right
        t = y.left
        x.right = t
        if t != self.NIL:
            t.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y


    def _right_rotate(self, x):
        y = x.left
        t = y.right
        x.left = t
        if t != self.NIL:
            t.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y



    def _fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._left_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = 0


    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        y = None
        x = self.root

        while x != self.NIL:
            y = x

            if data < x.data:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == None:
            self.root = new_node
        elif data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent == None:
            new_node.color = 0
            return

        if new_node.parent.parent == None:
            return

        self._fix_insert(new_node)


    def _minimum(self, v):
        while v.left != self.NIL:
            v = v.left

        return v


    def _transplant(self, v, u):
        if v.parent == None:
            self.root = u
        elif v == v.parent.left:
            v.parent.left = u
        else:
            v.parent.right = u

        if u != self.NIL:
            u.parent = v.parent


    def _fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self._right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self._left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root

        x.color = 0


    def delete(self, data):
        z = self.root
        while z != self.NIL:
            if z.data == data:
                break
            elif data < z.data:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            raise Exception('Node with data {} not found in tree'.format(data))

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, x)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, x)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right

            if y.parent != z:
                self._transplant(y, x)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self._fix_delete(x)


    def _preorder_helper(self, z):
        if z == self.NIL:
            return

        if z.color == 0:
            print('{}(B)'.format(z.data), end=' ')
        else:
            print('{}(R)'.format(z.data), end=' ')

        self._preorder_helper(z.left)
        self._preorder_helper(z.right)


    def preorder(self):
        self._preorder_helper(self.root)



def build_tree_one():
    rb_tree = RedBlackTree()
    for data in [55, 40, 65, 60, 75, 57]:
        rb_tree.insert(data)

    return rb_tree



def build_tree_two():
    rb_tree = RedBlackTree()
    for data in [15, 5, 1, 12, 19, 9, 13, 23, 10, 9]:
        rb_tree.insert(data)

    return rb_tree



def build_tree_three():
    rb_tree = RedBlackTree()
    for data in [13, 8, 17, 1, 11, 6, 15, 25, 22, 27]:
        rb_tree.insert(data)

    return rb_tree



if __name__ == '__main__':
    rb_tree_1 = build_tree_one()
    print('Red Black Tree One: ')
    rb_tree_1.preorder()

    rb_tree_2 = build_tree_two()
    print('\n\nRed Black Tree Two:')
    rb_tree_2.preorder()

    rb_tree_3 = build_tree_three()
    print('\n\nRed Black Tree Three:')
    rb_tree_3.preorder()

    print('\nDeleting 6 from RBT 3')
    temp = copy.deepcopy(rb_tree_3)
    temp.delete(6)
    temp.preorder()

    print('\nDeleting 1 from RBT 3')
    temp = copy.deepcopy(rb_tree_3)
    temp.delete(1)
    temp.preorder()

    print('\nDeleting 17 from RBT 3')
    temp = copy.deepcopy(rb_tree_3)
    temp.delete(17)
    temp.preorder()

    print('\nDeleting 25 from RBT 3')
    temp = copy.deepcopy(rb_tree_3)
    temp.delete(25)
    temp.preorder()
