---
layout: page
---

Funktiontips
============

En *funktion* i ett programspråk kan ha inparametrar och kan beräkna ett resultat.<sup>1</sup>

Här är exempel på en funktion som adderar två heltal i Scala:

    def sum(a:Int, b:Int) : Int = {
      return a + b
    }

Så här skriver man i Python:

    def sum(a, b):
        return a + b

Man kan sedan anropa funktionen med olika parametervärden:

    sum(1, 2)
    sum(37, 5)
    sum(sum(39,4), 7)

Prova att definiera en funktion, t.ex. `sum` ovan, och anropa den med lite olika parametrar.

Prova också att göra något mer i funktionen än att returnera resultatet. Till exempel att skriva ut<sup>2</sup> parametrarna:

I Scala:

    def sum(a:Int, b:Int) : Int = {
      println(a)
      println(b)
      return a + b
    }

I Python:

    def sum(a, b):
        print(a)
        print(b)
        return a + b


I Bråkspelet skall du skriva en funktion som tar två bråk som inparametrar och returnerar ett bråk, och där varje bråk är en tupel med två heltal. Här är ett skelett för hur du kan skriva i Scala:

    def sumFractions(f1:(Int, Int), f2:(Int, Int)) : (Int, Int) = {
      val (t1, n1) = f1
      val (t2, n2) = f2
      return (..., ...)
    }

----

<sup>1</sup>Dessutom kan en funktion ha sido-effekter som till exempel att skriva ut saker, eller ändra på variabler.

<sup>2</sup>`println` står för "print line", och betyder att man först skriver ut något, t.ex. värdet på `a`, och sedan gör en ny rad. Dvs nästa sak som skrivs ut kommer på nästa rad.
