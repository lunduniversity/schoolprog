---
layout: page
title: Funktionsgubbe
permalink: /exercises/functional-strawman/
toc: true
type: exercise
tags:
 - intermediate
 - functions
 - turtle graphics
---

I denna uppgift kommer du att träna på funktioner.

Koden i denna uppgift är provkörd på [http://repl.it/languages/python-turtle](http://repl.it/languages/python-turtle) (Python 2.7).

### 1. Rita en streckgubbe

Inför fortsättningen behöver vi programkod som ritar en streckgubbe utan armar. (Gubben kommer att få armar senare.)

Till att börja med behöver vi ett tomt program, som importerar `turtle`- och `math`-paketen och skapar en Turtle. Vi behöver även återanvända funktionen `jumpTo` från en tidigare uppgift. Vi kommer att ha nytta av den senare.

```python
import turtle
import math

t = turtle.Turtle()

def jumpTo(x, y):
  t.penup()
  t.setpos(x,y)
  t.pendown()
```

Lägg nu till rader i programmet som ritar gubbens ben, kropp och huvud.

*Tips:* Använd funktionerna `t.right(...)`, `t.forward(...)`, och `t.left(...)`.

Kom ihåg att lösa uppgiften i delar. Börja exempelvis med ett av benen, och se till att det blir rätt. När det stämmer utökar du ditt program med ett ben till. På samma sätt fortsätter du med ett streck för kroppen. Om du hellre vill börja med huvudet går det naturligtvis också bra.

<details>
<summary markdown="span">
Möjlig lösning
</summary>
<p>
Följande Python-program ritar en enkel streckgubbe, med en cirkel som huvud.

<pre>
import turtle

t = turtle.Turtle()

t.setheading(225)
t.forward(100)
t.left(180)
t.forward(100)
t.right(90)
t.forward(100)
t.left(180)
t.forward(100)
t.right(45)
t.forward(200)
t.right(90)
t.forward(50)
t.left(90)
for sida in range(3):
  t.forward(100)
  t.left(90)
t.forward(50)
</pre>
</p>
</details>

**Uppdrag:** Provkör programmet! Kontrollera att streckgubben (utan armar) ser rimlig ut.

### 2. Vi inför en funktion

Nu ska vi införa en funktion för att rita streckgubben. Denna funktion ska innehålla Python-satserna du skrev i föregående uppgift. Funktionen kan exempelvis heta `gubbe`:

```python
import turtle
import math

t = turtle.Turtle()

def jumpTo(x, y):
  # ... enligt tidigare

def gubbe():
  # ... satserna för att rita gubben, enligt tidigare uppgift
```

Inför funktionen `gubbe` enligt ovan och använd dina Python-satser där.

Kom ihåg att satserna i funktionen måste vara indenterade (indragna) med ett par mellanslag, annars kommer inte Python-tolken att förstå att de har med `gubbe` att göra.

**Uppdrag:** Kör programmet. Varför ser du inte längre någon gubbe?

Lägg nu till en rad i ditt program som anropar funktionen gubbe.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Jämför med vimpel-exemplet i uppgiften Sköldpaddsgrafik om du är osäker.
</p>
</details>

**Uppdrag:** Kör programmet igen. Nu när anropet till funktionen `gubbe` är på plats ska gubben vara tillbaka, fortfarande utan armar.

### 3. Vi inför en funktion till, för armarna

Vi kommer att pröva ett par olika sätt att rita gubbens armar. Först vill vi rita ett helt vanligt streck.

**Uppdrag:** Lägg nu in en tredje funktion i ditt program. Den kan exempelvis heta `armar`. I funktionen `armar` ska tre saker göras:

1. Sköldpaddan flyttas till koordinaterna `(-100, 0)`. (Du kan använda `jumpTo`, som vi ju återanvände sedan tidigare.)
2. Sköldpaddans riktning sätts till 0 grader, dvs rakt åt höger. (Du kan använda `t.setheading()`.)
3. Sköldpaddan tar 200 steg framåt.

Provkör programmet. Vad händer?

<details>
<summary markdown="span">
Tips
</summary>
<p>
Kom ihåg att funktionen <code>armar</code> måste anropas, precis som <code>gubbe</code>.
</p>
</details>

När du fått programmet att rita ut armarna kommer de troligen att ha hamnat på fel ställe. De utgår från att streckgubben har sina axlar i origo, vilket troligen inte alls passar med din streckgubbe.

**Uppdrag:** stoppa in ett `jumpTo`-anrop först i din funktion `gubbe`, så att gubben hamnar med axlarna i origo.
Justera koordinaterna så att armarna hamnar rätt. Det kan mycket väl behövas några försök för att det ska bli rätt.

Armarna ska vara lika långa, och sitta på kroppen.

### 4. Vi prövar en matematisk funktion

Nu lägger vi streckgubben åt sidan en stund. Vi återkommer snart till den.

Istället ska du vi införa en funktion till. Denna gång är det en funktion som, liksom matematiska funktioner, ger ett värde som resultat.

Vi börjar med den enkla funktionen

<img src="f1.png">

En sådan funktion skrivs i Python så här:

```python
def f(x):
  return -x
```

(Nyckelordet `return` talar om vilket värde funktionen skall returnera. De andra funktionerna vi skrivit tidigare har bara utfört kommandon, och inte räknat ut något resultat.)

Lägg till funktionen ovan i ditt program. Liksom tidigare händer det inget förrän funktionen anropas.

Vi ska snart använda funktionen till streckgubben, men först vill vi pröva den och se att den fungerar som vi förväntar oss.

Lägg därför till följande rader i ditt program (exempelvis sist):

```python
print f(1), f(3), f(-5)
```

**Uppdrag:** kör programmet, inklusive raderna ovan. Klicka på fliken _Console_, där utskrifterna (`print`) hamnar. Stämmer de tre värdena för f(x)?

### 5. Vi ger gubben matematiska armar

Nu ska vi förändra funktionen `armar`, så att gubbens armar ritas genom att vi plottar funktionen `f`. För detta behöver vi återigen införa en hjälpfunktion. Funktionen `plot` nedan använder sköldpaddan för att placera en punkt på koordinaterna `(x,y)`:

```python
def plot(x, y):
  jumpTo(x, y)
  t.dot(1)
```

Ändra nu i din funktion `armar` så att du använder repetition (en `for`-sats) för att plotta punkterna `(i, f(i))`. Låt `i` anta värdena 0 till 100.

*Tips:* Ta bort den gamla koden i `armar` som ritade ett streck, och ersätt med en `for`-loop som anropar `plot` för att sätta en punkt för varje varv i loopen.

**Uppdrag:** kör programmet. Hur många armar har streckgubben? Kan du se hur armen motsvarar funktionen `f`?

<details>
<summary markdown="span">
Tips: om du tycker det går för långsamt
</summary>
<p>
Det är många punkter som ska plottas. Man kan snabba upp Turtle-grafiken genom att bara uppdatera fönstret (exempelvis) var 10:e gång. Stoppa in följande rad i ditt program, direkt efter raden <code>t = turtle.Turtle()</code>:

<pre>
t.getscreen().tracer(10)
</pre>
</p>
</details>

Vi behöver tydligen ändra i programmet för att få med båda armarna. Just nu antar `i` ovan bara positiva värden.

**Uppdrag:** Ändra din `for`-sats så att `i` antar värden från -100 till 100. Använd `range(-100,100)`.

Nu ska gubben ha två armar, en som pekar uppåt, och en som pekar neråt. Kan du se att det är funktionen f(x) enligt ovan som avbildas?

### 6. Vi prövar andra funktioner

**Uppdrag:** använd din streckgubbe för att plotta följande funktioner, en i taget.

<img src="f2.png">

*Tips:* cos, sin och pi i Python
I Python skrivs sin(x) som `math.sin(x)` och pi som `math.pi`. Detta förutsätter att man i början av programmet skrivit `import math`, som vi gjort.

*Tips:* Glöm inte att man måste använda nyckelordet `return` i Python-funktionen för att den skall returnera ett värde till anropet.

**Uppdrag:** Hitta på en egen funktion som du plottar som armar.

*Tips:* För att armarna skall hamna förnuftigt, så se till att funktionen är noll eller nära noll för x=0. Du kan göra `print(f(0))` för att se vad funktionens värde är vid x=0.

### 7. Funktion som parameter (avancerat)

Uppgiften ovan löste du genom att ändra i din funktion `f`. Det vore praktiskt om man istället kunde ha många olika funktioner definierade, och därefter bara peka ut den önskade funktionen i anropet till `armar`.

Vi vill alltså ha en funktion `armar` som har en parameter. Parametern syftar i sin tur på den funktion som ska plottas. Om vår `armar`-funktion fungerar så, så kan den användas så här:

```python
def g(x):
  return x / 2.0

def h(x):
  return 50 * math.exp(x / 100.0) - 50

gubbe()
armar(g)    # plotta funktionen g
```

Här definieras ett par bra funktioner `g` och `h`, och därefter används `armar` för att plotta en av dem.

**Uppdrag:** ändra din funktion `armar` så att man kan använda en parameter enligt ovan.

<details>
<summary markdown="span">
Tips
</summary>
<p>
I <code>armar</code> används namnet <code>f</code> för att bestämma vilken funktion som ska plottas. Låt <code>f</code> vara en parameter till <code>armar<\code>, på samma sätt som <code>x\code> och <code>y\code> är parametrar till <code>jumpTo\code>.
</p>
</details>

Genom att ändra `g` till `h` ovan kan man nu enkelt välja vilken funktion som ska plottas.

*Kommentar:* Vid divisionerna i `g` och `h` används reella tal som `2.0` och `100.0` i stället för heltal `2` och `100`. Det är för att Python 2.7 (som används för paddan) tolkar division mellan två heltal som heltalsdivision där resten försvinner. När t.ex. Python räknar ut 3/2 blir resultatet 1 (i stället för 1.5). Men när något av talen i divisionen är ett reellt tal, så blir resultatet också reellt. Så när Python räknar ut 3/2.0 blir resultatet 1.5, som vi förväntar oss.
