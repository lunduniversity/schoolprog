---
title: Turtle graphics (Sköldpaddsgrafik)
toc: true
layout: page
type: exercise
tags:
 - nybörjare
 - grafiskt
 - funktioner
permalink: /exercises/turtle/
cover_image: https://i.imgur.com/YHHBJaS.png
cover_y_offset: 25%
---

Vill du rita snygga & coola saker med en programmerbar sköldpadda? Då är detta uppdraget för dig!

# Komma igång

Börja med att öppna online-miljön för [Python-turtle](https://repl.it/languages/python_turtle)

# Sekvens

Vi börjar med att låta paddan göra några saker i *sekvens*. Här är ett enkelt exempel där paddan går en liten tur:

```python
import turtle

t = turtle.Turtle()
t.color("red")

t.forward(75)
t.left(90)
t.forward(100)
t.right(90)
```

Kör programmet och se vad som händer. Kan du lista ut vad varje rad gör? Prova att ändra några värden och se hur beteendet förändras.

**Uppdrag rektangel:** Kan du få paddan att rita en rektangel?

*Tips!* Om du tycker paddan ritar för långsamt, lägg till ett anrop `t.speed(10)` för att rita snabbare.


# Repetition

Ibland vill vi låta paddan *repetera* en sekvens av saker. Här är ett enkelt exempel där sköldpaddan repeterar en liten sekvens med hjälp av en *for-loop*.

```python
import turtle

t = turtle.Turtle()
t.color("blue")

for c in range(3):
  t.forward(25)
  t.left(90)
  t.forward(20)
  t.right(90)
```
Prova programmet och se vad som händer. Prova att ändra olika saker i programmet. Kan du få paddan att repetera fler gånger? Kan du rita en annan slags figur genom att ändra innehållet i for-loopen?

**Uppdrag kvadrat:** Kan du rita en kvadrat på ett smart sätt med hjälp av en for-loop?

<details>
  <summary markdown="span">
    Tips
  </summary>
  <pre>
for c in range(4):
  t.forward(75)
  t.left(90)
  </pre>
</details>

Variabeln `c` i for-loopen är ett heltal som ändrar värde för varje varv i loopen. Prova att se vad värdet på loop-variabeln är genom att lägga till

```python
t.write(c)
```
inuti loopen.

**Uppdrag spiral:** Kan du rita en fyrkantig spiral på ett smart sätt genom att använda `c` för att låta paddan gå lite längre efter varje sväng?

<details>
  <summary markdown="span">
    Tips
  </summary>
  <pre>
for c in range(16):
  t.forward(75+10*c)
  t.left(90)
  </pre>
</details>


# Funktioner

Genom att definiera en funktion kan du göra egna byggblock som du kan använda på flera ställen.

Här definierar vi en funktion som ritar en liten vimpel:

```python
def vimpel() :
  t.forward(100)
  t.right(100)
  t.forward(40)
  t.right(160)
  t.forward(40)
  t.right(100)
```

Vi kan sedan prova att rita ut vimpeln på flera ställen. För att hoppa till olika ställen får vi be paddan dra upp sin penna.

```python
t.setheading(90)
vimpel()
t.right(120)
t.penup()
t.forward(70)
t.pendown()
t.left(120)
vimpel()
```

**Uppdrag myfig:** Kan du göra en funktion som ritar en enkel figur? T.ex. bokstaven L, eller något du hittar på själv. Prova att rita ut den på flera ställen. Funktionen skall vara *rotationsneutral*, dvs på slutet av funktionen skall paddan ha samma riktning som i början.



# Funktion med parameter

Genom att ge en funktion parametrar blir den mer användbar.

För att få paddan att hoppa kan vi t.ex. definiera följande funktion:

```python
def hop(length) :
  t.penup()
  t.forward(length)
  t.pendown()
```

Nu kan paddan hoppa, dvs gå framåt utan att rita. Prova med t.ex.

```python
t.forward(20)
hop(10)
t.forward(20)
hop(10)
t.forward(20)
```

**Uppdrag skalbar figur:** Ändra din funktion `myfig` så den tar en parameter `height` som representerar höjden på figuren. Rita alla delar skalenligt. Låt `100` motsvara att figuren ritas ut i skala 1:1. Anropa din funktion med olika värden på `height`.

<details>
  <summary markdown="span">
    Tips
  </summary>
Multiplicera sträckor med <code>height</code> och dividera med 100. Dvs i stället för att skriva <code>forward(60)</code>, skriv <code>forward(60*height/100)</code>.
</details>

Det kan vara praktiskt att en funktion är *rotations-* och *positionsneutral*, dvs att efter du har anropat funktionen så är sköldpaddans position och riktning oförändrad. Detta kan du åstadkomma genom att spara positionen och riktningen innan du ritar, och återställa dem efteråt:

```python
p = t.position()
h = t.heading()
... # rita
t.setposition(p)
t.setheading(h)
```

**Uppdrag neutral figur:** Ändra din funktion `myfig` så den blir rotations- och positionsneutral.

**Uppdrag decor:** Skriv en funktion `decor` som anropar `myfig` några gånger för att få ett intressant mönster. Prova med olika vinklar, olika storlekar och olika positioner. Du kan använda loopar och extra funktioner om du vill.




<!--

# Alternativ

TODO - någon övning på if-satser


# Tårta

TODO - en övning för att göra en funktion som ritar en tårta som har en färg för kanten och en för innehållet, och som kan placeras i antingen x eller y-led (så man kan rita flera tårtor bredvid varandra). Att användas i Piece-of-cake-uppdraget.

# Rita en blomma

TODO - en övning för att göra en funktion som ritar en liten enkel blomma. Ge funktionen x o y-parametrar så man kan dekorera tårtan genom att rita blommor på den. Att användas i Piece-of-cake-uppdraget.

# Rita koordinataxlar

TODO - övning för att göra en funktion som ritar en x och en y-axel. Att användas senare i uppdrag om att rita matematiska funktioner.

# Färgglad sköldpadda

Kör följande i varje steg i loopen (glöm inte att lägga till `import random` längst upp i filen!)

```py
t.color(random.choice(['red', 'green', 'magenta', 'orange', 'blue']))
```

-->
