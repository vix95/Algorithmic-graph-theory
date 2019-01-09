# Algorytmiczna teoria grafów 2017-2018 (Studia niestacjonarne)
## Laboratorium 2 (Podstawowe operacje na grafach skierowanych)

**Zadanie 1** (\*8 pkt)

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

Sklonować repozytorium i odpalić program na przykładach znajdujących się w folderze **edgeList** lub **adjMatrix**. 
Zmodyfikować plik **runTests.sh** o odpalanie wywoływanego programu (w pliku znajduje się odpowiednia zakomentowana linia).

----------------------------

**Zadanie 2** (1 pkt)

Przerób program, odpowiadający na pytanie czy graf posiada ścieżke/cykl Eulera na grafy skierowane.

-----------------------------

**Zadanie 3** (2 pkt) 

Źródłem nazywamy wierzchołek w grafie skierowanym G taki, że nie ma od żadnych krawędzi wchodzących (indeg = 0). Ujściem nazywamy wierzchołek w grafie skierowanym G taki, że nie ma od żadnych krawędzi wychodzących (outdeg = 0). 
Napisz program, który dla dowolnego grafu skierowanego G, obliczy ile jest źródeł oraz ujść w tym grafie.

-----------------------------

**Zadanie 4** (1 pkt) 

Odwróceniem grafu skierowanego G jest graf skierowany H otrzymany przez odwrócenie wszystkich łuków ("strzałek") w grafie G.
Napisz program, który dla danego grafu skierowanego tworzy jego odwrócenie.

-----------------------------

**Zadanie domowe** (\*8 pkt)

Napisz program, który dla dowolnego grafu **nieskierowanego** wypisze jego kolorowanie metodą LF lub SL. 

```
WEJŚCIE: Graf G podany jako lista krawędzi, macierz sąsiedztwa lub lista sąsiedztwa
WYJŚCIE: Kolorowanie metodą LF oraz SL wraz z podaniem liczby chromatycznej tego grafu.
Przykładowe wywołania programu: 
Dla danej macierzy sąsiedztwa (oraz jego odpowiednika w postaci list krawędzi):
0 1 0 0 0
1 0 1 0 0
0 1 0 1 0 = 1 2 2 3 3 4 4 5 
0 0 1 0 1
0 0 0 1 0
Kolorowanie metodą LF: [0 1 0 1 0] (liczba chromatyczna = 2)
Kolorowanie metodą SL: [1 0 1 0 1] (liczba chromatyczna = 2)

Natomiast dla grafu oraz jego listy sąsiedztwa: 
1 2
2 3
3 4
4 5
5
Kolorowanie metodą LF: [0 1 0 1 0] (liczba chromatyczna = 2)
Kolorowanie metodą SL: [1 0 1 0 1] (liczba chromatyczna = 2)
```

**UWAGI:** 

- Procedura sortująca powinna być napisana "od zera". Nie będzie akceptowane rozwiązanie za pomocą metody **sort()**.
- Algorytm LF i SL są algorytmami aproksymacyjnymi. Istnieją grafy, dla których kolorowanie tą metodą **zawsze** się pomyli!!! 

- 8 pkt - za napisanie programu, który w argumencie wywołania wypisze kolorowanie lub liczbę chromatyczną grafu. 
- 6 pkt - za napisanie programu, który jednocześnie wypisze kolorowanie wierzchołków oraz liczbę chromatyczną grafu.

Program wczytuje graf ze standardowego wejścia **(STDIN)**. 
Wierzchołki numerowane są od **jedynki**.

**TERMINY:**
- 26.05.2018 (100 %)
- 09.05.2018 (75 %)


