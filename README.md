# Hangman
Hangman.

Proiect realizat de Bălănean Mihai-Cristian

Instructiuni de rulare:
  python hangman.py \
  --input cuvinte_de_verificat.csv \
  --output date_iesire.csv \
  --dict dictionar_mijloc.txt

'hangman.py' - fisierul sursa
'cuvinte_de_verificat.csv' - fisierul .csv folosit pentru testing
'date_iesire.csv' - fisierul ce contine datele de iesire cerute
'dictionar_mijloc.txt' - dictionarul folosit pentru imbunatatirea eficentei programului - rezulta in 1098 de incercari totale pe fisierul 'cuvinte_de_verificat.csv'

Observatii:

Exista 3 fisiere ce pot fi folosite ca dictionar. Cel mai recomandat de folosit este fisierul 'dictionar_mijloc.csv' care contine cuvintele de test la mijlocul sau,
simuland astfel o distributie a cuvintelor mai aproape de cea bazata pe o sortare alfabetica.

Celelalte doua fisiere: 'dictionar_inceput.csv' si 'dictionar_sfarsit.csv' sunt menite sa arate cel mai bun, respectiv cel mai rau, caz posibil pentru aceasta abordare a problemei
