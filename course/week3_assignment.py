from math import pow

def remdup(l):
    ind_to_remove = []
    size = len(l)
    i = 0
    for i in range(size):
        j = i + 1
        while j < size:
            if l[i] == l[j]:
                ind_to_remove.append(l[i])
            j = j + 1
        i = i + 1

    for item in ind_to_remove:
        l.remove(item)
                
    return l


def splitsum(l):
    pos_total = 0
    neg_total = 0
    for item in l:
        if item >= 0:
            pos_total += item ** 2
        else:
            neg_total += item ** 3

    return [pos_total, neg_total]


def matrixflip(m,d):
    matrix = [row[:] for row in m]
    if d == 'h':
        for i in range(len(m)):
            matrix[i][0], matrix[i][1] = matrix[i][1], matrix[i][0]
        return matrix
    elif d == 'v':
        for i in range(len(m)):
            matrix[0][i], matrix[1][i] = matrix[1][i], matrix[0][i]
        return matrix
    else:
        return matrix

                


if __name__ == '__main__':
    print(remdup([3,1,3,5]))
    print(remdup([7,3,-1,-5]))
    print(remdup([3,5,7,5,3,7,10]))

    print(splitsum([1,3,-5]))
    print(splitsum([2,4,6]))
    print(splitsum([-19,-7,-6,0]))
    print(splitsum([-1,2,3,-7]))

    print(matrixflip([[1,2],[3,4]],'h'))
    print(matrixflip([[1,2],[3,4]],'v'))
    print(matrixflip([[1, 2], [3, 4]],'h'))

    print(matrixflip([[1, 2], [3, 4]],'h'))