---
layout: page
title: Piece of cake
permalink: /exercises/piece-of-cake/
toc: true
type: exercise
tags:
 - nybörjare
 - bråk
 - grafiskt
---

<img src="finalcake.png" height="150">

Denna uppgift går ut på att illustrera heltalsbråk som delar av tårtor.

Innan du gör uppgiften bör du ha lite koll på "turtle graphics", t.ex. genom att göra uppgiften [Turtle](../turtle/README.md).

A: Tredjedelar och fjärdedelar
==============================

## Rita en tårta

Rita en avlång rektangulär tårta med "turtle graphics". Kanten på tårtan skall vara i en färg och den skall vara fylld med en annan färg. T.ex.:

<img src="cake.png" height="70">

Till din hjälp, deklarera en turtle som du kallar `t`:

```python
t = turtle.Turtle()
```
och klistra in följande funktioner i ditt script för att kunna hoppa till en given plats och för kunna att rita en fylld rektangel:

```python
# Jump to a position without drawing anything
def jumpTo(x,y):
  t.penup()
  t.setx(x)
  t.sety(y)
  t.pendown()
```
```python
def drawFilledRect(width, height):
  t.setheading(0)
  t.fill(True)
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.fill(False)
```
Tips: Så här kan du sätta pennbredden, pennfärgen, och fyllningsfärgen:

```python
  t.width(3)            # Sätt bredden på pennan
  t.color('green')      # Sätt färgen på pennan
  t.fillcolor('red')    # Sätt fyllningsfärgen
```

**Uppdrag:** Rita tårtan! Prova med olika färger, t.ex. `blue`, `violet`, `pink`, `gold`, `orange`, `brown`. [Här](https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm) finns en lista på fler färger som kan användas.

## Rita två tårtor

**Uppdrag:** Rita två tårtor snyggt placerade bredvid varann. Tårtorna skall vara lika stora. T.ex. så här:

<img src="twocakes.png" height="130">


## Extra: snygga till tårtorna

**Uppdrag:** Om du tycker om snygga tårtor, skriv kod som dekorerar dem. Kanske med en ros i mitten på varje tårta?

## Skär upp tårtorna

Nu ska vi skära upp tårtorna.

Till din hjälp, klistra in följande funktion i ditt script.

```python
# Slice a rectangle in a number of pieces
def sliceRect(width, height, pieces):
  savex = t.xcor() # Save current turtle x-position
  savey = t.ycor() # Save current turtle y-position
  pieceWidth = float(width)/pieces
  for i in range(pieces-1):
    t.penup()
    t.setheading(0)
    t.forward(pieceWidth)
    t.right(90)
    t.pendown()
    t.forward(height)
    t.penup()
    t.backward(height)
  t.setpos(savex, savey) # Restore turtle position

```

Funktionen `sliceRect` skär upp en rektangel i ett antal lika stora bitar genom att rita streck över rektangeln.

**Uppdrag:** Skär upp översta tårtan i tredjedelar och nedersta tårtan i fjärdedelar. Använd en annan färg till snitten än du hade tidigare. Den tredelade tårtan borde se ut ungefär så här:

<img src="cutcake.png" height="70">

*Obs!* Du måste positionera paddan rätt innan du anropar funktionen, och du måste anropa den med samma bredd och höjd som du ritade rektanglarna med tidigare.

*Tips:* Går det långsamt att rita? Du kan ställa in hastigheten på paddan så här:

```python
t.speed(0)   # Rita så fort som möjligt
```


## Ät tårta

Nu skall vi illustrera att du äter en bit av den ena tårtan och en bit av den andra.

**Uppdrag:** Färga tårtbiten längst till vänster på vardera tårtan. Resultatet borde bli ungefär så här för den tredelade tårtan:

<img src="eatencake.png" height="70">

*Tips*: Anropa `drawFilledRect` med en tredjedel av bredden för den första tårtan och en fjärdedel av bredden för den andra tårtan. Till exempel så här:

```python
w = ... # the width of a full cake
h = ... # the height of a full cake
drawFilledRect(w/3, h)
```

## Hur mycket har du ätit?

Nu har du ju ätit 1/3 tårta plus 1/4 tårta. Hur mycket tårta blir det sammanlagt?

Om vi hade delat varje tårta i tolftedelar (delbart med både 3 och 4), så hade vi lätt kunnat se hur mycket tårta det blir.

Nu skall vi illustrera detta. Till din hjälp, klistra in följande funktion:

```python
# Slice each piece into a number of slices
def slicePieces(width, height, pieces, slices):
  savex = t.xcor()
  savey = t.ycor()
  pieceWidth = float(width)/pieces
  for p in range(pieces):
    sliceRect(pieceWidth, height, slices)
    t.penup()
    t.setheading(0)
    t.forward(pieceWidth)
  t.setpos(savex, savey)
```

Denna funktion skär upp en tårta som redan är delad i `pieces` bitar, så att varje bit delas ytterligare i `slices` delar.

**Uppdrag:** Skär upp de båda tårtorna i tolftedelar.

*Tips:* Anropa `slicePieces` så du skär upp bitarna i den tredelade tårtan i fjärdedelar och bitarna i den fyra-delade tårtan i tredjedelar. Den tredelade tårtan borde nu se ut så här:

<img src="slicedcake.png" height="70">

**Quiz:** Hur många tolftedelar tårta är uppätna totalt?

<details>
  <summary markdown="span">
    Svar
  </summary>
  <p>
  7
  </p>
</details>


B: Godtyckliga tårtbitar
========================

## Generalisera programmet

Ditt program illustrerar hur

     1     1       7
    ––– + –––  =  ––––
     3     4       12

Vi skall nu generalisera programmet så att du kan prova med andra bråk.

*Tips:* Spara en kopia av ditt fungerande program innan du börjar ändra något.

**Uppdrag:** Kapsla in koden för att rita, dela, äta, och skära tårtorna i en ny funktion `showFractionAdd(n,m)` så att du kan anropa den för att illustrera ekvationen:

     1     1       n+m
    ––– + –––  =  ––––-
     n     m       n*m

Om du t.ex. anropar `showFractionAdd(2,5)` så skall du få följande resultat:

<img src="showFractions.png" height="130">

*Tips:* Börja med att lägga in din kod i den nya funktionen, och att den fungerar när du anropar den med `showFractionAdd(3,4)`. Generalisera sedan funktionen så att den använder parametrarna `n` och `m` i stället för `3` och `4`.

## Lägg till ekvationen

**Uppdrag:** Utöka koden i `showFractionAdd` så att den skriver ut ekvationen under tårtorna. När du nu anropar `showFractionAdd(2,5)` så skall du få följande resultat:

<img src="finalcake.png" height="150">

*Tips:* Här är lite kod du kan använda för att skriva ut ekvationen:

```python
s1 = "1/"+str(n)
s2 = "1/"+str(m)
s3 = str(n+m)+"/"+str(n*m)
s4 = s1 + " + " + s2 + " = " + s3
t.write(s4, font=("Arial", 12, "normal"))
```
## Testa olika tårtbitar

Prova din funktion med olika värden på `n` och `m` för att räkna ut `1/n + 1/m`. Kontrollera t.ex. att
* 1/2 + 1/5 = 7/10

**Uppdrag:** Prova fler exempel. T.ex.:

* 1/3 + 1/4 = 7/12
* 1/5 + 1/7 = 12/35

Fungerar programmet bra för alla exempel? Vilka exempel kan du komma på som verkar intressanta att testa?
<details>
  <summary markdown="span">
    Tips
  </summary>
  <p>
  <ul>
    <li>Låt n eller m vara lika med 1
    <li>Låt n eller m vara lika med 0
    <li>Låt n eller m vara negativt
    <li>Prova med större värden
    <li>Prova med värden som har gemensamma faktorer, t.ex. n=2 och m=4
  </ul>
  </p>
</details>

Fungerade programmet bra för alla exemplen? Kanske det kan förbättras?

C: Snitta tårtorna smartare
===========================

Hur hanterar ditt program fallet med `n=2` och `m=4`? Skärs tårtorna upp med onödigt många snitt? För detta exempel borde det räcka att snitta tårtorna i fjärdedelar. Men ditt program kanske snittar dem i åttondelar?

Kan du räkna ut det smartaste sättet att snitta tårtorna (fjärdedelar i detta fall)?

<details>
  <summary markdown="span">
    Tips
  </summary>
  <p>
  Vi behöver hitta det minsta talet som går att dela med både n och m. Det kan vi göra genom att först hitta det största talet d som både n och m kan delas med. Det kallas den största gemensamma delaren till n och m, och motsvarar alla de onödiga snitten. Vi behöver inte snitta tårtorna n*m gånger. Det räcker med (n*m)/d gånger.
  </p>
</details>

## Räkna ut största gemensamma delaren

Det finns flera olika sätt att räkna ut största gemensamma delaren till två tal. Här är Euclides ursprungliga algoritm:

```python
def gcd(a, b):
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a
```
**Uppdrag:** Klistra in koden ovan för `gcd`-funktionen (Greatest Common Divisor) och kontrollera att den fungerar på några exempel, t.ex.:

* `print(gcd(2,4))` borde ge `2`
* `print(gcd(15,6))` borde ge `3`

## Skär tårtorna smartare

**Uppdrag:** Ändra ditt program så att `gcd` används för att skära tårtorna med så få snitt som möjligt.

T.ex. borde du kunna få följande resultat:

<img src="smartcake.png" height="150">


Testa fler exempel, t.ex. att:

* `1/2 + 1/4 = 3/4` (i stället för `6/8`)
* `1/6 + 1/15 = 7/30` (i stället för `21/90`)

Kommer du inte på hur du skall göra?

<details>
  <summary markdown="span">
    Tips
  </summary>
  <p>
  Som vi nämnde tidigare så behöver tårtorna bara snittas (n*m)/d gånger. För tårtan med n bitar behöver vi alltså skära varje bit i m/d skivor. Och för tårtan med m bitar behöver vi skära varje bit i n/d skivor. Båda dessa tal kommer att vara heltal eftersom både m och n kan delas jämnt med d.
  </p>
</details>


Extra: Bygg ut programmet
=========================

Hur skulle du kunna förbättra och utöka programmet? Kanske:

* äta mer än en bit från varje tårta
* ha fler än två tårtor
* illustrera subtraktion mellan bråk
* rita cirkulära tårtor i stället för rektangulära
* ...

Du kan också gå vidare med uppdraget [Bråkspel](../fractions/README.md) som också handlar om bråk, och där du får göra ett spel.
