from copy import deepcopy

from tabulate import tabulate
from click import style

from ggen import Generator
from repr import *


def create_graph():
    """Tworzy graf"""
    v = int(input("Podaj ilosc wierzcholkow grafu:"))
    print("Podaj kolejne wiersze macierzy sasiedztwa:")
    matrix = []
    for i in range(v):
        line = list(map(int, input(f"{i+1} linia:").split()))
        matrix.append(line)
    return matrix


def macierz_sasiedztwa(matrix):
    print("\nMacierz sasiedztwa")
    headings = [" "] + [f"V{j+1}" for j in range(len(matrix))]
    i = 1
    for line in matrix:
        line.insert(0, f"V{i}")
        i += 1
    print(tabulate(matrix, headers=headings, tablefmt='orgtbl'))


def lista_nastepnikow(matrix):
    print("\nLista nastepnikow")
    result = []
    result2 = []
    n = len(matrix)
    for i in range(n):
        nastepniki = []
        for j in range(n):
            if matrix[i][j] == 1:
                nastepniki.append(j + 1)
        result.append([i + 1, " -> ".join(list(map(str, nastepniki)))])
        result2.append([i + 1, nastepniki])
    print(tabulate(result, headers=['V', 'lista'], tablefmt='orgtbl'))
    return result2


def tabela_krawedzi(matrix):
    print("\nTabela krawedzi")
    n = len(matrix)
    table = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                table.append([i + 1, j + 1])
    print(tabulate(table, headers=["out", "in"], tablefmt='orgtbl'))
    return table


def dfs(v, result, successors):
    if v in result:
        return result
    result.append(v)
    for i in range(len(successors)):
        if successors[i][0] == v:
            nastepniki_v = successors[i][1]
            for el in nastepniki_v:
                result = dfs(el, result, successors)
            break
    return result


def przegladanie_dfs(successors):
    print("\nPrzegladanie DFS")
    res = []
    for i in range(len(successors)):
        res = dfs(successors[i][0], res, successors)
    res = " -> ".join(list(map(str, res)))
    return res


def bfs(v, result, successors):
    for i in range(len(successors)):
        if successors[i][0] == v:
            nastepniki_v = successors[i][1]
            to_ignore = []
            for el in nastepniki_v:
                if el not in result:
                    result.append(el)
                else:
                    to_ignore.append(el)
            for el in nastepniki_v:
                if el not in to_ignore:
                    result = bfs(el, result, successors)
            break
    return result


def przegladanie_bfs(successors):
    print("\nPrzegladanie BFS")
    res = []
    for i in range(len(successors)):
        nastepniki = successors[i][0]
        if nastepniki not in res:
            res.append(nastepniki)
            res = bfs(nastepniki, res, successors)
    res = " -> ".join(list(map(str, res)))
    return res


def dfs_sort_matrix(matrix):
    res = []
    print(style("Sortowanie DFS >> Macierz", fg='blue'))
    # for i in range(len(matrix)):
    #     if matrix[i][i] == 0:
    #         matrix[i][i] = 1  # "szary"
    #     if


# FUNCS
def next_by_matrix(matrix, i):
    successors = []
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            successors.append(j + 1)
    return successors


def next_by_list(list, i):
    return list[i][1]


def next_by_table(table, i):
    successors = []
    for j in range(len(table)):
        if table[j][0] == i + 1:
            successors.append(table[j][1])
    return successors


# sortowanie BFS
# macierz


def create_in_degree_matrix(matrix):
    in_degree = []
    for i in range(len(matrix)):
        degree = matrix[i].count(-1)
        in_degree.append([i + 1, degree])
    return in_degree


def sort_bfs_by_matrix(matrix):
    in_degree = create_in_degree_matrix(matrix)
    print("\nDla macierzy sasiedztwa")
    return sortowanieBFS(in_degree, next_by_matrix, matrix)


# lista
def create_in_degree_list(list, n):
    in_degree = []
    flatten = sum([list[k][1] for k in range(len(list))], [])
    for i in range(n):
        degree = flatten.count(i + 1)
        in_degree.append([i + 1, degree])
    return in_degree


def next_by_list(list, i):
    return list[i][1]


def sort_bfs_by_list(list, n):
    in_degree = create_in_degree_list(list, n)
    print("\nDla listy nastepnikow")
    return sortowanieBFS(in_degree, next_by_list, list)


# tabela
def create_in_degree_table(table, n):
    in_degree = []
    flatten = [table[k][1] for k in range(len(table))]
    for i in range(n):
        degree = flatten.count(i + 1)
        in_degree.append([i + 1, degree])
    return in_degree


def sort_bfs_by_table(table, n):
    print("\nDla tabeli krawedzi")
    in_degree = create_in_degree_table(table, n)
    return sortowanieBFS(in_degree, next_by_table, table)


def lower_degree(successors, in_degree):
    for i in range(len(in_degree)):
        if in_degree[i][0] in successors:
            in_degree[i][1] -= 1
    return in_degree


def sortowanieBFS(in_degree, find_next, data):
    result = []
    while max([in_degree[k][1] for k in range(len(in_degree))]) > -1:
        for i in range(len(in_degree)):
            if in_degree[i][1] == 0:
                in_degree[i][1] = -1
                result.append(i + 1)
                successors = find_next(data, i)
                in_degree = lower_degree(successors, in_degree)
    return " -> ".join(list(map(str, result)))


if __name__ == '__main__':
    while True:
        try:
            x = int(input("\nWybierz opcje:\n0.Wyjscie\n"
                          "1.Wygenerowac graf losowo\n"
                          "2.Podac macierz sasiedztwa z klawiatury\n-> "))
        except ValueError:
            print(style("[!] Nalezy podac liczbe z zakresu 0..2", fg='red'))
            continue

        if x == 0:
            break
        elif x == 1:
            _gen_size = int(input("Podaj liczbę wierzchołków grafu -> "))
            matrix = Generator(_gen_size).matrix
        elif x == 2:
            matrix = create_graph()
        else:
            print(style("[!] Nalezy podac liczbe z zakresu 0..2", fg='red'))
            continue

        macierz_sasiedztwa(deepcopy(matrix))
        successors_list = lista_nastepnikow(deepcopy(matrix))
        edge_table = tabela_krawedzi(deepcopy(matrix))
        while True:
            try:
                n = int(input(style("\n(0) Wyjscie\n"
                                    "(1) Przegladanie DFS\n"
                                    "(2) Przegladanie BFS\n"
                                    "(3) Sortowanie topologiczne DFS\n"
                                    "(4) Sortowanie topologiczne BFS\n", fg='black', bold=True) +
                              "    Wybierz dzialanie [0/1/2/3/4] -> "))
            except ValueError:
                print(style("[!] Nalezy podac liczbe z zakresu 0..4", fg='red'))
                continue

            if n == 0:
                break
            elif n == 1:
                print(przegladanie_dfs(successors_list))
            elif n == 2:
                print(przegladanie_bfs(successors_list))
            elif n == 3:
                print("\n-----Sortowanie topologiczne DFS-----")
                print(dfs_sort_matrix(deepcopy(matrix)))
            elif n == 4:
                print("\n-----Sortowanie topologiczne BFS-----")
                print(sort_bfs_by_matrix(deepcopy(matrix)))
                print(sort_bfs_by_list(successors_list, len(matrix)))
                print(sort_bfs_by_table(edge_table, len(matrix)))
            else:
                print("Nalezy podac liczbe 0-4.")
                continue
