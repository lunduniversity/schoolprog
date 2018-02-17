---
title: Turtle
toc: true
layout: page
type: exercise
tags:
 - nybörjare
 - grafiskt
 - funktioner
permalink: /exercises/turtle/
---

**Note:** This exercise is also available [in english](README_EN.md).

Vill du rita snygga & coola saker med en programmerbar sköldpadda? Då är detta uppdraget för dig!

# Komma igång

Börja med att öppna online-miljön för [*Turtle in Python*](https://repl.it/languages/python_turtle)

# Sekvens

Vi börjar med att låta paddan göra några saker i *sekvens*. Här är ett enkelt exempel där sköldpaddan går en liten tur:

```python
import turtle

t = turtle.Turtle()
t.color("red")

for c in range(4):
    t.forward(75)
    t.left(90)
```

Kör programmet och se vad som händer. Kan du lista ut vad varje rad gör? Prova att ändra några värden och se hur beteendet förändras.

Kan du få paddan att rita en rektangel?

# Rita fort

När vi ritar större saker vill vi kanske att paddan skall gå lite fortare.

TODO - visa hur man gör. Uppdrag att rita en blomma.

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

Kan du rita en kvadrat på ett smart sätt med hjälp av en for-loop?

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

Kan du rita en fyrkantig spiral på ett smart sätt genom att använda `c` för att låta paddan gå lite längre efter varje sväng?

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


# Alternativ

TODO - någon övning på if-satser

# Abstraktion

TODO - en övning på att göra en funktion. Först utan parameter. Sedan med parameter.

# Tårta

TODO - en övning för att göra en funktion som ritar en tårta som har en färg för kanten och en för innehållet, och som kan placeras i antingen x eller y-led (så man kan rita flera tårtor bredvid varandra). Att användas i Piece-of-cake-uppdraget.

# Rita en blomma

TODO - en övning för att göra en funktion som ritar en liten enkel blomma. Ge funktionen x o y-parametrar så man kan dekorera tårtan genom att rita blommor på den. Att användas i Piece-of-cake-uppdraget.

# Rita koordinataxlar

TODO - övning för att göra en funktion som ritar en x och en y-axel. Att användas senare i uppdrag om att rita matematiska funktioner.
