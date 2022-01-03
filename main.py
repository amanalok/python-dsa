import importlib
l = importlib.import_module('data_structures_two.2_linked_list')
LinkedList = getattr(l, 'LinkedList')

import heapq as hq

class employee:

  # constructor
    def __init__(self, n, d, yos, s):
        self.name = n
        self.des = d
        self.yos = yos
        self.sal = s

  # function for customized printing
    def print_me(self):
        print("Name :", self.name)
        print("Designation :", self.des)
        print("Years of service :", str(self.yos))
        print("salary :", str(self.sal))

    def __lt__(self, other):
        return self.sal < other.sal


if __name__ == '__main__':
    e1 = employee('Anish', 'manager', 3, 24000)
    e2 = employee('kathy', 'programmer', 2, 15000)
    e3 = employee('Rina', 'Analyst', 5, 30000)
    e4 = employee('Vinay', 'programmer', 1, 10000)

    # list of employee objects
    emp = [e1, e2, e3, e4]

    hq.heapify(emp)

    for e in emp:
        e.print_me()

    while(emp):
        e = hq.heappop(emp)
        e.print_me()
