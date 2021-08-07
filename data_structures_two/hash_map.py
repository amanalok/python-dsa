import numpy as np


class HashMapSeperateChaining:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage_map = [None] * self.capacity

    def _get_hash(self, key):
        ''' hash = 0
        for char in key:
            hash += ord(char) '''

        hash_val = hash(key)
        return hash_val % self.capacity

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.storage_map[key_hash] is None:
            self.storage_map[key_hash] = [key_value]
            return

        for key_val_pair in self.storage_map[key_hash]:
            if key == key_val_pair[0]:
                key_val_pair[1] = value
                return

        self.storage_map[key_hash].append(key_value)

    def get(self, key):
        key_hash = self._get_hash(key)

        if self.storage_map[key_hash] is None:
            raise Exception('Key not found in the hashmap !!!')

        for key_val_pair in self.storage_map[key_hash]:
            if key == key_val_pair[0]:
                return key_val_pair[1]

        raise Exception('Key not found in hashmap !!!')

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.storage_map[key_hash] is None:
            raise Exception('Key not found in hashmap !!!')

        for i in range(0, len(self.storage_map[key_hash])):
            if key == self.storage_map[key_hash][i][0]:
                self.storage_map[key_hash].pop(i)
                return

        raise Exception('Key not found in hashmap !!!')

    def print(self):
        print('*** Following are the hash map entries ***')
        for item in self.storage_map:
            if item is not None:
                print(str(item))

    def keys(self):
            arr = []
            for i in range(0, len(self.storage_map)):
                    if self.storage_map[i]:
                        for key_val_pair in self.storage_map[i]:
                            arr.append(key_val_pair[0])
            return arr



class HashMapLinearProbing:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage_map = [None] * self.capacity

    def _get_hash_version_1(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)

        return hash_val % self.capacity

    def _get_hash_version_2(self, key):
        hash_val = hash(key)
        return hash_val % self.capacity

    def _get_hash_version_3(self, key):
        hash_val = 0
        for idx, char in enumerate(key):
            hash_val += (idx + len(key)) ** ord(char)
            hash_val = hash_val % self.capacity

        return hash_val

    def add(self, input_key, value):
        index = self._get_hash_version_1(input_key)

        counter = 0
        while(self.storage_map[index] is not None):
            entry = self.storage_map[index]
            if entry[0] == input_key:
                break

            index = (index + 1) % self.capacity

            counter += 1
            if counter == self.capacity:
                break

        if counter != self.capacity:
            self.storage_map[index] = (input_key, value)
            return

        counter = 0
        while(self.storage_map[index][0] != np.inf):
            index = (index + 1) % self.capacity

            counter += 1
            if counter == self.capacity:
                break

        if counter != self.capacity:
            self.storage_map[index] = (input_key, value)
            return

        raise Exception('Hashmap if full !!!')

    def get(self, input_key):
        index = self._get_hash_version_1(input_key)

        counter = 0
        while(self.storage_map[index] is not None):
            key, value = self.storage_map[index]
            if key == input_key:
                return value

            index = (index + 1) % self.capacity

            counter += 1
            if counter == self.capacity:
                raise Exception('Key {} not found'.format(input_key))

        raise Exception('Key {} not found'.format(input_key))

    def delete(self, input_key):
        index = self._get_hash_version_1(input_key)

        counter = 0
        while(self.storage_map[index] is not None):
            key, value = self.storage_map[index]
            if key == input_key:
                self.storage_map[index] = (np.inf, np.inf)
                return

            coutner += 1
            if countter == self.capacity:
                raise Exception('Key {} not found in hashmap'.format(input_key))

        raise Exception('Key {} not found in hashmap'.format(input_key))

    def print(self):
        for entry in self.storage_map:
            if entry is not None:
                key, val = entry
                if key != np.inf:
                    print(entry)

    def keys(self):
        arr = []
        print(self.storage_map)
        for entry in self.storage_map:
            if entry is not None:
                key, val = entry
                if key != np.inf:
                    arr.append(key)

        return arr



def hashmap_with_linear_probing():
    h = HashMapLinearProbing(6)
    h.add('Bob', '567-8888')
    h.add('Ming', '293-6753')
    h.add('Ming', '333-8233')
    h.add('Ankit', '293-8625')
    h.add('Aditya', '852-6551')
    h.add('Alicia', '632-4123')
    print('*** Printing entries of the hashmap ***')
    h.print()
    h.add('Mike', '567-2188')
    h.add('Aditya', '777-8888')
    print('*** Printing entries of the hashmap ***')
    h.print()
    h.delete('Bob')
    print('*** Printing entries of the hashmap ***')
    h.print()
    print('Ming: ' + h.get('Ming'))
    print(h.keys())
    h.add('Ming', '367-8490')
    print('*** Printing entries of the hashmap ***')
    h.print()
    h.add('Aman', '716-7921')
    print('*** Printing entries of the hashmap ***')
    h.print()
    print('Aman: ' + h.get('Aman'))


def hashmap_with_seperate_chaining():
    h = HashMapSeperateChaining(6)
    h.add('Bob', '567-8888')
    h.add('Ming', '293-6753')
    h.add('Ming', '333-8233')
    h.add('Ankit', '293-8625')
    h.add('Aditya', '852-6551')
    h.add('Alicia', '632-4123')
    h.add('Mike', '567-2188')
    h.add('Aditya', '777-8888')
    h.print()
    h.delete('Bob')
    h.print()
    print('Ming: ' + h.get('Ming'))
    print(h.keys())


if __name__ == '__main__':
    hashmap_with_linear_probing()
