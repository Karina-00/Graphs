from time import time

from mejn import *
from ggen import *

# wygeneruj graf

TESTS = 10

print("n;przegladanie_dfs;przegladanie_bfs;dfs_sort_matrix;dfs_sort_list;dfs_sort_table;")

for _size in [100 * (i + 1) for i in range(10)]:
    matrix = Generator(_size).matrix
    successors_list = lista_nastepnikow(deepcopy(matrix))
    edge_table = tabela_krawedzi(deepcopy(matrix))
    print(f'{_size};', end='')

    # DFS
    _record = []
    for i in range(TESTS):
        start = time()
        przegladanie_dfs(successors_list)
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # BSF
    _record = []
    for i in range(TESTS):
        start = time()
        przegladanie_bfs(successors_list)
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # sort_bfs_by_matrix
    _record = []
    for i in range(TESTS):
        start = time()
        dfs_sort_matrix(matrix)
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # sort_bfs_by_list
    _record = []
    for i in range(TESTS):
        start = time()
        dfs_sort_list(successors_list, len(matrix))
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # sort_bfs_by_table
    _record = []
    for i in range(TESTS):
        start = time()
        dfs_sort_table(edge_table, len(matrix))
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    print()

# if __name__ == '__main__':
#     while True:
#         try:
#             x = int(input("\nWybierz opcje:\n0.Wyjscie\n"
#                           "1.Wygenerowac graf losowo\n"
#                           "2.Podac macierz sasiedztwa z klawiatury\n-> "))
#         except ValueError:
#             print(style("[!] Nalezy podac liczbe z zakresu 0..2", fg='red'))
#             continue
#
#         if x == 0:
#             break
#         elif x == 1:
#             _gen_size = int(input("Podaj liczbę wierzchołków grafu -> "))
#             matrix = Generator(_gen_size).matrix
#         elif x == 2:
#             matrix = create_graph()
#         else:
#             print(style("[!] Nalezy podac liczbe z zakresu 0..2", fg='red'))
#             continue
#
#         macierz_sasiedztwa(deepcopy(matrix))
#         successors_list = lista_nastepnikow(deepcopy(matrix))
#         edge_table = tabela_krawedzi(deepcopy(matrix))
#         while True:
#             try:
#                 n = int(input(style("\n(0) Wyjscie\n"
#                                     "(1) Przegladanie DFS\n"
#                                     "(2) Przegladanie BFS\n"
#                                     "(3) Sortowanie topologiczne DFS\n"
#                                     "(4) Sortowanie topologiczne BFS\n", fg='black', bold=True) +
#                               "    Wybierz dzialanie [0/1/2/3/4] -> "))
#             except ValueError:
#                 print(style("[!] Nalezy podac liczbe z zakresu 0..4", fg='red'))
#                 continue
#
#             if n == 0:
#                 break
#             elif n == 1:
#                 print(przegladanie_dfs(successors_list))
#             elif n == 2:
#                 print(przegladanie_bfs(successors_list))
#             elif n == 3:
#                 print("\n-----Sortowanie topologiczne DFS-----")
#                 print(dfs_sort_matrix(deepcopy(matrix)))
#             elif n == 4:
#                 print("\n-----Sortowanie topologiczne BFS-----")
#                 print(sort_bfs_by_matrix(deepcopy(matrix)))
#                 print(sort_bfs_by_list(successors_list, len(matrix)))
#                 print(sort_bfs_by_table(edge_table, len(matrix)))
#             else:
#                 print("Nalezy podac liczbe 0-4.")
#                 continue
