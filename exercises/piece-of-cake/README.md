---
layout: page
title: Piece of cake
permalink: /exercises/piece-of-cake/
toc: true
type: exercise
---

<img src="cake.png" width="100">

Detta uppdrag går ut på att illustrera heltalsbråk som delar av tårtor.

Innan du gör detta uppdrag bör du ha lekt lite med "turtle graphics".

<details>
  <summary markdown="span">
    Klicka här för python-exempel för att programmera en turtle.
  </summary>
  <pre>
    import turtle
    t = turtle.Turtle()
    t.color('pink')
    t.fillcolor(color)
    t.fill(True)
    t.width(5)
    t.forward(50)
    t.right(90)
    t.forward(300)
  </pre>
</details>

Rita en tårta
=============

Rita en avlång rektangulär tårta med "turtle graphics". Kanten på tårtan skall vara i en färg och den skall vara fylld med en annan färg.

Rita flera tårtor
=================

Gör om koden för tårtan till en funktion `drawCake(x)` som ritar en tårta `x` pixlar från origo. Anropa funktionen med två olika värden på `x` så att du får två tårtor snyggt placerade bredvid varann. Tårtorna skall vara lika stora.

Extra: snygga till tårtorna
===========================

Om du tycker om snygga tårtor, skriv en funktion `decorateCake(x)` som dekorerar tårtan på plats `x` på något sätt. Kanske med en ros i mitten?

Skär upp tårtan
===============

Tänk dig att du vill skära tårtan i delar. Skriv en funktion `cutCake(x, n)` som skär tårtan på plats `x` i `n` lika stora bitar. Skär tårtan genom att rita linjer med en tredje färg.

Prova att skära den ena tårtan i tredjedelar och den andra i fjärdedelar.

Ät tårta
========

Skriv en funktion `eatCake(x, n)`som äter upp den första biten av en tårta genom att färga delen svart.

Prova att äta en bit av tårtan som är skuren i tredjedelar och en av tårtan som är skuren i fjärdedelar.

Hur mycket har du ätit?
=======================

Hur mycket tårta är uppäten, räknat i delar av en hel tårta?

Om vi hade delat varje tårta i tolftedelar (delbart med både 3 och 4), så hade vi lätt kunnat se hur mycket tårta som ätits sammanlagt.

Illustrera detta genom att skriva en funktion `slicePieces(x, g)` som skär tårtan på plats `x` i `g` lika stora delar. Gör detta genom att rita linjer med en fjärde färg. Rita sådana linjer både på de bitar som ätits upp och de som är kvar.

Prova genom att anropa med `g=12` för de två tårtorna.

Hur många tolftedelar tårta är uppätna?

Generalisera ditt program
=========================

Ditt program illustrerar hur

     1     1       ??
    ––– + –––  =  ––––
     3     4       12

Skriv en funktion `addCakePieces(n,m)` som:

* ritar upp två tårtor
* delar den ena i `n` bitar och den andra i `m` bitar
* äter en bit från varje tårta
* illustrerar hur mycket tårta som ätits genom att dela upp bitarna på lämpligt sätt
* skriver ut ekvationen för den bråk-addition som illustreras, t.ex. `Eating cake: 1/3 + 1/4 = ...`

Prova ditt program med olika värden på `n` och `m`

Gå vidare
=========

Hur skulle du kunna modifiera och utöka programmet? Kanske:

* äta mer än en bit från varje tårta
* ha fler än två tårtor
* illustrera subtraktion mellan bråk
* rita cirkulära tårtor i stället för rektangulära
* ...
