from tabulate import tabulate
from copy import deepcopy


def generate():
    """Generuje graf"""
    pass
    # return graph


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
                nastepniki.append(j+1)
        result.append([i+1, " -> ".join(list(map(str, nastepniki)))])
        result2.append([i+1, nastepniki])
    print(tabulate(result, headers=['V', 'lista'], tablefmt='orgtbl'))
    return result2


def tabela_krawedzi(matrix):
    print("\nTabela krawedzi")
    n = len(matrix)
    table = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                table.append([i+1, j+1])
    print(tabulate(table, headers=["out", "in"], tablefmt='orgtbl'))


def find_next(v, result, successors):
    if v in result:
        return result
    result.append(v)
    for i in range(len(successors)):
        if successors[i][0] == v:
            nastepniki_v = successors[i][1]
            for el in nastepniki_v:
                result = find_next(el, result, successors)
            break
    return result


def przegladanieDFS(matrix, successors):
    print("\nPrzegladanie DFS")
    res = []
    for i in range(len(successors)):
        res = find_next(successors[i][0], res, successors)
    res = " -> ".join(list(map(str, res)))
    return res


def przegladanieBFS(graph):
    print("Przegladanie BFS")



def sortowanieDFS(graph):
    print("Sortowanie DFS")
    pass


def sortowanieBFS(graph):
    print("Sortowanie BFS")
    pass


example = [[0, 1, -1, 0, -1],
           [-1, 0, -1, 1, 1],
           [1, 1, 0, -1, 0],
           [0, -1, 1, 0, -1],
           [1, -1, 0, 1, 0]]

while True:
    try:
        x = int(input("\nWybierz opcje:\n0.Wyjscie\n"
                      "1.Wygenerowac graf losowo\n"
                      "2.Podac macierz sasiedztwa z klawiatury\n->"))
    except ValueError:
        print("Nalezy podac liczbe 0-2.")
        continue
    if x == 0:
        break
    elif x == 1:
        # martix = generate()
        generate()
    elif x == 2:
        matrix = create_graph()
    else:
        print("Nalezy podac liczbe 0-2.")
        continue
    macierz_sasiedztwa(deepcopy(matrix))
    successors_list = lista_nastepnikow(deepcopy(matrix))
    tabela_krawedzi(deepcopy(matrix))
    while True:
        try:
            n = int(input("\nWybierz dzialanie dla podanego grafu:\n0.Wyjscie\n"
                          "1.Przegladanie DFS\n"
                          "2.Przegladanie BFS\n"
                          "3.Sortowanie topologiczne DFS\n"
                          "4.Sortowanie topologiczne BFS\n->"))
        except ValueError:
            print("Nalezy podac liczbe 0-4.")
            continue

        if n == 0:
            break
        elif n == 1:
            print(przegladanieDFS(matrix, successors_list))
        elif n == 2:
            print(2)
            # print(przegladanieBFS(graph))
        elif n == 3:
            print(3)
            # print(sortowanieDFS(graph))
        elif n == 4:
            print(4)
            # print(sortowanieBFS(graph))
        else:
            print("Nalezy podac liczbe 0-4.")
            continue
