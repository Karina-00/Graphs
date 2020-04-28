from random import randint
from sys import argv


def min_rich(size):
    return size * (size - 1) // 4


def randomize_matrix(arr):
    l = len(arr)
    for i in range(min_rich(l)):
        x, y = randint(0, l - 1), randint(0, l - 1)
        arr[x][y] = 0
        arr[y][x] = 0

    return arr


class Generator:
    def __init__(self, size):
        self.matrix = [[
            *[-1 for z in range(i)],
            0,
            *[1 for z in range(size - i - 1)]
        ] for i in range(size)]

        self.matrix = randomize_matrix(self.matrix)


if __name__ == '__main__':
    try:
        times = int(argv[1])
    except:
        times = int(input("matrix size -: "))

    try:
        do_test = (argv[2] == '-test')
    except:
        do_test = False

    if do_test:
        print('2')
        print(times)
    [print("".join([f'{el: 3}' for el in row]))
     for row in Generator(times).matrix]
    if do_test:
        print('1\n2\n3\n4\n0\n0')
