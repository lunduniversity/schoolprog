---
layout: default
title: Triss
permalink: /exercises/three-of-a-kind/
toc: true
type: exercise
tags:
 - nybörjare
 - text
 - variabel
 - kasta tärning
 - sannolikhet
---
# Triss
Hur sannolikt är det att få triss om man slår tre tärningar? I denna uppgift skall vi programmera ett experiment där vi tar reda på det.

Koden i denna uppgift är provkörd på [http://replit.com/languages/python3](http://replit.com/languages/python3) (Python 3).

### 1. Kasta tärning

Vi skulle ju kunna kasta tre tärningar gång på gång på gång för att se hur sannolikt det är att slå triss. Men med ett program kan vi göra det mycket snabbare.

Vi börjar med att bara kasta en tärning en gång och se vad resultatet blir. Vi kan simulera ett tärningskast genom att använda funktionen `randint` i paketet `random`:

```python
import random
k = random.randint(1,6) # Dra ett slumptal mellan 1 och 6.
```

**Uppdrag:** Skriv ett program som simulerar att man kastar en tärning och som skriver ut resultatet (1, 2, 3, 4, 5 eller 6). Kör programmet några gånger så du ser att det verkar fungera. Får du både 1:or och 6:or? Och alla tal där emellan?

### 2. Gör många tärningskast

Vad är sannolikheten för att få en 6:a med en perfekt tärning?

<details>
<summary markdown="span">
Svar:
</summary>
Sannolikheten är 1/6, alltså 0.16666666666...
</details>

Nu ska vi försöka kontrollera detta experimentellt.

**Uppdrag:** Ändra ditt program så att du slår tärningen 100 gånger och räknar hur många 6:or du får. Skriv ut utfallet (antal 6:or genom 100). Exempel på utdata från programmet:

<p><font color="blue">Antal kast: 100<br>
Antal 6:or: 12<br>
Utfall: 0.12</font></p>

*Tips!* Använd en `for`-loop för att slå tärningen 100 gånger. Använd en variabel för att hålla reda på hur många 6:or du får. Exemplet nedan visar hur du kan öka variabeln med 1 varje gång du fått en 6:a

```python
count = 0   # Variabel för att räkna antal 6:or
for i in range(100):
  k = ...
  if k==6:  # Testa om k har värdet 6
    count += 1  # Variabeln ökas med 1
```

<details>
<summary markdown="span">
Lösning:
</summary>
<pre>
import random

count = 0
for i in range(100):
  k = random.randint(1,6)
  if k==6:
    count += 1
print("Antal kast: " + str(100))
print("Antal 6:or: " + str(count))
print("Utfall:     " + str(count/100))
</pre>
</details>

### 3. Variera antalet kast

**Uppdrag:** Inför en variabel `e` för antalet experiment (antalet kast). Kör programmet med olika värden på `e`. Hur stort `e` verkar du behöva för att de två första decimalerna (oftast) skall stämma med den teoretiska sannolikheten?

### 4. Triss

Om vi slår tre tärningar, vad är sannolikheten att få triss?

**Uppdrag:** Skriv ett program som slår tre tärningar ett stort antal gånger, och räknar hur många gånger det blev triss.

*Tips!* Anta att du kallat de tre tärningskasten `k1`, `k2` och `k3`. Du kan jämföra dem genom att skriva `k1==k2==k3`

**Uppdrag:** Vad är den teoretiska sannolikheten för triss? Vilket resultat fick du? Stämmer det på ett ungefär med den teoretiska sannolikheten?

<details>
<summary markdown="span">
Svar:
</summary>
Den första tärningen kan få vilket värde som helst. Sedan är det 1/6 chans att nästa tärning får samma värde. Om detta händer är det sedan 1/6 chans att sista tärningen också får samma värde. Alltså är sannolikheten 1/36 att alla tre har samma värde.
</details>

### 5. Extra: Snabba upp experimentet

Det kan ta lång tid att köra experimentet. Kanske kan man snabba upp det? För att mäta hur lång tid det tar att köra programmet kan man läsa av klockan i början och slutet:

```python
import time
t1 = time.clock()
...
t2 = time.clock()
print("Det tog " + str(t2-t1) + " sekunder")
```

**Uppdrag:** Kan du komma på något sätt att snabba upp experimentet, så du slipper slå alla tre tärningarna i varje omgång? Lägg till tidmätningen till programmet. Prova att snabba upp det. Kontrollera att du får samma resultat som tidigare.

<details>
<summary markdown="span">
Tips 1:
</summary>
Om andra tärningen får ett annat värde än första tärningen så kan du hoppa över att slå tredje tärningen.
</details>

<details>
<summary markdown="span">
Tips 2:
</summary>
Du behöver faktiskt inte slå första tärningen alls. Den skulle fått ett värde, men vilket spelar ingen roll. Du kan anta att värdet till exempel blev 2.
</details>
