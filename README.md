# GRAFER

## TO-DO

- [x] Wygeneruj spójny skierowany graf acykliczny o n wierzchołkach
  - [x] współczynnik nasycenia łukami w grafie powinien być równy 50% (czyli 50% z `n(n-1)/2`)
  - [x] najłatwiej jest utworzyć graf acykliczny skierowany poprzez wypełnienie odpowiednią liczbą jedynek górnego trójkąta macierzy sąsiedztwa
- [x] Graf może zostać utworzony również poprzez podanie z klawiatury wierszy macierzy sąsiedztwa
- [x] Graf jest reprezentowany poprzez macierz sąsiedztwa, listę następników oraz tabelę krawędzi - wyświetl je.
- [x] Zaimplementuj funkcje przechodzenia grafu wszerz i w głąb (z wyświetlaniem). – Dybde-først-søk og Bredde-først-søk med utstilling
- [x] Zaimplementuj dwa algorytmy sortowania topologicznego dla każdej z reprezentacji zgodnie z algorytmem przeszukiwania:
  - [x] w głąb - etykietowanie wierzchołków (biały-nieodwiedzony, szary-przetwarzany, czarny-zakończony)
  - [x] wszerz - wyszukiwanie wierzchołków bez krawędzi wejściowych, usuwanie ich następników, powtarzanie iteracji dopóki wszystkie wierzchołki nie będą wypisane
- [x] Po utworzeniu grafu (losowo lub z klawiatury) użytkownik może dla tego grafu wykonać dowolne procedury przeglądania lub sortowania grafu

## TEST

- [x] dokonaj pomiaru czasu działania algorytmów dla każdej reprezentacji grafu
- [x] ogólne idee algorytmów, mają być takie same dla różnych reprezentacji grafu, różnice wynikają z innej złożoności wyszukiwania następników w grafie
- [x] nie należy przekształcać każdej reprezentacji np. w liste następników, a nastepnie sortować
- [x] nie należy upraszczać algorytmów ze względu na przygotowanie danych wejściowych (np. macierz sąsiedztwa jest górnotrójkątna i tylko tam sprawdzamy czy są łuki)
- [x] Pomiary czasu przedstaw na wykresie `t=f(n)`, dla 10 różnych wartości `n`

## GENERATOR

### CLI

```sh
# wygeneruj z pytaniem o wielkosć grafu
python3 ggen.py

# wygeneruj z określoną wielkością
# python3 ggen.py [SIZE]
python3 ggen.py 10

# wygeneruj z danymi wejściowymi do potoku
# python3 ggen.py [SIZE] -test
python3 ggen.py 10 -test

# użycie w potoku; przykład
python3 ggen.py 10 -test | python3 main.py
```

### Module

```py
from ggen import Generator
# …
graphMatrix = Generator(size).matrix
```
