---
layout: page
title: Derivera funktioner
permalink: /exercises/derivative/
toc: true
type: exercise
tags:
 - intermediate
 - functions
 - plotting
---
I denna uppgift kommer du att träna mer på funktioner. Du kommer även att få se hur man kan använda Python för att plotta funktioner och derivera dem.

Koden i denna uppgift är provkörd på [http://repl.it/languages/python3](http://repl.it/languages/python3) (Python 3).

### 1. Vi undersöker en funktion

Vi ska undersöka följande funktion:

<img src="g.png">

**Uppdrag:** Skapa ett Python-program med funktionen `g` enligt ovan, definierad som en (vanlig) Python-funktion. Lägg till en utskrift i ditt program, så att funktionens värde för x = 2, dvs `g(2)`, skrivs ut.

Resultatet som skrivs ut ska vara ungefär -0.34.

<details>
<summary markdown="span">
Tips
</summary>
<p>
<pre>
import math

def g(x):
  return # ...
...
print(g(2))
</pre>
</p>
</details>

### 2. Plotta funktionen

Att skriva ut ett enda funktionsvärde, som ovan, säger oss inte speciellt mycket om hur funktionen ser ut. En graf vore mycket bättre. Vi vill istället plotta funktionen för x-värden från 0 till 10.

Använd samma teknik för plottningen som du prövat i uppgiften "Plotta funktioner". Använd gärna den funktion `fplot` som finns där. Om du gjort en egen variant (exempelvis för att sätta etiketter på funktionerna) går det att använda den också.

**Uppdrag:** Modifiera ditt program så att funktionen `g(x)` plottas för x-värden i intervallet 0 <= x < 10. Glöm inte spara grafen i en fil, så att du kan se den.

### 3. Derivera numeriskt

Vi intresserar oss nu för funktionens derivata, g'(x). Det är fullt möjligt att derivera funktionen symboliskt (med hjälp av deriveringsreglerna). Här ska vi emellertid plotta g'(x) på ett annat sätt, nämligen genom att låta datorn **beräkna** derivatans värde för varje x-värde.

För detta använder vi derivatans definition:

<img src="fprime.png">

Ofta ser man detta samband som ett gränsvärde, där man tänker sig h gå mot 0 (noll). Här ska vi istället använda sambandet som utgångspunkt för att beräkna derivatan av en funktion `f` för x-värdet `x`. Vi kommer därför att välja ett "lagom" litet h-värde. Du kommer strax att få se hur det går till.

**Uppdrag:** Inför en Python-funktion `gderiv` i ditt program. Dess resultat är funktionen `g`:s derivata för värdet `x`. Använd derivatans definition (ovan) för beräkningen.

Din Python-kod kan se ut i stil med följande:

```python
def gderiv(x):
  h = 0.00001
  return # ... fyll i derivataberäkning här
```

**Uppdrag:** Ändra ditt program så att `g` och `gderiv` plottas i samma bild.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Du behöver två <code>fplot</code>-rader: ett för <code>g</code> och ett för <code>gderiv</code>.
</p>
</details>

Den första funktionen ritas i blått, den andra i orange.

**Uppdrag:** Är derivatan rimlig?

<details>
<summary markdown="span">
Tips
</summary>
<p>
När <code>g</code> har ett lokalt minimum ska derivatan vara noll.
När <code>g</code> pekar som brantast uppåt ska derivatan ha ett lokalt maximum.
</p>
</details>

### 4. Testa några möjliga derivator

Som vi redan nämnt kan man även derivera `g` symboliskt, det vill säga med hjälp av deriveringsreglerna.

De tre vännerna Bent, Alva och Kit har försökt göra detta, men det är länge sedan de gick i gymnasiet, och endast ett vagt minne av deriveringsreglerna återstår. De kommer fram till olika svar:

<img src="sx.png">

**Uppdrag:** Använd Python för att ta reda på vilken av derivatorna `s1`, `s2` och `s3` som bäst stämmer överens med den beräknade (`gderiv`). Vem av de tre kan sina deriveringsregler bäst?

Du ska alltså **inte** använda dina egna kunskaper om deriveringsreglerna i denna uppgift.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Du kan exempelvis införa en funktion som följer:
<pre>
def diff1(x):
  return gderiv(x) - s1(x)
</pre>
Plotta funktionen.
Den visar hur mycket <code>gderiv</code> och <code>s1</code> skiljer sig åt. Om de är helt lika blir skillnaden 0, och då ska grafen för <code>diff1</code> ju bli en horisontell, rät linje. (I praktiken blir värdena inte exakt 0, men mycket små.)
</p>
</details>

### 5. Gör en mer generell funktion för numerisk derivering

Titta på din funktion `gderiv` igen. Den är specifikt gjord för att beräkna ett derivatavärde för `g`: om du vill derivera en annan funktion på samma sätt behöver du göra en ny variant på `gderiv`. Det är opraktiskt i längden.

Istället ska vi nu göra en generell funktion, som kan få heta `deriv`. Den funktionen ska ta *två* parametrar, en funktion `f` att derivataberäkna, samt (som tidigare) ett `x`-värde. Derivatan av `f` beräknas som tidigare, men `f` är alltså nu en parameter.

Idén är att du nu ska kunna skriva `gderiv` enklare. Och nästa gång du behöver beräkna ett derivatavärde för en funktion kan du också, på motsvarande sätt, göra det rätt enkelt.

```python
def deriv(f, x):
  h = 0.00001
  return ... # derivatan av f

# derivatan av g, som nu kan skrivas enklare
def gderiv(x):
  return deriv(g, x)
```

**Uppdrag:** Skriv färdigt funktionen `deriv` enligt ovan. Skriv om `gderiv` så att den använder `deriv`, också enligt ovan. Plotta `g` tillsammans med sin derivata. Ser derivataberäkningen ut att fungera?

### 6. Använd anonyma funktioner för att förenkla ditt program

I uppgiften "Plotta funktioner" prövade du att använda anonyma funktioner (lambdas). Gå gärna tillbaka till den uppgiften om du behöver repetera hur de fungerar.

Med hjälp av en sådan anonym funktion kan man helt låta bli definiera `gderiv` enligt ovan. Det räcker med `g` och `deriv`.

**Uppdrag:** Förenkla ditt program så att `g` och dess derivata plottas, men istället för att plotta `gderiv` använder du en kombination av en anonym funktion, `deriv` och `g`.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Du behöver två <code>fplot</code>-rader, i stil med följande:
<pre>
fplot(g, 0, 10, "g")
fplot(lambda x: ..., 0, 10, "g'")
</pre>
Här ska <code>...</code> ersättas med ett lämpligt uttryck. Du ska alltså <b>inte</b> använda <code>gderiv</code>. (Notera också att vi här utgått från att din <code>fplot</code>-funktion tar funktionens ettikett som fjärde parameter; du kan ev. behöva justera dessa detaljer för att passa in egen <code>fplot</code>.) 
</p>
</details>

### 7. Plotta fler funktioner enkelt

Ovan har du använt funktioner som parametrar och anonyma funktioner. Du har även skapat en praktisk funktion som kan beräkna derivatavärdet för en godtycklig funktion `f` och ett godtyckligt `x`-värde. Med hjälp av dessa byggstenar kan du lätt plotta andra funktioner och deras derivator.

**Uppdrag:** Plotta följande två funktioner tillsammans med sina derivator, i intervallet -1 <= x <= 1. Du ska **inte** införa några nya, namngivna funktioner (med `def`), utan göra detta med de byggstenar som just nämnts.

| funktion | namn i Python |
| --------- | ----------------- |
| sinus | `math.sin`|
| absolutvärde | `abs`  eller `math.fabs` |

**Uppdrag:** Plotta den naturliga logaritmen (`math.log`) på samma sätt, i samma intervall.

Vad beror felmeddelandet på?

<details>
<summary markdown="span">
Tips
</summary>
<p>
Logaritmen log(x) är inte definierad för x=0. Vad är derivatan av log(x)? Varför kan den inte fungera för x=0?
</p>
</details>

**Uppdrag:** Justera intervallet till något mer meningsfullt, och pröva igen.

<details>
<summary markdown="span">
Tips
</summary>
<p>
Kom ihåg att du måste välja rätt intervall på två ställen: både för funktionen och för dess derivata.
</p>
</details>
