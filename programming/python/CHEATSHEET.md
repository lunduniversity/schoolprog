---
title: Snabbreferens för Python
layout: page
toc: true
permalink: /cheatsheet/python/
---

Denna snabbreferens innehåller vanliga konstruktioner för Python 3.6. För mer information, se t.ex. [The Python Tutorial](https://docs.python.org/3.6/tutorial/index.html).

## Kommentarer
```python
# Detta är en kommentar.
x = 1 # Kommentaren fortsätter till radens slut
```

## Variabler, tilldelning och utskrift

```python
x = 10    # variabeln x får värdet 10
print(x)  # talet 10 skrivs ut i terminalfönstret
x = "hej" # variabeln x får ett nytt värde: texten "hej"
print(x)  # texten "hej" skrivs ut i terminalfönstret
```

## Typer och värden

### Typer
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

Ta reda på typen för ett värde med funktionen `type`:
```python
x = ...
print(type(x))
```

### Aritmetiska uttryck

```python
x0 = 1 + 1   # addition:        x0 == 2
x1 = 1 - 1   # subtraktion:     x1 == 0
x2 = 2 * 3   # multiplikation:  x2 == 6
x3 = 13 / 5  # division:        x3 == 2.6
x4 = 13 // 5 # heltalsdivision: x4 == 2 (största heltalet <= 13/5)
x5 = 13 % 5  # rest:            x5 == 3 (13 - (13//5))
x6 = 2 ** 3  # upphöjt till:    x6 == 8 (2^3).
```




### Logiska uttryck

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

### Prioriteter
Operatorer har olika prioritet som bestämmer hur ett uttryck med flera operatorer tolkas. T.ex. har `**` högre prioritet än `*` och `/`, som i sin tur har högre prioritet än `+` och `-`.

Till exempel tolkas `a + b * c` som `a + (b * c)`, och inte som `(a + b) * c`. Om det var den senare tolkningen du ville ha så måste du skriva parenteserna.

De aritmetiska operatorerna har högre prioritet än jämförelseoperatorerna, som i sin tur har högre prioritet än de Booleska operatorerna. Bland de Booleska operatorerna har `not` högst prioritet, sedan `and`, sedan `or`.

Till exempel tolkas `not a and b or c` som `((not a) and b) or c`.

Är du tveksam om vilka prioriteter operatorerna har, så kan du alltid skriva ut parenteserna.


### Strängkonkatenering

Lägg ihop strängar till en längre sträng.
```python
a = "hej"
b = "dig"
print(a + " på " + b) # Skriver ut "hej på dig"
```

### Stränginterpolering
Sätt ihop en sträng som innehåller tal. Sätt ett litet `f` framför strängen så kan man spränga in tal i strängen genom att omgärda talen med `{}` parenteser.
```python
a = 18
b = 13
print(f"Klockan är {a}:{b}.")
```
Samma resultat kan åstadkommas med typomvandling och konkatenering, men då blir koden lite krångligare:
```python
a = 18
b = 13
print("Klockan är " + str(a) + ":" + str(b) + ".")
```

## Standardbiblioteket

[Standardbiblioteket](https://docs.python.org/3.6/library/index.html) i Python innehåller många användbara paket med funktionalitet.

### Math-paketet
Många matematiska funktioner, som `sin` och `sqrt` (square root, d.v.s. roten ur)
finns i `math`-paketet.
```python
import math

print(math.sqrt(4)) # skriver ut 2
```

### Random-paketet
```python
import random

k = random.randint(1,6) # Dra ett slumptal mellan 1 och 6.
```

Om det är bara en funktion man vill ha i ett bibliotek kan den importeras så att man kommer åt den direkt:

```python
from random import randint

k = randint(1,6) # Dra ett slumptal mellan 1 och 6.
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
print("Då är du " + str(ar+1) + " om ett år!")
```

## Sammansatta konstruktioner

### Villkorssatser (if-sats, alternativ)

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
    print("a är större än eller lika med 10")
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


### Repetition (iteration, loop)

#### For-loop

Repetera ett bestämt antal gånger.

Omvandla orden i listan till stora bokstäver och skriv ut dem.

```python
for ord in ["hej", "på", "dig"]:
  print(ord.upper())
```

Skriv ut de 4 första naturliga talen,
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

#### While-loop

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

### Funktioner (abstraktion)

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

### Indentering

Python använder *indentering* (blanktecken i början på raden) för att tolka strukturen hos sammansatta konstruktioner som if, for, och funktionsdefinitioner.

Det är viktigt att delarna i en struktur har *samma* indentering. Oftast används 4 blanktecken. Men ibland 2.

```python
# Fel: de inre satserna har olika indentering.
if x > 1:
  print(x)
    print(x + 2)
```
```python
# Rätt: de inre satserna har samma indentering.
if x > 1:
  print(x)
  print(x + 2)
```

När sammansatta konstruktioner nästlas inne i varandra ökar man antalet blanka för varje nivå. Exempel:

```python
for x in range(5): # första FOR
  print("x = " + str(x))
  if x%2 == 1:       # IF nästlad inuti första FOR
    print("x är udda")
    for y in range(7): # ny FOR nästlad inuti IF
      print("y = " + str(y))
      if y%2 == 1:       # ny IF nästlad inuti andra FOR
        print("Både x och y är udda")
  else:              # hör till första IF
    print("x är jämn")
print("Beräkningen är färdig.")
```

## Sammansatta datatyper
### Lista

Listor är ordnade. Elementen i listan är oftast av *samma* typ. Samma värde kan finnas på flera ställen i listan.

Exempel: Löpande band med frukter

```python
lopande_band = ["äpple", "päron", "apelsin", "äpple"]
print(lopande_band)        # Skriv ut hela listan
print(lopande_band[0])     # Skriv ut det första elementet
lopande_band[2] = "citron" # Ändra tredje elementet
lopande_band.append("persika") # Lägg till ett element sist
print(lopande_band)        # Skriv ut listan igen
```

Gör något med varje element i listan:

```python
for frukt in lopande_band:
    print("Nu kom det en frukt av typ: " + frukt)
```

#### Listbyggare (list comprehension, listomfattning)

Skapa en lista som omfattar vissa värden.

Exempel: Givet det löpande bandet ovan, skapa en lista med fruktnamn omvandlat till stora bokstäver, men bara för de frukter som börjar på `p`. T.ex. från listan ["äpple", "päron", "citron", "äpple", "persika"] vill vi få en lista ["PÄRON", "PERSIKA"].

```python
stora_p = [p.upper() for p in lopande_band if p[0]=="p"]
```
Ovanstående är ekvivalent med:
```python
stora_p = [] # Tom lista
for p in lopande_band:
  if p[0]=="p":
    stora_p.append(p.upper())
```

### Tupel

Tupler är ordnade och kan *inte* ändras (de är immutable). De används ofta för att gruppera data som hör ihop och som kan vara av *olika* typer.

```python
person = ("Stina", 14, "Lund") # Person med namn, ålder och ort
punkt = (3, 5) # Punkt med x- och y-koordinat
```
Man kan plocka ut elementen i en tupel med indexering:

```python
namn =  person[0] # Plocka ut första elementet
alder = person[1] # Plocka ut andra elementet
ort =   person[2] # Plocka ut tredje elementet
```
Men det är ofta trevligare att plocka ut elementen genom att "packa upp" tupeln:
```python
namn, alder, ort = person
x, y = punkt
```

En vanlig användning är när man vill att en funktion skall returnera mer än ett resultat:

```python
def spegla_i_x_axeln(p): # spegla punkt i x-axeln
  x, y = p
  return -x, y

sx, sy = spegla_i_x_axeln(punkt)
```


### Mängd (set)

Mängder är *oordnade*. Det spelar inte någon roll i vilken ordning vi lägger till saker i en mängd. Om vi försöker lägga till ett värde som redan finns, så ändras inte mängden.

```python
frukter_1 = {"äpple", "päron", "persika"}
frukter_2 = {"päron", "äpple", "persika"}
assert frukter_1 == frukter_2 # Mängderna är lika
frukter_2.add("äpple")
assert frukter_1 == frukter_2 # Mängderna är fortfarande lika
```

Vi kan iterera över elementen i en mängd:
```python
for f in frukter_1:
  print(f)
```

#### Mängdbyggare (set comprehension)

Vi kan bygga en mängd på liknande sätt som vi bygger en lista.

Exempel: Skapa mängd av fruktnamn som har högst sex tecken.
```python
korta_fruktnamn = [f for f in frukter_1 if len(f)<=6]
```


### Nyckel-värdetabell (mappning, dictionary, lexikon)

En nyckel-värdetabell är en mappning från en nyckel till ett värde. Med hjälp av en nyckel kan vi slå upp värdet för nyckeln.

Exempel: volleybollföreningens inventarieförteckning:

```python
inventarier = {"boll":17, "vattenflaska":10, "matchtröja":18}

inventarier["boll"] = 18  # Ändra värdet för nyckeln "boll"
inventarier["pokal"] = 28 # Sätt värde för nyckeln "pokal"

# Slå upp ett värde
pokaler = inventarier["pokal"]
print("Vi har " + str(pokaler) + " pokaler")
```


## Assert-satser

En assert-sats används för att kontrollera om ett villkor är sant. Om det inte är sant kommer programmet att krascha.


```python
assert True        # Fungerar fint
assert 3 * 2 == 6  # Fungerar fint
assert 1 + 1 == 3  # Kommer att krascha programmet
```

Exempel på användning: Kontrollera att en funktion bara anropas med positiva tal:

```python
def kelvin_till_celsius(k):
  assert k >= 0
  return k - 273.15
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

### långa`_`funktionsnamn

Vid långa namn på funktioner och variabler, använd understrykningstecken, `_`, mellan orden. (I flera andra språk är det i stället vanligt med "camel case".)

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
