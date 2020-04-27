def generate():
    """Generuje graf"""
    pass
    # return graph


def create_graph():
    """Tworzy graf"""
    pass
    # return graph


def macierz_sasiedztwa(graph):
    print("\nMacierz sasiedztwa")
    pass
    # return matrix


def lista_nastepnikow(graph):
    print("\nLista nastepnikow")
    pass
    # return list


def tabela_krawedzi(graph):
    print("\nTabela krawedzi")
    pass
    # return table


def przegladanieDFS(graph):
    print("Przegladanie DFS")
    pass


def przegladanieBFS(graph):
    print("Przegladanie BFS")
    pass


def sortowanieDFS(graph):
    print("Sortowanie DFS")
    pass


def sortowanieBFS(graph):
    print("Sortowanie BFS")
    pass


while True:
    try:
        x = int(input("\nWybierz opcje:\n0.Wyjscie\n1.Wygenerowac graf losowo\n2.Podac macierz sasiedztwa z klawiatury\n->"))
    except ValueError:
        print("Nalezy podac liczbe 0-2.")
        continue
    if x == 0:
        break
    elif x == 1:
        # graph = generate()
        generate()
    elif x == 2:
        # graph = generate()
        create_graph()
    else:
        print("Nalezy podac liczbe 0-2.")
        continue
    # print(macierz_sasiedztwa(graph))
    # print(lista_nastepnikow(graph))
    # print(tabela_krawedzi(graph))
    while True:
        try:
            n = int(input("\nWybierz dzialanie dla podanego grafu:\n0.Wyjscie\n1.Przegladanie DFS\n2.Przegladanie BFS\n3.Sortowanie topologiczne DFS\n"
                          "4.Sortowanie topologiczne BFS\n->"))
        except ValueError:
            print("Nalezy podac liczbe 0-4.")
            continue
        if n == 0:
            break
        elif n == 1:
            print(1)
            # print(przegladanieDFS(graph))
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
