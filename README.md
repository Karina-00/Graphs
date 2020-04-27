# GRAFER

## GJØR

- [ ] Wygeneruj spójny skierowany graf acykliczny o n wierzchołkach
  - [ ] współczynnik nasycenia łukami w grafie powinien być równy 50% (czyli 50% z `n(n-1)/2`)
  - [ ] najłatwiej jest utworzyć graf acykliczny skierowany poprzez wypełnienie odpowiednią liczbą jedynek górnego trójkąta macierzy sąsiedztwa
- [x] Graf może zostać utworzony również poprzez podanie z klawiatury wierszy macierzy sąsiedztwa
- [X] Graf jest reprezentowany poprzez macierz sąsiedztwa, listę następników oraz tabelę krawędzi - wyświetl je.
- [X] Zaimplementuj funkcje przechodzenia grafu wszerz i w głąb (z wyświetlaniem). – Dybde-først-søk og Bredde-først-søk med utstilling
- [ ] Zaimplementuj dwa algorytmy sortowania topologicznego dla każdej z reprezentacji zgodnie z algorytmem przeszukiwania:
- [ ] w głąb - etykietowanie wierzchołków (biały-nieodwiedzony, szary-przetwarzany, czarny-zakończony)
- [X] wszerz - wyszukiwanie wierzchołków bez krawędzi wejściowych, usuwanie ich następników, powtarzanie iteracji dopóki wszystkie wierzchołki nie będą wypisane
- [X] Po utworzeniu grafu (losowo lub z klawiatury) użytkownik może dla tego grafu wykonać dowolne procedury przeglądania lub sortowania grafu

## TEST

- [ ] dokonaj pomiaru czasu działania algorytmów dla każdej reprezentacji grafu
- [ ] ogólne idee algorytmów, mają być takie same dla różnych reprezentacji grafu, różnice wynikają z innej złożoności wyszukiwania następników w grafie
- [ ] nie należy przekształcać każdej reprezentacji np. w liste następników, a nastepnie sortować
- [ ] nie należy upraszczać algorytmów ze względu na przygotowanie danych wejściowych (np. macierz sąsiedztwa jest górnotrójkątna i tylko tam sprawdzamy czy są łuki)
- [ ] Pomiary czasu przedstaw na wykresie `t=f(n)`, dla 10 różnych wartości `n`
