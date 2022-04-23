---
layout: default
type: exercise
tags:
 - bra första-uppgift
 - sköldpaddsgrafik
 - sekvenser och loopar
 - geometri och vinklar
---

# Månghörningar

I denna uppgift kommer du att träna på vinklar i regelbundna månghörningar. Vi använder "turtle graphics" för detta.

Du får även träna på att ändra i och experimentera med program.

**En bra första-uppgift. Du lär dig...**
* Sköldpaddsgrafik
* Sekvenser och loopar
* Geometri och vinklar


Koden i denna uppgift är provkörd på [http://repl.it/languages/python-turtle](http://repl.it/languages/python-turtle) (Python 2.7).

### 1. Rita en triangel

I följande program deklareras en turtle kallad `t`.
Därefter ritas en liksidig triangel med sidan 100.
Efter varje sida svänger sköldpaddan 120 grader.

```python
import turtle
t = turtle.Turtle()

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
```

**Uppdrag:** Provkör programmet! Läs programmet och se om du kan se varför det ger en triangel.

### 2. Rita en felaktig triangel

Ändra talet 120 i programmet ovan till exempelvis 130. (Du behöver ändra på tre ställen.)

**Uppdrag:** Kör programmet och titta på figuren. Varför kommer sköldpaddan inte tillbaka till ursprungspunkten?

Ändra nu talet 130 istället till 110. (Du behöver återigen ändra på tre ställen.)

**Uppdrag:** Kör programmet igen. Varför kommer sköldpaddan inte tillbaka till ursprungspunkten?

### 3. Fundera lite på geometri

Tydligen måste vinkeln vara exakt 120 grader för att sköldpaddan ska hitta tillbaka.

**Uppdrag:** Fundera: kan du komma på varför vinkeln måste vara just 120 grader?

<details>
<summary markdown="span">
Tips
</summary>
<p>
Hur många grader går det på ett varv? Hur många gånger svänger sköldpaddan? Hur många grader måste den då svänga i taget?
</p>
</details>

<details>
<summary markdown="span">
Tips
</summary>
<p>
360 / 3 = 120
</p>
</details>

### 4. Gör en femhörning

Ändra i programmet så att du får en regelbunden femhörning, istället för en triangel.

Du behöver göra två saker:

  * Lägg till ytterligare två par av `forward` och `left` sist i ditt program. Kopiera gärna från den befintliga koden.
  * Ändra vinkeln, från 120 till ett bättre värde. Du behöver nu alltså ändra på fem ställen.

Kan du räkna ut hur många grader sköldpaddan måste svänga mellan varje sida i femhörningen, för att hitta tillbaka till startpunkten?

**Uppdrag:** kör ditt femhörningsprogram. Blir resultatet som du förväntade dig?

### 5. Ett mer generellt program

Här följer ett annat program för att rita en liksidig triangel.
Det använder en `for`-sats för att rita en sida `n` gånger.

```python
import turtle
t = turtle.Turtle()

n = 3

for i in range(n):
  t.forward(100)
  t.left(120)
```

**Uppdrag:** kör programmet. Pröva att ändra variabeln `n` till något annat. Får du något annat än en liksidig triangel? Varför inte?

<details>
<summary markdown="span">
Tips
</summary>
<p>
Raden <code>t.left(120)</code> behöver ändras.
</p>
</details>

**Uppdrag:** ändra programmet så att det fungerar för godtyckliga värden på `n`, där `n` matas in av användaren. (T.ex., om n = 5 skall en liksidig femhörning ritas ut.)

För att läsa in ett heltal `n` från tangentbordet kan du göra så här:

```python
n = int(input("Antal sidor: "))
```

Notera att inmatningen sker i fliken **console**, så när du kör programmet måste du växla till den, knappa in `n`, och därefter växla till fliken **result** för att se din `n`-hörning.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Du behöver stoppa in beräkningen <code>360.0 / n</code> på rätt ställe.
</p>
</details>

<details>
<summary markdown="span">
Tips: glipar din månghörning?
</summary>
<p>
Kanske upptäcker du att vissa månghörningar ändå glipar lite grann, exempelvis för <code>n = 7</code>.
Det beror på att 7 inte går jämnt upp i 360.
För att få med decimalerna i kvoten behöver man skriva <code>360.0 / n</code>.
Om man skriver <code>360 / n</code> får man en kvot utan decimaler, så om <code>n = 7</code> får man kvoten 51 istället för 51,428.
</p>
</details>

Talet 360 är delbart med väldigt många heltal (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30 och 60). Babylonierna, som delade in cirkeln i 360 grader för sisådär 4000 år sedan, visste vad de gjorde.
