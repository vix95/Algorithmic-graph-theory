# Algorytmiczna teoria grafów 2017-2018 (Studia niestacjonarne)
## Laboratorium 2 (Grafy eulerowskie oraz 2-kolorowanie grafów)

**Zadanie 1** (\*8 pkt)

Napisz program, który dla grafu G podanego jako lista lub macierz sąsiedztwa, sprawdzi czy podany graf jest eulerowski/półeulerowski.

**Wskazówka:** Należy zbadać spójność grafu!

```
WEJŚCIE: Graf G = (VG, EG) podany jako lista lub macierz sąsiedztwa.
WYJŚCIE: Informacja, czy graf jest eulerowski/półeulerowski/nieulerowski/niespójny.
```

- 8 pkt - maksymalna liczba punktów dla wersji przy użyciu list sąsiedztwa (wersja krawędziowa).
- 6 pkt - maksymalna liczba punktów dla wersji przy użyciu macierzy sąsiedztwa.

Przykładowe wywołania programu:
```
Macierz sasiedztwa oraz lista sasiedztwa (wersja krawedziowa) tego samego grafu:
0 1 0 0 0 1
1 0 1 0 0 0
0 1 0 1 0 0 = 1 2 1 6 2 3 3 4 4 5 5 6
0 0 1 0 1 0
0 0 0 1 0 1
1 0 0 0 1 0
Jest eulerowski
Macierz sasiedztwa oraz lista sasiedztwa (wersja krawedziowa) tego samego grafu:
0 1 1 1 1 1
1 0 1 0 1 1
1 1 0 1 1 0 = 1 2 1 3 1 4 1 5 1 6 2 3 2 5 2 6 3 4 3 5 4 6 5 6
1 0 1 0 0 1
1 1 1 0 0 1
1 1 0 1 1 0
Jest poleulerowski
```

Sklonować repozytorium i odpalić program na przykładach znajdujących się w folderze **edgeList** lub **adjMatrix**. 
Zmodyfikować plik **runTests.sh** o odpalanie wywoływanego programu (w pliku znajduje się odpowiednia zakomentowana linia). 

----------------------------

**Zadanie 2** (1 pkt)

Napisz program, który dla grafu G podanego jako lista lub macierz sąsiedztwa, wyświetli sąsiadów każdego wierzchołka grafu G.

----------------------------

**Zadanie 3** (2 pkt)

Napisz program, który dla **digrafu** G podanego jako lista lub macierz sąsiedztwa, wyświetli liczbę krawędzi wchodzących i wychodzących oraz listę sąsiadów dla każdego wierzchołka digrafu G.

----------------------------

**Zadanie dodatkowe** (4 pkt)

Wypisz cykl/ścieżkę eulera dla danego grafu eulerowskiego/półeulerowskiego.

----------------------------

**Zadanie domowe** (\*8 pkt) - do oddania na następnym zjeździe.

Napisz program, w którym użytkownik podaje graf i otrzymuje informację, czy podany graf jest dwudzielny. W przypadku pozytywnej odpowiedzi program zwraca podział zbioru wierzchołków na dwa rozłączne podzbiory - tzw. partycje dwudzielności.

```
WEJŚCIE: Graf G podany jako lista lub macierz sąsiedztwa.
WYJŚCIE: Informacja, czy graf jest dwudzielny. W przypadku pozytywnej odpowiedzi wypisanie partycji dwudzielności grafu G.
Przykładowe wywołania programu: 
Dla danej macierzy sąsiedztwa (oraz jego odpowiednika w postaci list krawędzi):
0 0 1 1 1 1
0 0 1 1 1 1
1 1 0 0 1 1 = 1 3 1 4 1 5 1 6 2 3 2 4 2 5 2 6 3 5 3 6 4 5 4 6 
1 1 0 0 1 1
1 1 1 1 0 0
1 1 1 1 0 0
Odpowiedź jest negatywna

Natomiast dla danej macierzy sąsiedztwa (oraz jego odpowiednika w postaci list krawędzi): 
0 0 0 1 1 1 1
0 0 0 1 1 1 1
0 0 0 1 1 1 1
1 1 1 0 0 0 0 = 1 4 1 5 1 6 1 7 2 4 2 5 2 6 2 7 3 4 3 5 3 6 3 7 
1 1 1 0 0 0 0
1 1 1 0 0 0 0
1 1 1 0 0 0 0
Odpowiedź jest pozytywna oraz partycja dwudzielności wygląda następująco: 
X = [1,2,3]
Y = [4,5,6,7]
```

- 8 pkt - za wykorzystanie struktury list sąsiedztwa
- 6 pkt - za wykorzystanie struktury macierzy sąsiedztwa

Program wczytuje graf ze standardowego wejścia **(STDIN)**. 
Wierzchołki numerowane są od **jedynki**.

**TERMINY:**
- 12.05.2018 (100 %)
- 26.05.2018 (75 %)
- 09.06.2018 (50 %)

Program należy wrzucić do repozytorium, które utworzy się na następnym zjeździe
