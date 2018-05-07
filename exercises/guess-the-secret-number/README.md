---
layout: page
title: Gissa det hemliga numret
permalink: /exercises/guess-the-secret-number/
toc: true
type: exercise
tags:
 - medel
 - spel
 - slump
 - intervallhalvering
 - text
---

<!--**Note:** This exercise is also available [in english](README_EN.md).-->

Här skriver vi ett litet spel där programmet väljer ett slumpmässigt tal och låter dig gissa dig fram till vilket talet är.

Koden i denna uppgift är provkörd på [http://repl.it/languages/python3](http://repl.it/languages/python3) (Python 3).

## 1. Gissa en gång

Vi börjar med att programmet låter dig gissa en enda gång. Programmet skall alltså:

 * skapa ett slumptal
 * skriva ut vilka gränser talet ligger mellan
 * låta dig gissa ett tal
 * kontrollera om du gissat rätt
 * skriva ut vilket slumptalet var

Nedan visar vi vilka byggblock du behöver:

Använd `random` för att dra ett slumptal:
```python
# Skapa ett slumptal mellan 1 och 3
from random import randint
random_number = randint(1, 3)
```

Använd `print` för att skriva ut något:
```python
print("Jag tänker på ett tal mellan 1 och 3")
```

Använd `input` för att läsa in ett tal med en ledtext:
```python
# Låt programmet be dig gissa ett tal.
# Det du svarar hamnar i variabeln "guess"
guess = int(input("Gissa vilket tal jag tänker på!"))
```

Använd en `if`-sats för att kontrollera ett villkor:
```python
# Låt programmet kontrollera om du gissat rätt.
if guess == random_number:
  print("Snyggt jobbat! Det var rätt!")
else:
  print("Tyvärr, det var fel.")
```

Använd `str` för att göra om ett tal till en sträng och `+` för att slå ihop två strängar till en:
```python
print("Jag tänkte på " + str(random_number))
```


**Uppdrag:** Sätt ihop byggblocken till ett program. Provkör det några gånger och se om du kan gissa rätt tal. Lyckas du gissa rätt?

## 2. Gissa flera gånger

För att göra programmet lite mer spännande skall vi ändra det så du kan gissa flera gånger. I stället för att använda en `if`-sats skall vi använda en `while`-loop som ber om en ny gissning tills du svarat rätt.

Du kan använda följande byggblock med en while-loop:

```python
found = False
while not found:
  guess = int(input("Gissa vilket tal jag tänker på!"))
  if guess == random_number:
    print("Snyggt jobbat! Det var rätt!")
    found = True
  else:
    print("Tyvärr. Det var fel.")
```

**Uppdrag:** Gör om programmet så att du får gissa flera gånger. *Tips:* Byt ut `if`-satsen mot en `while`-loop enligt ovan. Provkör ditt program så du ser att det fungerar. Hur många gånger behöver du gissa innan du gissar rätt?

## 3. Gissa med återkoppling
Det är svårt att bara slumpmässigt gissa nummer. Om intervallet är lite större, t.ex. mellan 1 och 100 kan det ta otroligt mycket tid.

Det skulle underlätta om programmet gav dig återkoppling och berättade om talet du gissade var för högt eller för lågt. Det kan du göra genom att bygga ut `if`-satsen enligt följande mönster:

Använd `elif` för att testa ytterligare ett villkor i en `if`-sats:
```python
if guess == random_number:
  print("Snyggt jobbat! Det var rätt!")
  stillGuessing = False
elif guess < random_number:
  print("Tyvärr. Det var för lågt.")
else:
  print("Tyvärr. Det var för högt.")
```

**Uppdrag:** Ändra programmet så att det ger dig återkoppling på om det gissade talet var för stort eller för litet. Ändra också gränserna så att du får gissa ett tal mellan 1 och 100. Provkör ditt program.

## 4. Räkna antalet gissningar

Du kan låta programmet hålla reda på hur många gissningar du gör. Det kan du göra genom att:

 * Införa en variabel `tries` som sätts till 0 i början av programmet.
 * Lägg till 1 till variabeln för varje gissning inuti while-loopen.
 * Skriv ut på slutet hur många försök det blev.

Här är byggblocken du behöver:

Lägg till en ny variabel som du sätter till 0:
```python
tries = 0
```

Öka en variabel med ett:
```python
tries += 1
```

Skriv ut variabeln:
```python
print("Du gjorde " + str(tries) + " gissningar!")
```

**Uppdrag:** Använd byggblocken ovan för att hålla reda på och skriva ut antalet gissningar. Prova ditt program.

**Uppdrag:** Fundera på hur du skall göra för att gissa rätt tal med så få gissningar som möjligt!

<details>
<summary markdown="span">
Kommentar:
</summary>
<p>Den bästa strategin är att gissa i mitten hela tiden! Börja alltså med att gissa på 50. Om det var för litet gissar du sedan på 75 (mitten av intervallet 50-100). Om det var för stort gissar du på 62 (mitten av intervallet 50-75), och så vidare. Detta kallas <i>intervall-halvering</i>.
</p>
</details>

## 5. Låt programmet gissa! (Utmaning!)

Vi kan undersöka hur många gissningar som behövs genom att låta programmet självt gissa med hjälp av intervallhalvering.

I stället för att programmet ska be oss om en gissning ska vi alltså låta det självt räkna ut en gissning!

För att programmera detta behöver vi en variabel `low` som håller reda på den lägre gränsen för intervallet och en annan `high` som håller reda på den högre gränsen. Vi börjar med att låta `low` vara 1 och `high` vara 101 (ett mer än 100), och flyttar sedan en av gränserna efter varje gissning.

En ny gissning kan då räknas ut som:
```python
guess = low + (high-low)//2
```
där `//` är heltalsdivision. (Heltalsdivision är som vanlig division, men avrundar nedåt till närmsta heltal. T.ex. är `7//2` lika med `3` i stället för `3.5`.)

Anledningen till att vi sätter high till 101 från början, och inte 100, är att gissningen annars aldrig kan bli 100, eftersom heltalsdivisionen alltid avrundar nedåt. Vi vill ju att programmet skall fungera även om slumptalet som dras råkar vara 100.

**Uppdrag:** Ändra så att programmet självt gissar med hjälp av intervallhalvering, och skriver ut hur många gissningar som behövdes. Här är ett exempel på output från en programkörning:

```
Slumptalet är: 78
Gissning: 50
Gissning: 75
Gissning: 88
Gissning: 81
Gissning: 78
Det behövdes 5 gissningar
```

## 6. Hur många gissningar behövs?
Som du kanske märkt verkar det som mest behövas 7 gissningar för att gissa ett tal mellan 1 och 100. Hur många gissningar tror du det behövs som mest för att gissa ett tal mellan 1 och 200?

**Uppdrag:** Ändra programmet så att det gissar ett tal mellan 1 och 200. Kör programmet några gånger. Hur många gissningar verkar behövas som mest?

<details>
<summary markdown="span">
Svar:
</summary>
<p>Det behövs bara en till: max 8 gissningar behövs.
</p>
</details>

**Uppdrag:** Ändra programmet så att det gissar ett tal mellan 1 och 1 miljard (1000000000). Hur många gissningar tror du kan behövas som mest? Provkör några gånger och se vad du får för resultat!

<details>
<summary markdown="span">
Svar:
</summary>
<p>Det behövs max 30 gissningar.
</p>
</details>

## 7. Lägg till en variabel för största talet
I stället för att skriva 100 eller 1 miljard på flera ställen i programmet är det praktiskt att införa en variabel. Då slipper du ändra på mer än ett ställe om du vill prova ett annat intervall.

**Uppdrag:** Lägg till en variabel `max_number` för det största talet som skall kunna dras. Snygga också till ditt program så det blir lättläst. Prova programmet med olika värden på `max_number`.
