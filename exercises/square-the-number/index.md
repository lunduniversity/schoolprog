---
layout: default
title: Kvadrera talet
permalink: /exercises/square-the-number/
toc: true
type: exercise
tags:
 - nybörjare
 - text
 - input/output
 - typer
 - sträng-konkatenering
 - enkla beräkningar
 - kvadrat
 - hypotenusa
---
# Kvadrera talet
I denna uppgift får du träna på att låta programmet skriva ut och läsa in text. Vi experimenterar också med typer på värden.
Sedan har vi tillräckligt med kunskaper för att programmera enkla matte-tal med in och utdata, t.ex. kvadrera ett tal.

Vi kör Python 3 i denna uppgift, och har inte tillgång till någon sköldpadda. Koden är provkörd på [http://replit.com/languages/python3](http://replit.com/languages/python3) (Python 3).

## 1. Hello world!

Det enklaste program man kan tänka sig är ett som skriver ut en text när man kör det, t.ex. *Hello world!*. Så här ser detta program ut i Python 3:

```python
print("Hello world!")
```

**Uppdrag:** Skriv in programmet och kör det. Var dyker texten upp? Ändra texten som skrivs ut till något annat, t.ex. "Hej svejs i lingonskogen!"

Texten dyker upp i den så kallade *console*-vyn. Kärt barn har många namn, och denna vy kallas också för t.ex. *terminalfönstret*, eller *kommandoraden*.

(Dessa termer härstammar från datorns barndom innan det fanns grafiska skärmar med fönster och pixlar. Då styrde man datorn från en "console" eller "terminal" som hade en enkel textskärm och där man skrev kommandon som text-rader.)

*Tips* Om du använder Python-turtle-miljön så kommer inte åäö att fungera. Även andra saker fungerar annorlunda, så vi rekomenderar dig att använda python 3-miljön som är länkad till ovan.

## 2. Inläsning

Nu skall vi ändra programmet så det kan *läsa in*, och inte bara *skriva ut* något. Följande program frågar vad du heter, och hejar sedan på dig:

```python
namn = input("Vad heter du?")
print("Hejsan " + namn)
```
**Uppdrag:** Skriv in programmet och kör det. Fundera sedan över vad som händer när programmet körs och i vilken ordning. Titta sedan på svaret nedan.


<details>
<summary markdown="span">
Svar:
</summary>
<ol>
<li><i>input</i>-funktionen skriver ut texten "Vad heter du?" och väntar på svar.</li>
<li>Användaren skriver in ett svar, t.ex. "Lisa", och trycker på return.</li>
<li>Programmet fortsätter köra och lagrar svaret ("Lisa") i variabeln <i>namn</i>.</li>
<li>Programmet lägger ihop texten "Hejsan " med texten i variabeln <i>namn</i> till den längre texten: "Hejsan Lisa".</li>
<li><i>print</i>-funktionen anropas och skriver ut den längre texten, "Hejsan Lisa".</li>
</ol>
</details>

*Kommentar:* Texten som `input`-funktionen skriver ut kallas *ledtext* eller *prompt*.

## 3. Strängar och konkatenering

Texter, som t.ex. "Hejsan" och "Vad heter du?", kallas *strings* på engelska, och på svenska säger vi *strängar*.

Observera att strängar kan *läggas ihop* med plustecknet. Det betyder att de läggs efter varann till en längre sträng. Om vi t.ex. lägger ihop
```python
"Hej" + "Svejs"
```
så blir resultatet:
```python
"HejSvejs"
```

Att lägga ihop två strängar kallas också att man *konkatenerar* dem.

**Uppdrag:** Ändra programmet så att det skriver ut t.ex. "Hejsan Lisa! Kul att träffas!" (när du svarat "Lisa").

Det programmet skriver ut kallas *utdata*. Det programmet läser in kallas *indata*.

## 4. Om typer

Värden i datorn kan vara av olika *typer*. T.ex. *sträng*, *heltal*, och *decimaltal*. På engelska kallas de *string*, *integer* och *float*.

När man anropar en funktion med en parameter, så förväntar sig oftast funktionen att parametern skall ha en särskild typ, t.ex. heltal. Råkar man skicka in ett värde av fel typ, t.ex. en sträng i detta fall, så kan funktionen krascha eller räkna ut fel sak.

I Python kan man ta reda på typen på ett värde med funktionen `type`. T.ex. kan man skriva ut typen på värdet `7+3` på följande sätt:

```python
print(type(7+3))
```

I Python 3 representeras typerna av något som kallas *klasser*, och ovanstående program skriver ut

```python
<class 'int'>
```

vilket betyder att `7` har typen *int*, vilket är kort för *integer*, alltså ett heltal.

För att förstå typer bättre skall vi experimentera lite:

**Uppdrag:** Använd `print` och `type` för att ta reda på typen för följande uttryck:
  * `5.2`
  * `3`
  * `3 + 3`
  * `5.2 + 5.2`
  * `3 + 5.2`
  * `"hej"`
  * `"hej" + "svejs"`

Som du ser kan man ibland lägga ihop värden som är av *olika* typ, t.ex. (`3 + 5.2`). När detta uttryck beräknas kommer Python att först göra om heltalet `3` till decimaltalet `3.0`, och sedan lägga ihop det med `5.2`. Resultatet blir ett decimaltal (en *float*).

### 4.1 Typfel

Det är inte alltid man kan kombinera värden av olika typer.

**Uppdrag:** Ta reda på typen för följande uttryck:
```python
3 + "vligt"
```
<details>
<summary markdown="span">
Svar:
</summary>
<p>När du försöker köra ett program med ovanstående uttryck i Python 3 så får du följande fel:
<pre>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
</pre>
Det betyder alltså att Python 3 <i>inte</i> stödjer att man lägger ihop heltal med strängar. Programmet kraschar när man försöker göra detta.
</p>
</details>

### 4.2 Typomvandling till sträng

Om du hade tänkt dig att uttrycket ovan skulle räknas ut till strängen `"3vligt"`, så måste du själv först göra om heltalet `3` till strängen `"3"`. Det kan du gära med hjälp av funktionen `str` som gör om heltal eller decimaltal (eller andra typer) till strängar:

```python
str(3) + "vligt"
```
**Uppdrag:** Ta reda på värdet och typen av detta uttryck.

<details>
<summary markdown="span">
Tips:
</summary>
<p>Du kan skriva ut värdet med:
<pre>
print(...)
</pre>
och typen med
<pre>
print(type(...))
</pre>
</p>

</details>

### 4.3 Sträng-interpolering: skriv strängar som innehåller tal

Följande program skriver ut vad klockan är (på den dator där programmet körs):

```python
import datetime
now = datetime.datetime.now()
print("Klockan är " + str(now.hour) + ":" + str(now.minute) + " på den här datorn!")
```
Det kan kännas lite krångligt att behöva omvandla talen till strängar och använda strängkonkatering. Men det finns ett enklare sätt:

```python
import datetime
now = datetime.datetime.now()
print(f"Klockan är {now.hour}:{now.minute} på den här datorn!")
```

Detta kallas *stränginterpolering*, det vill säga att en text ändras genom att andra värden stoppas in på olika ställen i den. De andra värdena, som `now.hour` och `now.minute`, omvandlas automatiskt till strängar. För att denna formattering skall fungera behöver man skriva ett litet `f` framför strängen: `f"..."`. På engelska kallas detta *string interpolation*.

**Uppdrag:** Skriv ett program som använder stränginterpolering för att skriva ut vad klockan är, inklusive sekunder. (Använd `now.second`.)

### 4.4 Typomvandling till heltal

Ibland kan man behöva omvandla strängar till tal, t.ex. när man läser in med `input`-funktionen.

Man kan omvandla strängar till heltal med funktionen `int`.

**Uppdrag:** Ta reda på typen för
  * `"42"`
  * `int("42")`

`int`-funktionen är praktisk t.ex. när man vill läsa in ett tal med `input`-funktionen. Resultatet av `input`-funktionen är alltid en sträng.

**Uppdrag:** Ta reda på typen på `x` respektive `y` i nedanstående program.

```python
x = input("Skriv ett tal: ")
y = int(input("Skriv ett tal"))
```

<details>
<summary markdown="span">
Svar:
</summary>
<p>
<code>x</code> är en sträng. <code>y</code> är ett heltal.
</p>
</details>

### 4.5 Logiska värden (Boolean)

Om man jämför två tal får man ett *logiskt* värde, som antingen är sant (`True`) eller falskt (`False`). Sådana värden kallas också *Booleska* värden (eller *Boolean* på engelska) efter matematikern George Boole (1815-1864).

**Uppdrag:** Ta reda på vad typen är på följande uttryck: `4 < 5`. Ta också reda på vad värdet är.

<details>
<summary markdown="span">
Svar:
</summary>
<p>
Typen är <i>bool</i>, alltså boolean. Värdet är <i>True</i>, alltså sant.
<pre>
print(type(4<5))
print(4<5)
</pre>

</p>
</details>

### 4.6 Floats är inte exakta

Decimaltal representeras med *flyttal* (floats) i datorn. Floats är inte exakta, utan approximativa värden. Anledningen är att de representeras av ett fixt antal *bitar* där varje bit är noll eller ett.

**Uppdrag:** Prova vad `7.2 - 7.1` har för värde.

<details>
<summary markdown="span">
Svar:
</summary>
<p>
Du kan göra:
<pre>
print(7.2 - 7.1)
</pre>
Du ser att 7.2 - 7.1 inte är exakt 0.1.
</p>
</details>

## 5. Kvadrera talet

Nu när vi har ett hum om hur in och utdata och typer fungerar kan vi programmera enkla matte-tal.

**Uppdrag:** Skriv ett program som frågar efter ett tal och skriver ut vad kvadraten av talet är.

Här är exempel på körning, med utdata i blått och indata i rött.

<p>
<font color="blue">Skriv ett tal jag skall kvadrera: </font><font color="red">5</font><br>
<font color="blue">Kvadraten av 5 är 25</font>
</p>

<details>
<summary markdown="span">
Lösning:
</summary>
<pre>
tal = int(input("Skriv ett tal jag skall kvadrera: "))
kvadrat = tal * tal
print(f"Kvadraten av {tal} är {kvadrat}")
</pre>
</details>

## 6. Beräkna hypotenusan av en rätvinklig triangel

**Uppdrag:** Skriv ett program som frågar användaren efter längden på två kateter hos en rätvinklig triangel och skriver ut hypotenusan som svar.

Exempel på ett par körningar, med utdata i blått och indata i rött:

<p>
<font color="blue">Jag kan räkna ut hypotenusan för en rätvinklig triangel.<br>
Hur lång är den ena kateten?</font> <font color="red">3</font><br>
<font color="blue">Och hur lång är den andra?</font> <font color="red">4</font><br>
<font color="blue">Enkelt! Hypotenusan är 5.0</font>
</p>


<p>
<font color="blue">Jag kan räkna ut hypotenusan för en rätvinklig triangel.<br>
Hur lång är den ena kateten?</font> <font color="red">5</font><br>
<font color="blue">Och hur lång är den andra?</font> <font color="red">3</font><br>
<font color="blue">Enkelt! Hypotenusan är 5.830951894845301</font>
</p>

*Tips* För att räkna ut en kvadratrot kan du använda Pythons bibliotek `math`:

```python
import math
...
...math.sqrt(...)...
...
```

## 7. Extra: Hitta på en egen beräkning

**Uppdrag:** Hitta på en egen beräkning där användaren skriver in tal och programmet räknar ut något. Några ideer:
  * Arean på en rätvinklig triangel
  * Omkretsen på en cirkel (använd `math.pi`)
  * Volymen på ett rätblock
  * ...
