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

<img src="cake.png" width="100">

Detta uppdrag går ut på att illustrera heltalsbråk som delar av tårtor.

Innan du gör detta uppdrag bör du ha gjort uppdraget [Turtle](../turtle/README.md) där du får prova på "turtle graphics".

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

<details>
  <summary markdown="span">
    Svar
  </summary>
  <p>
  7
  </p>
</details>


Generalisera ditt program
=========================

Ditt program illustrerar hur

     1     1       7
    ––– + –––  =  ––––
     3     4       12

Skriv en funktion `addCakePieces(n,m)` som:

* ritar upp två tårtor
* delar den ena i `n` bitar och den andra i `m` bitar
* äter en bit från varje tårta
* illustrerar hur mycket tårta som ätits genom att snitta upp tårtorna i `n*m` bitar
* skriver ut ekvationen för den bråk-addition som illustreras, t.ex. `Eating cake: 1/3 + 1/4 = 7/12`

Prova ditt program med olika värden på `n` och `m` för att räkna ut `1/n + 1/m`. Kontrollera t.ex. att
* 1/2 + 1/5 = 7/10

Prova fler exempel. Vilka exempel kan du komma på som verkar intressanta att testa?
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

Fungerade ditt program bra för alla exemplen?

Extra: Snitta tårtorna smartare
===============================

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

Innan du går vidare med denna extrauppgift bör du göra [detta uppdrag](../gcd/README.md) där du lär dig hur man programmerar uträkning av största gemensamma delaren mellan två tal. Sedan kan du förbättra ditt tårtprogram så det snittar tårtorna på smartaste sätt. Testa t.ex. att:

* `1/2 + 1/4 = 3/4` (i stället för `6/8`)
* `1/6 + 1/15 = 7/30` (i stället för `21/90`)

Extra: Bygg ut programmet
=========================

Hur skulle du kunna förbättra och utöka programmet? Kanske:

* äta mer än en bit från varje tårta
* ha fler än två tårtor
* illustrera subtraktion mellan bråk
* rita cirkulära tårtor i stället för rektangulära
* ...

Du kan också gå vidare med uppdraget [Bråkspel](../fractions/README.md) som också handlar om bråk, och där du får göra ett spel.
