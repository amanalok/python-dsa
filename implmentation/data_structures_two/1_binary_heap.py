import sys

class MinHeap:

    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return (index * 2) + 1

    def get_right_child_index(self, index):
        return (index * 2) + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < size

    def get_parent(self, index):
        parent_index = self.get_parent_index(index)
        return self.storage[parent_index]

    def get_left_child(self, index):
        left_child_index = self.get_left_child_index(index)
        return self.storage[left_child_index]

    def get_right_child(self, index):
        right_child_index = self.get_right_child_index(index)
        return self.storage[right_child_index]

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def is_full(self):
        return self.capacity == self.size

    def is_empty(self):
        return self.size == 0

    def add(self, data):
        if self.is_full():
            raise Exception('Min Binary Heap is full !!!')

        self.storage[self.size] = data
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1

        while(self.has_parent(index) and
              self.get_parent(index) > self.storage[index]):

            parent_index = self.get_parent_index(index)
            self.swap(parent_index, index)
            index = parent_index

    def delete(self):
        if self.is_empty():
            raise Exception('Min Binary Heap is empty !!!')

        temp = self.storage[0]
        self.storage[0] = self.storage[self.size-1]
        self.size -= 1
        self.heapify_down()
        return temp

    def heapify_down(self):
        index = 0
        while(self.has_left_child()):
            smaller_child_index = self.get_left_child_index(index)

            if (self.has_right_child_index() and
                self.get_right_child(index) < self.storage[smaller_child_index]):

                smaller_child_index = self.get_right_child_index(index)

            if self.storage[index] < self.storage[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)
            index = smaller_child_index

    def recursive_add(self, data):
        if self.is_full():
            raise Exception('Min Binary Heap is full !!!')

        index = self.size
        self.storage[index] = data
        self.size += 1
        self.recursive_heapify_up(index)

    def recursive_heapify_up(self, index):
        if (self.has_parent(index) and
            self.get_parent(index) > self.storage[index]):

            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            self.recursive_heapify_up(parent_index)

    def recursive_delete(self):
        if self.is_empty():
            raise Exception('Min Binary Heap is empty !!!')

        index = 0
        temp = self.storage[index]
        self.storage[index] = self.storage[self.size-1]
        self.size -= 1
        self.recursive_heapify_down(index)
        return temp

    def recursive_heapify_down(self, index):
        min_value_index = index

        if (self.has_left_child(index)
            and self.get_left_child(index) < self.storage[index]):

            min_value_index = self.get_left_child_index(index)

        if (self.has_right_child(index)
            and self.right_child_index() < self.left_child_index()):

            min_value_index = self.get_right_child_index(index)

        if index != min_value_index:
            self.swap(index, min_value_index)
            self.recursive_heapify_down(min_value_index)

class MaxHeap:

    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return (index * 2) + 1

    def get_right_child_index(self, index):
        return (index * 2) + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def get_parent(self, index):
        parent_index = self.get_parent_index(index)
        return self.storage[parent_index]

    def get_left_child(self, index):
        left_child_index = self.get_left_child_index(index)
        return self.storage[left_child_index]

    def get_right_child(self, index):
        right_child_index = self.get_right_child_index(index)
        return self.storage[right_child_index]

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def add(self, data):
        if self.is_full():
            raise Exception('Max Binary Heap is full !!!')

        self.storage[self.size] = data
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while (self.has_parent(index) and
            self.get_parent(index) < self.storage[index]):

            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)

            index = parent_index

    def delete(self):
        if self.is_empty():
            raise Exception('Max Heap is empty !!!')

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return data

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            larger_child_index = self.get_left_child_index(index)

            if(self.has_right_child(index) and
             self.get_right_child(index) > self.get_left_child(index)):

             larger_child_index = self.get_right_child_index(index)

            if self.storage[index] > self.storage[larger_child_index]:
              break

            self.swap(index, larger_child_index)
            index = larger_child_index

    def recursive_add(self, data):
        if self.is_full():
            raise Exception('Max Binary Heap is full !!!')

        self.storage[self.size] = data
        self.size += 1
        self.recursive_heapify_up(self.size - 1)

    def recursive_heapify_up(self, index):
        if (self.has_parent(index) and
            self.get_parent(index) < self.storage[index]):

            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            self.recursive_heapify_up(parent_index)

    def recursive_delete(self):
        if self.is_empty():
            raise Exception('Max Binary Heap is empty !!!')

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.recursive_heapify_down(0)
        return data

    def recursive_heapify_down(self, index):
        larger_val_index = index
        if (self.has_left_child(index) and
            self.left_child_index(index) > self.storage[index]):

            larger_val_index = self.get_left_child_index(index)

        if (self.has_right_child(index) and
            self.get_right_child(index) > self.get_left_child(index)):

            larger_val_index = self.get_right_child_index(index)

        if index != larger_val_index:
            self.swap(index, larger_val_index)
            self.recursive_heapify_down(larger_val_index)

    def display(self):
        print('Following are the elements in the Max Heap: ', end='')
        print(self.storage[:self.size])


def max_val_pq_main():
    max_pq = MaxHeap(10)
    max_pq.add(20)
    max_pq.add(11)
    max_pq.add(29)
    max_pq.add(17)
    max_pq.add(81)
    max_pq.display()

    print('Dequeued elements sequence: ')
    while(max_pq.size != 0):
        print(max_pq.delete(), end=' ')

    print('\n')
    max_pq.recursive_add(12)
    max_pq.recursive_add(1)
    max_pq.recursive_add(14)
    max_pq.recursive_add(7)
    max_pq.display()

    print('Dequeued (Recursive) elements sequence: ')
    while(max_pq.size != 0):
        print(max_pq.recursive_delete(), end= ' ')

    print()


def min_val_pq_main():

    min_pq = MinHeap(10)
    min_pq.add(20)
    min_pq.add(11)
    min_pq.add(29)
    min_pq.add(17)
    min_pq.add(81)
    min_pq.display()

    print('Dequeued elements sequence: ')
    while(min_pq.size != 0):
        print(min_pq.delete(), end=' ')

    print('\n')
    min_pq.recursive_add(12)
    min_pq.recursive_add(1)
    min_pq.recursive_add(14)
    min_pq.recursive_add(7)
    min_pq.display()

    print('Dequeued (Recursive) elements sequence: ')
    while(min_pq.size != 0):
        print(min_pq.recursive_dequeue(), end=' ')

    print()


if __name__ == '__main__':

    max_val_pq_main()
