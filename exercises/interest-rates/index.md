---
title: Låna pengar
layout: default
toc: true
type: exercise
permalink: /exercises/interest-rates/
tags:
 - medel
 - text
 - plottning
 - procent
 - ränta
---
# Låna pengar

Det är lätt att låna pengar, t.ex. med ett sms-lån, men hur mycket kostar det egentligen?
Vi skall skriva ett program som räknar ut det.

Koden i denna uppgift är provkörd på [http://repl.it/languages/python3](http://repl.it/languages/python3) (Python 3).

Vi vill kunna jämföra erbjudanden om lån från olika firmor. En firma *Buffel&Båg* lånar ut med en månadsränta på 29% och en månadsavgift på 149 kr. En annan firma *Lurendrejarna* lånar ut utan månadsavgift men med 39% månadsränta.

## 1. Kostnad efter en månad

Funktionen

```python
def cost_after_one_month(loan, month_rate, month_fee):
  ...
```
ska returnera kostnaden för att låna `loan` kronor med en månadsränta på `month_rate` procent och en månadsavgift på `month_fee` kronor. Till exempel blir

* `cost_after_one_month(1000, 11, 0)` = `110`
* `cost_after_one_month(1000, 0, 42)` = `42`
* `cost_after_one_month(1000, 11, 42)`= `152`

**Uppdrag:**
* Skriv funktionen `cost_after_one_month`.
<!--* Lägg till *asserts* för att kontrollera att funktionen räknar rätt i testfallen ovan.-->
* Anropa funktionen för att se till att den fungerar för testfallen ovan.
* Anropa funktionen för att räkna ut vad det kostar att låna 1000 kr i en månad hos firman *Buffel&Båg* respektive hos *Lurendrejarna*.
* Skriv ut resultatet på ett begripligt sätt. T.ex. "1000 kr lån i 1 månad hos Buffel&Båg kostar ... kronor."

<details>
<summary markdown="span">
Tips för att skriva funktionen!
</summary>
<p>För att räkna ut räntekostnaden i kronor skall du multiplicera lånet med månadsräntan och sedan dividera med 100 (eftersom månadsräntan anges i procent). Funktionen skall returnera hela kostnaden. För att få den behöver du lägga ihop räntekostnaden och månadsavgiften.
</p>
</details>



<!--*Mer tips!* För att använda *asserts*, se övningen [Avlusning](exercises/debugging).-->

<!--
## 2. Skuld efter en månad

I förra uppdraget räknade vi bara ut kostnaden för att få låna. Själva lånet skall ju också betalas. Vi ska lägga till en ny funktion

```python
def debt_after_one_month(loan, month_rate, month_fee):
  ...
```

som räknar ut vad skulden är efter en månad. Till exempel blir

* `debt_after_one_month(1000, 11, 0)` = `1110`
* `debt_after_one_month(1000, 0, 42)` = `1042`
* `debt_after_one_month(1000, 11, 42)`= `1152`

**Uppdrag:**
* Skriv funktionen `debt_after_one_month`
* Anropa funktionen för att se till att den fungerar för testfallen ovan.
* Anropa funktionen för att räkna ut vad skulden är efter en månad om man lånar 1000 kr hos *Buffel&Båg* respektive *Lurendrejarna*.
* Skriv ut resultatet på ett begripligt sätt.

<details>
<summary markdown="span">
Tips för att skriva funktionen!
</summary>
<p>Du räknar lätt ut resultatet genom att anropa <code>cost_after_one_month</code> och sedan lägga till den tidigare skulden.
</p>
</details>
-->

## 2. Skulden växer...

Om man inte betalar skulden så växer den varje månad. Vi antar att långivarna vid varje månadsskifte räknar ut räntan på hela skulden, och sedan ökar på skulden med både räntan och månadsavgiften.

Vi skall skriva en funktion som räknar ut vad skulden är efter *m* månader:

```python
def debt_after_m_months(loan, month_rate, month_fee, m):
  ...
```

Här är några exempel på resultat efter 1 månad:
* `debt_after_m_months(1000, 11, 0, 1)`  = `1110`
* `debt_after_m_months(1000, 0, 42, 1)`  = `1042`
* `debt_after_m_months(1000, 11, 42, 1)` = `1152`

Och här är några exempel på resultat efter 2 månader:
* `debt_after_m_months(1000, 11, 0, 2)`  = `1232.1`
* `debt_after_m_months(1000, 0, 42, 2)`  = `1084.0`
* `debt_after_m_months(1000, 11, 42, 2)` = `1320.72`



**Uppdrag:**
* Skriv funktionen `debt_after_m_months`.
* Anropa funktionen så att du ser att den fungerar för testfallen ovan.
* Anropa funktionen för att räkna ut vad man är skyldig efter en månad om man lånar 1000 kr hos *Buffel&Båg* respektive *Lurendrejarna*.
* Anropa funktionen för att räkna ut vad man är skyldig efter ett år om man lånar 1000 kr hos *Buffel&Båg* respektive *Lurendrejarna*.
* Skriv ut resultaten på ett begripligt sätt.
* Hade du velat låna pengar hos någon av dessa firmor?

<details>
<summary markdown="span">
Tips för att skriva funktionen!
</summary>
<p>För att räkna ut skulden kan du loopa <code>m</code> gånger och i varje varv anropa <code>cost_after_one_month</code> för att räkna ut hur mycket skulden ökar. Du kan hålla reda på hur stor skulden är med en variabel `debt`. Glöm inte att anropa <code>cost_after_one_month</code> med aktuellt värde på skulden.
</p>
</details>

<details>
<summary markdown="span">
Kommentar om resultatet (spoiler)
</summary>
<p>Om du programmerat rätt ser du att skulden blir väldigt stor efter ett år: över 30.000 för Buffel&Båg och över 50.000 för Lurendrejarna.
</p>
</details>


## 3. Effektiv ränta

Många långivare försöker dölja hur mycket det kostar att låna genom att ha olika avgifter förutom räntan. En del påstår till och med att de inte har någon ränta alls, men har många olika avgifter i stället. Därför infördes en lag år 2010 som säger att om lånet är på mer än 3 månader så måste långivaren tala om vad den *effektiva räntan* är.

Den effektiva räntan är vad det kostar att låna under ett år, uttryckt som en årsränta i procent. Om man tar ett banklån för ett hus är den effektiva räntan ofta runt 2-5% idag (2018). Tar man ett sms-lån kan den effektiva räntan bli väldigt mycket högre...

Du kan räkna ut den effektiva räntan genom att
* räkna ut vad skulden är efter ett år (med hjälp av `debt_after_m_months`)
* subtrahera storleken på det ursprungliga lånet (då har du kvar årskostnaden för lånet)
* dividera årskostnaden med lånestorleken
* multiplicera med hundra för att få det i procent

**Uppdrag:** Skriv en funktion `effective_rate` som räknar ut den effektiva räntan, givet lånestorlek, månadsränta och månadsavgift. Vad är den effektiva räntan hos *Buffel&Båg* respektive *Lurendrejarna*? Skriv ut resultatet på ett begripligt sätt.

<details>
<summary markdown="span">
Kommentar om resultatet (spoiler)
</summary>
<p>Den effektiva räntan blir över 3000% för Buffel&Båg och över 5000% för Lurendrejarna!
</p>
</details>


## 4. Plotta skulden

För att åskådliggöra hur skulden stiger skall vi skriva ett program som plottar vad skulden är vid olika tidpunkter. Vi skall använda matplotlib, precis som i övningen [Plotta funktioner](exercises/plot).

Till vår hjälp kan vi använda följande funktion `intplot` som plottar y-värden för en funktion `f` för x-värdena 1 till och med m:

```python
import matplotlib.pyplot as plt
plt.ion()

def intplot(f, m, lbl):
  xs = [i+1 for i in range(m)]
  ys = [f(i+1) for i in range(m)]
  plt.plot(xs, ys, label=lbl)
```
(Parametern `lbl` är en sträng som används som etikett på kurvan.)

Som exempel kan vi plotta ett 100-kronors lån hos en firma med 10% månadsränta och 0 kronor i avgift på följande sätt: Skapa först en funktion som ger y-värdena för olika värden på m:

```python
def example_loan(m):
  return debt_after_m_months(100, 10, 0, m)
```

Anropa sedan `intplot` med denna funktion som argument, t.ex. för att se hur skulden växer de första 24 månaderna:

```python
intplot(example_loan, 24, "exempel-firma")
```

Sätt sedan etiketter på x och y-axeln, skriv ut funktionsetiketterna (*legend*), sätt på ett rutnät och spara plotten i en fil:

```python
plt.xlabel("månader")
plt.ylabel("kronor")
plt.title("sms-lån")
plt.legend(loc = "upper center")
plt.grid(True)
plt.savefig("plot.png")
```

Nu kan vi titta på kurvan i filen `plot.png`

**Uppdrag:** Prova att plotta exempel-lånet enligt exemplet ovan. Kör programmet och titta på det resulterande filen `plot.png`.

*Tips!* Det kan vara bra att först ha kört igenom uppgiften [Plotta funktioner](exercises/plot) för att förstå hur plottning fungerar.

**Uppdrag:** Plotta hur skulden växer de första 5 månaderna när man lånat 1000 kronor hos Buffel&Båg och Lurendrejarna. Vilken firma är minst dålig i början? Vilken är minst dålig i slutet av perioden?

**Uppdrag:** Plotta hur skulden växer det första året.

<details>
<summary markdown="span">
Kommentar om resultaten (spoiler)
</summary>
<p>Du bör se att kurvorna korsar varandra vid cirka 3.5 månader. Om du tittar på 12-månaders sikt ser du att skulden växer i allt snabbare takt (så kallad *exponentiell* tillväxt).
</p>
</details>
