---
title: Implementera aritmetiska operatorer
toc: true
type: exercise
layout: default
tags:
 - medel
 - text
 - aritmetik
 - funktioner
permalink: /exercises/implement-arithmetic-operators/
---
# Implementera aritmetiska operatorer

I denna uppgift skall vi undersöka hur vi kan klara oss med enbart addition och negerade tal för att räkna ut olika uttryck och implementera andra operatorer.

Koden i denna uppgift är provkörd på [http://repl.it/languages/python3](http://repl.it/languages/python3) (Python 3).

### 1. Addition och negation

Vi börjar med att implementera funktioner för addition och negation med hjälp av Pythons inbyggda operatorer `+` och `-`. Vi kallar funktionerna `add` och `neg`:

```python
def add(a, b):
  return a + b

def neg(a):
  return -a
```

**Uppdrag:** Skriv in funktionerna ovan. Använd print-satser för att undersöka vad följande uttryck blir:

- `add(3, 5)`
- `neg(7)`
- `add(add(3, 5), neg(7))`
- `add(neg(7), add(3, 5))`

**Uppdrag:** Använd `add`, `neg` och konstanterna `2`, `5` och `10` för att skriva ut värdena `4`, `7` och `8`.

**Uppdrag:** Kan du hitta (minst) tre olika uttryck där du använder `add`, `neg` och konstanterna `2`, `5` och `10` för att skriva ut värdet `6`?

### 2. Subtraktion

Vi kan subtrahera `b` från `a` genom att skriva `add(a, neg(b))`. Men det vore trevligt att ha en funktion `sub` så att vi kan skriva `sub(a, b)` i stället:

```python
def sub(a, b):
  return ...
```
**Uppdrag:** Implementera funktionen `sub` enbart genom att använda funktionerna `add` och `neg`. Kontrollera att funktionen fungerar genom att testa den på t.ex. följande exempel:

- `sub(100, 3)`
- `sub(1, 1001)`

(Vad borde resultatet bli?)

**Uppdrag:** Kan du uttrycka värdet `11` med hjälp av funktionerna `add` och `sub` och konstanterna `2`, `5` och `10`?

### 3. Multiplikation

Vi skulle vilja ha en funktion för multiplikation:

```python
def mul(a, b):
  ...
  return ...
```

så att om vi t.ex. anropar `mul(3, 5)` så får vi värdet `15`.

Vi kan implementera `mul` genom addera många gånger i en loop!

**Uppdrag:** Implementera funktionen `mul` genom att använda en loop och anropa `add`. Kontrollera att din funktion fungerar för `mul(3, 5)`.

*Tips!* Vi kan använda en variabel `result` som vi börjar med att sätta till `0`. Sedan kan vi loopa `b` gånger, och i varje varv lägga till `a` till `result` med hjälp av `add`.

**Uppdrag:** Testa din funktion mer. Kontrollera t.ex. att den fungerar för:

- `mul(0, 10)`
- `mul(1000, 1000)`

(Vad borde resultatet bli?)

### 4. Heltalsdivision

I Python 3 skrivs vanlig division som `a/b` och heltalsdivision som `a//b`.  Resultatet av en heltalsdivision är heltalsdelen av vanlig division. Till exempel är `14/3 = 4.666...`, medan `14//3 = 4`.

Om resultatet går jämnt ut blir resultatet för heltalsdivision detsamma som för vanlig division. Till exempel är både `12/4 = 3` och `12//4 = 3`.

Vi kan tänka på heltalsdivision som att vi ska räkna ut hur många tegelstenar av längd `b` som får plats i en avlångt utrymme av längd `a`. När vi har lagt ner så många stenar som möjligt så kanske det finns lite plats över i utrymmet, men den platsen kommer i så fall att vara kortare än `b`.

Vi skall implementera en funktion `intdiv(a, b)` som räknar ut heltalsdivision enbart med hjälp av våra funktioner `add` och `sub`, alltså *utan* att använda den inbyggda operatorn `//`.

Ett sätt att implementera `intdiv` är att använda en loop som simulerar att vi provar med allt fler tegelstenar ända tills de inte får plats.

**Uppdrag:** Implementera `intdiv` och prova att den fungerar genom att anropa `intdiv(14, 3)` och `intdiv(12, 4)`.

*Tips!* Använd en variabel `bricks` som håller reda på antalet tegelstenar och en variabel `length` som håller reda på sammanlagda längden av tegelstenarna. Börja med att sätta båda till 0. Använd en while-loop som ökar `length` med `b` och `bricks` med 1 så länge som `length` är mindre än eller lika med `a`. När while-loopen är färdig har vi alltså provat med en tegelsten för mycket, och resultatet av heltalsdivisionen är alltså ett mindre än `bricks`.

<details>
<summary markdown="span">
Lösning
</summary>
<pre>
def intdiv(a, b):
  length = 0
  bricks = 0
  while (length <= a):
    length = add(length, b)
    bricks = add(bricks, 1)
  return sub(bricks, 1)
</pre>
</details>

### 5. Exponentiering

*Exponentiering* skrivs matematiskt <i>b<sup>n</sup></i> och i programmeringsspråk som `b**n`. Operatorn `**` kallas *power*, eller på svenska *potens* eller *upphöjt-till*. Exponentiering motsvarar upprepad multiplikation. Till exempel är `3**5` lika med `3*3*3*3*3` det vill säga lika med `243`.

Vi skall implementera en funktion `power(b, n)` som räknar ut exponentiering enbart med hjälp av vår tidigare funktion `mul`, alltså utan att använda den inbyggda operatorn `**`.

Funktionen skall fungera för heltal `b > 0` och `n >= 0`, alltså där basen `b` är ett positivt heltal och exponenten `n` är större än eller lika med `0`. Om exponenten `n` är `0` är resultatet alltid `1`. Till exempel är `137**0` lika med `1`.

**Uppdrag:** Implementera `power` och kontrollera att den fungerar för till exempel `power(3, 5)` och `power(137, 0)`.

*Tips!* Vi kan använda en variabel `result` som vi börjar med att sätta till `1`. Sedan kan vi loopa `n` gånger, och i varje varv multiplicera `result` med `b` med hjälp av funktionen `mul`.

### 6. Kommentarer

I uppgifterna ovan har vi lyckats implementera funktioner för subtraktion, multiplikation, heltalsdivision och exponentiering enbart genom att bygga på addition och negering. Detta illustrerar hur vi både inom matematiken och programmering kan bygga upp komplexa operationer genom att börja med enkla byggstenar och definiera nya operationer i termer av dem.
