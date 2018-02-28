---
layout: page
title: Kojo/Scala Turtle snabbreferens
permalink: turtle-cheatsheet/scala
toc: true
---

Denna kod är provkörd på online-miljön [kojo-js](http://kojojs.kogics.net) för Scala.

# Kom igång

Kojo är en miljö för programspråket Scala och med stöd för "turtle graphics". Här är ett program som ritar en liten figur.

```scala
forward(20)   // Paddan går 20 steg framåt
right(60)     // Paddan vrider sig 60 grader åt höger
forward(30)   // Paddan går 20 steg framåt
```

# Styr sköldpaddan

## Styr med relativa kommandon

```scala
forward(20) // Paddan går 20 steg framåt
back(20)    // Paddan går 20 steg framåt
right(45)   // Paddan vrider sig 45 grader åt höger
left(45)    // Paddan vrider sig 45 grader åt vänster
hop(20)     // Paddan hoppar 20 steg framåt, utan att rita
hop(-20)    // Paddan hoppar -20 steg framåt, dvs 20 steg bakåt, utan att rita
arc(50, 90) // Paddan ritar en båge med radien 50 och vinkeln 90
circle(50)  // Paddan ritar en cirkel med radien 50
```

## Styr med absoluta koordinater

```scala
setPosition(50,80) // Paddan hoppar till läget (50, 80) utan att rita
setHeading(45)     // Paddan vrider nosen till vinkeln 45 grade
moveTo(10,10)      // Paddan vrider sig och går till läget (10, 10)
```

## Sätt färger, penntjocklek, etc.

```scala
setPenColor(pink)    // Sätter pennans färg till rosa
setFillColor(purple) // Sätter ifyllnadfärgen till lila
setPenThickness(20)  // Sätter pennans bredd till 20
```

## Låt paddan skriva text

```scala
write("hello")      // Paddan skriver texten "hello"
setPenFontSize(20)  // Paddan kommer nästa gång att skriva text med storlek 20
```

## Sätt hastigheten på paddan
```scala
setAnimationDelay(0)     // Paddan ritar så snabbt som möjligt
setAnimationDelay(10000) // Paddan ritar väldigt långsamt
```

# Annat du kan göra i Kojo

## Läs in och skriv ut

Du kan skriva ut text i paddans fönster:

```scala
println("Hello!")
```

Du kan läsa in inmatning från användaren med följande funktioner. De skriver alla ut en ledtext och väntar sedan på inmatning. Det som användaren skrev hamnar i värdet `s` respektive `i` och `d`.

```scala
val s = readln("Skriv en sträng: ")        // läs in en sträng
val i = readInt("Skriv ett heltal: ")      // läs in ett heltal
val d = readDouble("Skriv ett double-tal") // läs in ett decimaltal
```

Typen double används för decimaltal. Man använder punkt i stället för komma: `3.14` i stället för `3,14`.


*Obs!* I kojo-js kommer du inte att se vad paddan ritar eller vad `println` skrivit ut förrän programmet kört klart, dvs efter alla reads.

## Sätta ihop strängar

När du skriver ut är det ofta praktiskt att sätta ihop strängar. Det kan man göra med `+`. Men tal och andra värden som inte är strängar från början behöver då omvandlas till strängar med hjälp av funktionen `toString`:

```scala
println("En vecka har " + 7.toString + " dagar.")
```

## Dra slumptal

Du kan använda slumptal på följande sätt:

```scala
random(100)       // Ger ett slumptal mellan 0 och 99
randomDouble(100) // Ger ett slumptal mellan 0 och 99.9999
randomBoolean     // Ger slumpmässigt värdet true eller false
randomFrom(Seq(1,3,5)) // Drar ett värde slumpmässigt från sekvensen
```

# Konstruktioner i Scala

Kojo är en miljö för språket Scala. Här är några enkla exempel på Scala-konstruktioner.

## Definiera en funktion

Med en `def` kan du göra egna funktioner som kan användas som byggblock:

```scala
def step(length:Int) = {   // Definera funktionen step
  forward(length)
  left(90)
  forward(length)
  right(90)
}

step(20)                  // Anropa funktionen
step(30)                  // med olika parametrar
```

## Deklarera värden och variabler

`val` används för att namnge värden. `var` används för att namnge variabler. Man kan ändra värdet på en variabel.

```scala
val v = 10       // v är ett namn på värdet 10
println(v)       // 10 skrivs ut
var w = 20       // w är en variabel som ges värdet 10
println(w)       // 20 skrivs ut
w = w + 1        // värdet på w ändras till 20 + 1
println(w)       // 21 skrivs ut
```

## Repetition

Med en for-loop kan vi repetera ett visst antal varv:

```scala
var a = 0           // deklarera en loop-variabel a
for( a <- 1 to 5){  // repetera 5 gånger
   println(a)       // a har olika värden i varje varv
}
```

Med en while-loop kan vi repetera tills ett uttryck är sant:

```scala
var a = 1
while (a <= 5) {    // loopa så länge a är mindre eller lika med 5
  println(a)
  a = a + 1         // öka a med 1
}
```

## Alternativ

Med en if-sats kan man göra alternativa saker beroende på värdet på ett uttryck:

```scala
val a = readInt("Skriv ett heltal: ")
if (a < 10) {
  println("Det var mindre än 10")
}
else if (a == 10) {
  println("Det var lika med 10")
}
else {
  println("Det var större än 10")
}
```

# Tangentbordet

Har du svårt att hitta vissa tecken på tangentbordet? För ett svenskt tangentbord behöver du känna till:

* SKIFT-tangenten - den man får stora bokstäver med
* ALT-tangenten - sitter någonstans nere till vänster.
* ALT-GR-tangenten - finns på Windows-datorer. Sitter någonstans nere till höger. Ibland är den bara märkt med ALT.

Genom att hålla nere en eller flera av dessa tangenter innan du trycker på en annan tangent kan du få fram ovanliga tecken.

* `/` kallas "snedstreck" ("slash" på engelska). Två snedstreck används för att inleda en kommentar i Scala.
* `*` används för multiplikation i kod.
* `{ }` kallas "krullparenteser" eller "måsvingar" ("curly brackets", "braces", eller "curly braces" på engelska).

Prova att hålla nere SKIFT-tangenten för att t.ex. skriva `/` eller `*`.

För att få fram krullparenteserna:
* På Mac: håll nere *både* SKIFT och ALT och tryck på `(` för vänsterkrulle och `)` för högerkrulle.
* På Windows: håll nere ALT-GR och tryck på `7` för vänsterkrulle och `0` för högerkrulle.

Fungerar inte detta? Prova dig fram, fråga, eller googla.


# Mer information

* [Lalit Pants snabbreferens till Kojo](https://bitbucket.org/lalit_pant/kojo/downloads/KojoQuickref-301014.pdf) *Obs!* Alla kommandon i kojo fungerar inte ännu på kojo-js miljön.
