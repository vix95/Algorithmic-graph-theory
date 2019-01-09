# Algorytmiczna teoria grafów 2017-2018 (Studia niestacjonarne)
## Laboratorium 4 (Podstawowe produkty grafowe)

**Zadanie 1** (\*8 pkt)

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
- 09.06.2018 (75 %)
- ??.06.2018 (50 %)
--------------

**Dane testowe do zadań 2-5 są w pliku DaneLab4.zip**

----------------

**Zadanie 2** (1 pkt)

Dopełnieniem grafu prostego <a href="https://www.codecogs.com/eqnedit.php?latex=G=(V_G,E_G)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G=(V_G,E_G)" title="G=(V_G,E_G)" /></a> nazywamy graf <a href="https://www.codecogs.com/eqnedit.php?latex=\overline{G}&space;=&space;(V_G,E_{\overline{G}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\overline{G}&space;=&space;(V_G,E_{\overline{G}})" title="\overline{G} = (V_G,E_{\overline{G}})" /></a>, w którym dwa wierzchołki są sąsiednie wtedy i tylko wtedy, gdy nie są sąsiednie w grafie G.

Zaimplementuj metodę, która dla dowolnego grafu nieskierowanego będzie tworzyło jego dopełnienie.

----------------

**Zadanie 3** (2 pkt) 

Grafem krawędziowym <a href="https://www.codecogs.com/eqnedit.php?latex=L(G)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?L(G)" title="L(G)" /></a> grafu prostego <a href="https://www.codecogs.com/eqnedit.php?latex=G=(V_G,E_G)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G=(V_G,E_G)" title="G=(V_G,E_G)" /></a> nazywamy graf, którego wierzchołki stoją we wzajemnie jednoznacznej odpowiedniości z krawędziami grafu G i taki, że jego wierzchołki są sąsiednie wtedy i tylko wtedy, gdy odpowiadające im krawędzie grafu są sąsiednie. 

Zaimplementuj metodę, która dla dowolnego grafu prostego G, będzie tworzyło jego graf krawędziowy.

**Zadanie 4** (1 pkt) 

Kwadratem grafu <a href="https://www.codecogs.com/eqnedit.php?latex=G=(V_G,E_G)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G=(V_G,E_G)" title="G=(V_G,E_G)" /></a> nazywamy graf <a href="https://www.codecogs.com/eqnedit.php?latex=G^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G^2" title="G^2" /></a>, taki, że dla wierzchołków <a href="https://www.codecogs.com/eqnedit.php?latex=u,v&space;\in&space;V_G" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u,v&space;\in&space;V_G" title="u,v \in V_G" /></a> krawędź <a href="https://www.codecogs.com/eqnedit.php?latex=uv&space;\in&space;E_G^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?uv&space;\in&space;E_G^2" title="uv \in E_G^2" /></a> wtedy i tylko wtedy, gdy graf G zawiera ścieżkę między u i v złożoną z co najwyżej dwóch krawędzi. 

Zaimplementuj metodę, która dla dowolnego grafu nieskierowanego będzie tworzyło jego potęgę grafu. 

(+1 pkt) dla działającej metody dla grafu skierowanego.

**Wskazówka:** Wystarczy podnieść do kwadratu macierz sąsiedztwa grafu G.

**Zadanie 5** (Dodatkowe na 2 pkt)

Średnicą grafu <a href="https://www.codecogs.com/eqnedit.php?latex=G=(V_G,E_G)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G=(V_G,E_G)" title="G=(V_G,E_G)" /></a> nazywamy najdłuższą v-u ścieżkę biegnącą w grafie G. Zaimplementuj metodę, która będzie obliczać średnicę dla danego grafu G. 

**Wskazówki:** Skorzystaj z algorytmu Dijkstry lub z operacji potęgi grafu.
