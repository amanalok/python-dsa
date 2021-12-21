class MinPriorityQueue:

    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2*index + 1

    def get_right_child_index(self, index):
        return 2*index + 2

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

    def enqueue(self, data):
        if self.is_full():
            raise Exception('Min PQ is full')

        self.storage[self.size] = data
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while(self.has_parent(index) and
              self.get_parent(index) > self.storage[index]):

              parent_index = self.get_parent_index(index)
              self.swap(index, parent_index)
              index = parent_index

    def dequeue(self):
        if self.is_empty():
            raise Exception('Min PQ is empty')

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return data

    def heapify_down(self):
        index = 0
        while(self.has_left_child(index)):
            smaller_child_index = self.get_left_child_index(index)

            if(self.has_right_child(index) and
               self.get_right_child(index) < self.get_left_child(index)):

                smaller_child_index = self.get_right_child_index(index)

            if self.storage[index] < self.storage[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)
            index = smaller_child_index

    def recursive_enqueue(self, data):
        if self.is_full():
            raise Exception('Min PQ is full')

        self.storage[self.size - 1] = data
        self.size += 1
        self.recursive_heapify_up(self.size - 1)

    def recursive_heapify_up(self, index):
        if not self.has_parent(index):
            return

        if self.storage[index] < self.get_parent(index):
            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            self.recursive_enqueue(parent_index)

        return

    def recursive_dequeue(self):
        if self.is_empty():
            raise Exception('Min PQ is empty')

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.recursive_heapify_down(0)
        return data

    def recursive_heapify_down(self, index):
        min_value_index = index

        if self.has_left_child(index):
            min_value_index = self.get_left_child_index(index)

        if (self.has_right_child(index) and
            self.get_right_child(index) < self.get_left_child(index)):

            min_value_index = self.get_right_child_index(index)

        if index != min_value_index:
            self.swap(index, min_value_index)
            self.recursive_heapify_down(min_value_index)

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def display(self):
        print(self.storage[:self.size])


def min_val_pq_main():

    min_pq = MinPriorityQueue(10)
    min_pq.enqueue(20)
    min_pq.enqueue(11)
    min_pq.enqueue(29)
    min_pq.enqueue(17)
    min_pq.enqueue(81)
    min_pq.display()

    print('Dequeued elements sequence: ')
    while(min_pq.size != 0):
        print(min_pq.dequeue(), end=' ')

    print('\n')
    min_pq.recursive_enqueue(12)
    min_pq.recursive_enqueue(1)
    min_pq.recursive_enqueue(14)
    min_pq.recursive_enqueue(7)
    min_pq.display()

    print('Dequeued (Recursive) elements sequence: ')
    while(min_pq.size != 0):
        print(min_pq.recursive_dequeue(), end=' ')

    print()


if __name__ == '__main__':

    min_val_pq_main()
