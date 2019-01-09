#!/bin/bash
#Poniżej w zmiennej COMMAND WPISAĆ POLECENIE, które uruchamia program!!!
COMMAND="python3 1-graph.py" #Odpalanie programu w przypadku języka ANSI C
#POZOSTAŁEJ CZĘŚCI SKRYPTU NIE ZMIENIAĆ!!!

echo "Jaki jest typ danych (1 - macierz sąsiedztwa, 2 - lista sąsiedztwa, 3 - lista krawędzi)"
read answer
if ! [[ "$answer" =~ ^[0-9]+$ ]]; then
  echo "Wprowadziłeś nieprawidłową odpowiedź - nie liczbę"
  exit 1
fi
if [[ "$answer" == 1 ]]; then
  echo "Uruchamiam testy dla macierzy sąsiedztwa"
  listOfFiles=`ls adjMatrix | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND < adjMatrix/$testFile
  done
elif [[ "$answer" == 2 ]]; then
  echo "Uruchamiam testy dla list krawędzi"
  listOfFiles=`ls adjList | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND < adjList/$testFile
  done
elif [[ "$answer" == 3 ]]; then
  echo "Uruchamiam testy dla list krawędzi"
  listOfFiles=`ls edgeList | sort -g`
  for testFile in $listOfFiles; do
    echo "Uruchamiam test dla pliku:"$testFile
    $COMMAND < edgeList/$testFile
  done
else
  echo "Nieprawidłowa liczba"
  exit 1
fi


exit 0
