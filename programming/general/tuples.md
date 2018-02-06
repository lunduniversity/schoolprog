---
layout: page
---

Tupeltips
=========

En *tupel* är ett sammansatt värde. Den passar bra för att representera ett till exempel ett heltalsbråk, som ju består av två delar: en täljare och en nämnare.

Tuplar kan användas både i Scala och Python. Ett tupelvärde skrivs med parenteser runt värdet, och med komman mellan delvärdena. T.ex. kan man konstruera bråket "en halv" med:

| Scala  | Python |
|:------:|:------:|
|`(1, 2)`|`(1, 2)`|


Typen på detta värde är `(Int, Int)`

Så här deklarerar du ett bråk `b` med täljaren `2` och nämnaren `5`:

| Scala          | Python       |
|:--------------:|:------------:|
|`val b = (2, 5)`|`b = (2, 5)`  |

När du har ett tupelvärde, som `b`, kan du *dekonstruera* det på lite olika sätt, det vill säga du kan komma åt delvärdena på lite olika sätt.

Få ut alla delvärdena på en gång:

| Scala              | Python       |
|:------------------:|:------------:|
|`val (t, n) = b`    |`(t, n) = b`  |

Få ut ett av delvärdena i taget genom att tänka sig att de numreras från vänster till höger (från `1` i Scala, från `0` i Python):

| Scala              | Python       |
|:------------------:|:------------:|
|`val t = b._1`      |`t = b[0]`    |
|`val n = b._2`      |`t = b[1]`    |


Prova att deklarera ett värde med namnet `x` som representerar "tre sjundedelar", och prova att dekonstruera det för att få ut delvärdena tre och sju.

I programspråk som inte stödjer tuplar kan man i stället använda arrayer eller objekt, men det blir lite krångligare.

Hur skriva en funktion som summerar två bråk?
---------------------------------------------

Funktionen bör ta två bråk som input och räkna ut ett nytt bråk som output.

Här får du ett skelett till funktionen i Scala:

    def sumBrak(b1:(Int, Int), b2:(Int, Int)) : (Int, Int) = {
        return ...
    }
