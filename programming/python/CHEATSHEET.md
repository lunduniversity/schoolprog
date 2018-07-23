---
title: Snabbreferens för Python
layout: page
toc: true
permalink: /cheatsheet/python/
---

## Kommentarer
```python
# Detta är en kommentar.
```

## Variabler, tilldelning och utskrift

```python
x = 10    # variabeln x får värdet 10
print(x)  # talet 10 skrivs ut i terminalfönstret
x = "hej" # variabeln x får ett nytt värde: texten "hej"
print(x)  # texten "hej" skrivs ut i terminalfönstret
```

## Typer
Varje värde har en *typ*, t.ex. sträng (string), heltal (integer), decimaltal (float)
eller logiskt värde (boolean).

```python
a = 1        # a är nu ett heltal med värdet 1
a = "1"      # a är nu en sträng med värdet "1"
a = int("1") # strängen "1" konverteras till heltalet 1
a = str(1)   # heltalet 1 konverteras till strängen "1"
a = float(1) # heltalet 1 konverteras till decimaltalet 1.0
a = 1/1      # resultatet av divisionen är decimaltalet 1.0
a = 1<2      # resultatet av mindre-än-operationen är True
```

Notera att `int("hej")` kommer att krascha programmet.
`int` och `float`-funktionerna förväntar sig strängar som kan tolkas som tal.

## Aritmetiska uttryck

```python
x0 = 1 + 1   # addition:        x0 == 2
x1 = 1 - 1   # subtraktion:     x1 == 0
x2 = 2 * 3   # multiplikation:  x2 == 6
x3 = 13 / 5  # division:        x3 == 2.6
x4 = 13 // 5 # heltalsdivision: x4 == 2 (största heltalet <= 13/5)
x5 = 13 % 5  # rest:            x5 == 3 (13 - (13//5))
x6 = 2 ** 3  # upphöjt till:    x6 == 8 (2^3).
```
Många matematiska funktioner, som `sin` och `sqrt` (square root, d.v.s. roten ur)
finns i `math`-paketet.
```python
import math

print(math.sqrt(4)) # skriver ut 2
```

## Logiska uttryck

```python
x = 1
y = 2
# Jämförelser
print(x == y) # lika med                  (False)
print(x != y) # inte lika med             (True)
print(x < y)  # mindre än                 (True)
print(x > y)  # större än                 (False)
print(x <= y) # mindre än eller lika med  (True)
print(x >= y) # större än eller lika med  (False)
```

```python
a = 1 < 2      # True
b = 1 > 2      # False
# Booleska operatorer
print(not a)   # Negation    (icke a)
print(a and b) # Konjunktion (a och b)
print(a or b)  # Disjunktion (a eller b)
```

## Strängkonkatenering

Lägg ihop strängar till en längre sträng.
```python
a = "hej"
b = "dig"
print(a + " på " + b) # Skriver ut "hej på dig"
```

## Inläsning och utskrift

Läs in en sträng och använd i utskrift:

```python
name = input("Vad heter du? ")
print("Hej " + name + "!")
```

Läs in ett heltal och använd i utskrift:

```python
ar = int(input("Hur gammal är du? "))
print("Då är du " + str(ar+1) + "om ett år!")
```

## Villkorssatser (if-sats, alternativ)

Gör olika saker beroende på logiska värdet hos ett uttryck:

```python
# Enkel if-sats
if a < 10:
    print("a är mindre än 10")
```

```python
# If-else-sats
if a < 10:
    print("a är mindre än 10")
else:
    print("a är lika med eller större än 10")
```

```python
# If-sats med många villkor
if a < 10:
    print("a är mindre än 10")
elif a == 10:
    print("a är lika med 10")
elif a == 11:
    print("a är lika med 11")
else:
    print("a är större än 11")
```


## Repetition (iteration, loop)

### For-loop

Repetera ett bestämt antal gånger.

Skriv ut orden i listan med stora bokstäver:

```python
for ord in ["hej", "på", "dig"]:
  print(ord.upper())
```

Skriv ut de 4 första talen från och med noll,
dvs 0, 1, 2, 3:
```python
for i in range(4):
  print(i)
```

Gå igenom de 10 första naturliga talen och skriv ut de som är udda:
```python
for i in range(10):
    if i%2 == 1:
        print(i)
```

### While-loop

Repetera så länge ett villkor är True:
```python
losenord = "sesam"
forsok = ""
raknare = 0
while forsok != losenord:
  forsok = input("Skriv lösenordet för att komma in: ")
  raknare += 1
print("Bravo! Du behövde " + str(raknare) + " försök för att gissa rätt.")
```

## Funktioner (abstraktion)

Med en funktion kan du återanvända en beräkning flera gånger. Genom att ge funktionen parametrar kan du anpassa vad funktionen gör eller räknar ut.

Enkel funktion utan parametrar:

```python
def skriv_ut_5_udda_tal():
  for i in range(5):
    print(i*2+1)
```

Funktion med parameter:
```python
def skriv_ut_udda_tal(n):
  for i in range(n):
    print(i*2+1)
```

Funktion med två parametrar och som returnerar värde:
```python
def triangel_area(bas, hojd):
  return bas * hojd / 2
```

Anrop av funktionerna:
```python
skriv_ut_5_udda_tal()
skriv_ut_udda_tal(7)
a = triangel_area(5, 8)
print("Arean är: " + str(a))
```

## Indentering
Python använder *indentering* (blanktecken i början på raden) för att tolka strukturen hos sammansatta konstruktioner som if, for, och funktionsdefinitioner.

Det är viktigt att delarna i en struktur har *samma* indentering. Oftast används 4 blanktecken. Men ibland 2.

```python
# Fel indentering inuti if-satsen
if x > 1:
  print(x)
    print(x + 2)
```
```python
# Korrekt indentering
if x > 1:
  print(x)
  print(x + 2)
```

## Listor

Bygg en enkel lista:

```python
lista = [1, 2, 3]
print(lista)
```

Gör något med varje tal i listan:

```python
lista = [1, 2, 3]
for nummer in lista:
    print(nummer * 2)
```

Bygg en lista med de första `n` heltalen och summera dem.

```python
n = 100
lista = list(range(n))
print(sum(lista))
```

## Debugging

Försäkra dig om att ett villkor är sant. Om det inte är sant kommer programmet att krascha.

```python
assert True        # Fungerar fint
assert 3 * 2 == 6  # Fungerar fint
assert 1 + 1 == 3  # Kommer att krascha programmet
```

## Konventioner

### Mer lättläst med blanktecken

Använd blanktecken och blankrader för att göra koden tydligare.

Blanktecken mellan operatorer:
```python
# Mindre lättläst:
x=x+1
```
```python
# Mer lättläst:
x = x + 1
```

Men om man har operatorer med olika prioritet kan man ta bort blanka mellan de med högst prioritet:
```python
x = a*b + c*d
```

Blankrader efter importer och mellan funktionsdefinitioner:
```python
# Mindre lättläst:
import math
def cirkel_area(r):
  return math.pi*r**2
def cirkel_omkrets(r):
  return 2*math.pi*r
print(cirkel_area(3))
print(cirkel_omkrets(4))
```

```python
# Mer lättläst:
import math

def cirkel_area(r):
  return math.pi * r**2

def cirkel_omkrets(r):
  return 2 * math.pi * r

print(cirkel_area(3))
print(cirkel_omkrets(4))
```

### Beskrivande namn

Namnge variabler och parametrar så det är lätt att förstå vad de representerar.

Namnge funktioner så det är lätt att förstå vad de gör.

```python
# Dålig namngivning:
def min_utrakning(x):
  y = math.pi * x**2
  return y
```
```python
# Bra namngivning:
def cirkel_area(r):
  area = math.pi * r**2
  return area
```

### `_` i långa funktionsnamn

Vid långa namn på funktioner och variabler, använd understrykningstecken, `_`, mellan orden. (I flera andra språk används "camel case".)

```python
# "camel case" är inte så vanligt på funktioner i Python:
def cirkelArea(r):
  ...
```
```python
# I stället rekommenderas `_` mellan orden i ett långt funktionsnamn:
def cirkel_area(r):
  ...
```

### Funktionsnamn börjar på liten bokstav

Namn på funktioner och variabler brukar börja på liten bokstav:

```python
# Inte rekommenderat:
def Cirkel_area(r):
  ...
```
```python
# Rekommenderat:
def cirkel_area(r):
  ...
```
