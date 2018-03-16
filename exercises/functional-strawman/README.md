I denna uppgift kommer du att träna på funktioner.

Koden i denna uppgift är provkörd på [http://repl.it/languages/python-turtle](http://repl.it/languages/python-turtle) (Python 2.7).

### 1. Rita en streckgubbe

Inför fortsättningen behöver vi programkod som ritar en streckgubbe utan armar. (Gubben kommer att få armar senare.)

Till att börja med beöver vi ett tomt program, som importerar `turtle`- och `math`-paketen och skapar en Turtle. Vi behöver även återanvända funktionen `jumpTo` från en tidigare uppgift.

```import turtle
import math

t = turtle.Turtle()

def jumpTo(x, y):
  t.penup()
  t.setpos(x,y)
  t.pendown()
```

Lägg nu till rader i programmet som ritar gubbens ben, kropp och huvud.

Kom ihåg att lösa uppgiften i delar. Börja exempelvis med ett av benen, och se till att det blir rätt. När det stämmer utökar du ditt program med ett ben till. På samma sätt fortsätter du med ett streck för kroppen. Om du hellre vill börja med huvudet går det naturligtvis också bra.

<details>
<summary markdown="span">
Möjlig lösning
</summary>
<p>
Följande Python-program ritar en enkel streckgubbe, med en cirkel som huvud.

```python
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
```
</p>
</details>

**Uppdrag:** Provkör programmet! Kontrollera att streckgubben (utan armar) ser rimlig ut.

### 2. Vi inför en funktion

Nu ska vi införa en funktion för att rita streckgubben. Denna funktion ska innehålla Python-satserna du skrev i föregående uppgift. Funktionen kan exempelvis heta `gubbe`:

```python
import turtle

t = turtle.Turtle()

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

**Uppdrag:** Kör programmet igen. Nu när anropet till funktionen `gubbe` är på plats ska gubben vara tillbaka -- fortfarande utan armar.

### 3. Vi inför en funktion till för armarna

Vi kommer att pröva ett par olika sätt att rita gubbens armar. Först vill vi rita ett helt vanligt streck.

Vi återanvänder funktionen `jumpTo` från Sköldpaddsgrafik-uppgiften:

```python
def jumpTo(x, y):
  t.penup()
  t.setpos(x,y)
  t.pendown()
```

Denna funktion flyttar paddan till läget `(x,y)` utan att rita.

**Uppdrag:** Stoppa in Python-raderna ovan i ditt program, på något lämpligt ställe. De kan exempelvis passa bra innan din `gubbe`-funktion. Kontrollera att programmet fortfarande gör samma sak som tidigare -- du har ju inte med något anrop till `jumpTo` ännu.

**Uppdrag:** Lägg nu in en tredje funktion i ditt program. Den kan exempelvis heta `armar`. I funktionen `armar` ska tre saker göras:

1. Sköldpaddan flyttas till lämpliga koordinater. Använd koordinaterna `(-50, 50)` så länge. Du kommer säkert att behöva justera dem strax.
2. Sköldpaddans riktning sätts till 0 grader, dvs rakt åt höger. (Du kan använda `t.setheading()`.)
3. Sköldpaddan tar 200 steg framåt.

Provkör programmet. Vad händer?

<details>
<summary markdown="span">
Tips
</summary>
<p>
Kom ihåg att funktionen `armar` måste anropas, precis som `gubbe`.
</p>
</details>

När du fått programmet att rita ut armarna kommer de troligen att ha hamnat på fel ställe. Ovan lät vi dem börja på koordinaterna `(-50,50)`, vilket troligen inte alls passar med din streckgubbe.

Justera koordinaterna så att armarna hamnar rätt. De ska vara lika långa, och sitta på kroppen.

### 4. Vi prövar en matematisk funktion

Nu lägger vi streckgubben åt sidan en stund. Vi återkommer snart till den.

Istället ska du vi införa en funktion till. Denna gång är det en funktion som, liksom matematiska funktioner, ger ett värde som resultat.

Vi börjar med den enkla funktionen

f(x) = -x

En sådan funktion skrivs i Python så här:

```
def f(x):
  return -x
```

Texten från `#` och framåt är en kommentar. Den är inte nödvändig för att programmet ska fungera, utan fungerar istället som en anteckning för programmeraren.

Lägg till funktionen ovan i ditt program. Liksom tidigare händer det förrän funktionen anropas.

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

**Uppdrag:** kör programmet. Hur många armar har streckgubben? Kan du se hur armen motsvarar funktionen `f`?

<details>
<summary markdown="span">
Tips: snabba upp utritningen
</summary>
<p>
Det är många punkter som ska plottas. Man kan snabba upp Turtle-grafiken genom att bara uppdatera fönstret (exempelvis) var 20:e gång. Stoppa in följande rad i ditt program, direkt efter raden `t = turtle.Turtle()`:

```python
t.getscreen().tracer(20)
```
</p>
</details>

Vi behöver tydligen ändra i programmet för att få med båda armarna. Just nu antar `i` ovan bara värden >= 0.

**Uppdrag:** Ändra `for`-satsen så att `i` antar värden från -100 till 100. Använd `range(-100,100)`.

<details>
<summary markdown="span">
Tips
</summary>
<p>
```python
def armar():
  for i in range(-100, 100):
    # ...
```
  </p>

</details>

Nu ska gubben ha två armar, en som pekar uppåt, och en som pekar neråt.

### 6. Vi prövar andra funktioner

**Uppdrag:** använd din streckgubbe för att plotta följande funktioner:

* f(x) = x
* f(x) = 50 cos (x * pi / 200)
* f(x) = 50 sin (x * pi / 200)
* f(x) = 50 sin (x * pi / 400)
* f(x) = x * x / 100

där pi har ett välkänt värde (3.14159...).

<details>
<summary markdown="span">
Tips: cos, sin och pi i Python
</summary>
<p>
I Python skrivs sin(x) som `math.sin(x)` och pi som `math.pi`. Detta förutsätter att man i början av programmet skrivit `import math`, som vi gjort.
</p>
</details>

### 7. Funktion som parameter (avancerat)

Uppgiften ovan löste du genom att ändra i din funktion `f`. Det vore praktiskt om man istället kunde ha många olika funktioner definierade, och därefter bara peka ut den önskade funktionen i anropet till `armar`.

Vi vill alltså ha en funktion `armar` som har en parameter. Parametern syftar i sin tur på den funktion som ska plottas. Så här kan det se ut när man definierar ett par bra funktioner, och använder `armar` för att plotta en av dem:

```python
def g(x):
  return 50 * math.exp(x / 100.0)

def h(x):
  return x / 2.0

gubbe()
armar(g)    # plotta funktionen g
```

**Uppdrag:** ändra din funktion `armar` så att man kan använda en parameter enligt ovan.
