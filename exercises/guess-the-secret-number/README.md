---
layout: page
title: Guess the secret number
permalink: /exercises/guess-the-secret-number/
toc: true
type: exercise
---

Skriv ett programn som väljer ett slumpmässigt nummer och låter dig gissa
fram till vilket.

## Instruktioner

Det kommer gå till ungefär såhär:

1. Randomisera ett nummer: För att kunna få Python att ge dig ett slumpnmässigt nummer måste du först importera paketet 'random' som innehåller metoden 'randint()'. Detta gör du genom att kopiera följande kod i din "editor" (textredigerare):

 ```python
 from random import randint

 # Genererar ett nummer mellan 0 och 10 och tilldelar detta nummer till variablen 'random_number'. Variablen kommer vara ditt hemliga nummer som du ska försöka gisa dig fram till. Kan du redan nu komma på ett effektivt sätt för att gissa så få antal gånger som möjligt?
 random_number = randint(0, 10)
```


{:start="2"}
 2. Nu vill du skriva kod som ber dig att gissa ett nummer inom det intervall du angav när du genererade ett slumpmässigt nummer till 'random_number. Kopiera följande kod till din editor:

```python
# Läser in input från tangentbordet och gör om detta till typen 'integer', därefter tilldelas numret till variabeln 'guessed_number'.
guessed_number = int(input("Write something here!"))
```

{:start="3"}
 3. Du vill ha möjligheten att kunna fortsätta gissa så länge guessed_number inte är samma värde som random_number. För att åstadkomma detta kan du använda något som kallas 'while-loop', är du osäker på detta kan du läsa mer i [cheatsheetet](../../cheatsheet/python/). Kolla in följande kod exempel och försök lista ut hur du kan använda satsen för ditt eget program:

```python
a = 10
b = 13

# Denna rad av kod under while-blocket kommer att fortsätta upprepas tills satsen inte längre är uppfylld. Eftersom att 10 inte är 13 så kommer koden att upprepa sig själv. 
while a != b:
    b = int(input("Assign a new value to b with new input"))
```

{:start="4"}
 4. Det är svårt att bara slumpmässigt gissa nummer, beroende på hur omfattande intervallet är kan det ta otroligt mycket tid. Det skulle underlätta med någon form utav återkoppling, t.ex. om talet som gissades är för lågt eller för högt. För att göra detta kan du utnyttja en 'if-sats' inuti din while-loop. Titta på följande exempel:
 
```python
a = 10
b = 13
 
while a != b:
    if a < b:
        b = int(input("Try a lower number!"))
    if a > b:
        b = int(input("Try a higher number!"))
```
 
{:start="5"}
 5. Någon form av återkoppling för när du faktiskt lyckas gissa rätt nummer är också viktigt. Annars kan det vara svårt att veta när du kommit ut ur while.loopen. Du kan testa detta kommande efter din while-loop:
 
```python
print("Here you can write whatever you want and it will show in the terminal!")
```
  
## Extra

Skriv ett program som baserat på ett givet nummer och ett intervall mellan 0-100 hittar korrekt värde på minimalt antal försök genom binärsökning. 

Exempel:

```
IN      >>> 10
OUT     6

IN      >>> 50
OUT     1
```

*Binary search:*
https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm

