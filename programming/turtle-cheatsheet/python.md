---
layout: page
title: Python-turtle snabbreferens
permalink: turtle-cheatsheet/python
toc: true
---


Denna kod är provkörd på online-miljön [python-turtle på repl.it](http://repl.it/languages/python-turtle) för Python 2.7.

# Kom igång

Python-turtle är en online-miljö för programspråket Python 2.7 och med stöd för "turtle graphics". Här är ett program som ritar en liten figur.

```python
import turtle        # Importera biblioteket för sköldpaddan
t = turtle.Turtle()  # Skapa en ny padda som vi kallar t

t.forward(20)        # t går framåt 20 steg
t.right(60)          # t svänger höger 60 grader
t.forward(30)        # t går framåt 30 steg
```

*Obs!* I exemplen nedan förutsätter vi att du har med de två första raderna ovan (`import`... och `t =`) först i varje program.

# Styr sköldpaddan

## Styr med relativa kommandon

```python
t.forward(20) # Paddan går 20 steg framåt
t.back(20)    # Paddan går 20 steg framåt
t.right(45)   # Paddan vrider sig 45 grader åt höger
t.left(45)    # Paddan vrider sig 45 grader åt vänster
t.hop(20)     # Paddan hoppar 20 steg framåt, utan att rita
t.hop(-20)    # Paddan hoppar -20 steg framåt, dvs 20 steg bakåt, utan att rita
t.circle(50)  # Paddan ritar en cirkel med radien 50
t.circle(50, extent = 90) # Paddan ritar en båge med radien 50 och vinkeln 90
```

## Hoppa framåt

Det är praktiskt att låta paddan kunna hoppa framåt utan att rita. För att göra detta, klistra in följande funktion som lyfter pennan, går framåt, och sedan sänker pennan igen:

```python
def hop(length):
  t.penup()
  t.forward(length)
  t.pendown()
```

Sedan kan du hoppa framåt. T.ex.

```python
t.forward(10)
hop(20)
t.forward(10)
```

## Styr med absoluta koordinater

```python
t.setpos(100,200) # Paddan hoppar till läget (100, 100) utan att rita
t.setheading(45)  # Paddan vrider nosen till vinkeln 45 grade
```

## Sätt färger, penntjocklek, etc.

```python
t.color("pink")       # Sätter pennans färg till rosa
t.fillcolor("purple") # Sätter ifyllnadfärgen till lila
t.width(20)           # Sätter pennans bredd till 20
```

För att rita en fylld form slår man först på fyllning, och stänger sedan av det igen:

```python
t.fill(True)
t.forward(100)
t.right(90)
t.forward(50)
t.fill(False)
```

## Låt paddan skriva text

```python
t.write("hello")      # Paddan skriver texten "hello"
t.write("hello", font=("Arial", 12, "normal"))  # Skriv med ett visst typsnitt
```

## Sätt hastigheten på paddan
```python
t.speed(1)     # Paddan ritar väldigt långsamt
t.speed(20)    # Paddan ritar väldigt snabbt
t.speed(0)     # Paddan ritar så snabbt som möjligt
```

# Annat du kan göra i Python-turtle

## Läs in och skriv ut

Du kan skriva ut text i paddans "console"-fönster:

```python
print("Hello!")
```

Använd funktionen `input` för att läsa in något som användaren skriver i console-fönstret. Det inlästa värdet blir en sträng: Om användaren skriver `42` så ger `input` strängvärdet `"42"`. Funktionen `int` gör om en sträng till ett heltal, t.ex. `"42"` till `42`.

```python
s = input("Write a string: ")       # läs in en sträng
i = int(input("Write a number: "))  # läs in ett heltal
```

*Obs!* Python-turtle klarar inte svenska tecken som `åäö` i sina strängar. Därför är frågorna ovan på engelska.

## Sätta ihop strängar

När du skriver ut är det ofta praktiskt att sätta ihop strängar. Det kan man göra med `+`. Men tal och andra värden som inte är strängar från början behöver då omvandlas till strängar med hjälp av funktionen `str`:

```python
print("En vecka har " + str(7) + " dagar.")
```

## Dra slumptal

För att dra slumptal behöver du importera funktionen randint från biblioteket random:

```python
from random import randint
t = randint(1,9)       # Ger ett slumptal mellan 1 och 9
```

# Tangentbordet

Har du svårt att hitta vissa tecken på tangentbordet? För ett svenskt tangentbord behöver du känna till:

* SKIFT-tangenten - den man får stora bokstäver med
* På Mac: ALT-tangenten - sitter någonstans nere till vänster.
* På Windows: ALT-GR-tangenten - sitter någonstans nere till höger. Ibland är den bara märkt med ALT.

Genom att hålla nere en eller flera av dessa tangenter innan du trycker på en annan tangent kan du få fram ovanliga tecken.

* `#` kallas "brädgård" ("hash" på engelska). Används för att inleda en kommentar i Python.
* `*` används för multiplikation i kod.
* `[]` kallas "hakparenteser" ("square brackets" på engelska). Används för listor i Python.
* `{ }` kallas "krullparenteser" eller "måsvingar" ("curly brackets", "braces", eller "curly braces" på engelska). Används för mängder i Python.

Prova att hålla nere SKIFT-tangenten för att få fram `#` och `*`.

För att få fram hakparenteser:
* På Mac: håll nere ALT och tryck på `(` för vänsterhake och `)` för högerhake.
* På Windows: håll nere ALT-GR och tryck på `8` för vänsterhake och `9` för högerhake.

För att få fram krullparenteserna:
* På Mac: håll nere *både* SKIFT och ALT och tryck på `(` för vänsterkrulle och `)` för högerkrulle.
* På Windows: håll nere ALT-GR och tryck på `7` för vänsterkrulle och `0` för högerkrulle.

Fungerar inte detta? Prova dig fram, eller fråga eller googla.



# Mer information

* [Python cheatsheet](../../programming/python/CHEATSHEET.md) (Mer tips om hur du skriver python-kod.)
* [Dokumentation för Python 2.7's turtle-bibliotek](https://docs.python.org/2/library/turtle.html)
