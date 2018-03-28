---
layout: page
title: Kvadrera talet
permalink: /exercises/square-the-number/
toc: true
type: exercise
tags:
 - beginner
 - console i/o
 - types
---
I denna uppgift får du träna på att låta programmet skriva ut och läsa in text. Vi kör Python 3 i denna uppgift, och har inte tillgång till någon sköldpadda. Vi experimenterar också med typer på värden.

Koden i denna uppgift är provkörd på [http://repl.it/languages/python3](http://repl.it/languages/python3) (Python 3).

### 1. Hello world!

Det enklaste program man kan tänka sig är ett som skriver ut en text när man kör det, t.ex. *Hello world!*. Så här ser detta program ut i Python 3:

```python
print("Hello world!")
```

**Uppdrag:** Skriv in programmet och kör det. Var dyker texten upp? Ändra texten som skrivs ut till något annat, t.ex. "Hej svejs i lingonskogen!"

Texten dyker upp i den så kallade *console*-vyn. Kärt barn har många namn, och denna vy kallas också för t.ex. *terminalfönstret*, eller *kommandoraden*.

(Dessa termer härstammar från datorns barndom innan det fanns grafiska skärmar med fönster och pixlar. Då styrde man datorn från en "console" eller "terminal" som hade en enkel textskärm och där man skrev kommandon som text-rader.)

### 2. Om inläsning, strängar, och konkatenering

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
<li>Programmet skriver ut texten "Vad heter du?" och väntar på svar.</li>
<li>Användaren skriver in ett svar, t.ex. "Lisa", och trycker på return.</li>
<li>Programmet fortsätter köra och lagrar svaret ("Lisa") i variabeln <i>namn</i>.</li>
<li>Programmet lägger ihop texten "Hejsan " med texten i variabeln <i>namn</i> till den längre texten: "Hejsan Lisa".</li>
<li>Programmet skriver ut den längre texten, "Hejsan Lisa".</li>
</ol>
</details>

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

### 3. Om typer

Värden i datorn kan vara av olika *typer*. T.ex. *sträng*, *heltal*, och *decimaltal*. På engelska kallas de *string*, *integer* och *float*.

I Python kan man ta reda på typen på ett värde med funktionen `type`. T.ex. kan man skriva ut typen på värdet `7` på följande sätt:

```python
print(type(7))
```

I Python 3 representeras typerna av något som kallas *klasser*, och ovanstående program skriver ut

```python
<class 'int'>
```

vilket betyder att `7` har typen *int*, vilket är kort för *integer*, alltså ett heltal.

**Uppdrag:** Ta reda på typen för följande uttryck:
  * `5.2`
  * `3`
  * `3 + 3`
  * `5.2 + 5.2`
  * `3 + 5.2`
  * `"hej"`
  * `"hej" + "svejs"`

Som du ser kan man ibland lägga ihop värden som är av *olika* typ, t.ex. (`3 + 5.2`). När detta uttryck beräknas kommer Python att först göra om heltalet `3` till decimaltalet `3.0`, och sedan lägga ihop det med `5.2`. Resultatet blir ett decimaltal (en *float*).

**Uppdrag:** Försök ta reda på typen för följande uttryck
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
Det betyder alltså att Python 3 <i>inte</i> stödjer att man lägger ihop heltal med strängar.
</p>
</details>


Om du hade tänkt dig att uttrycket skulle räknas ut till strängen `"3vligt"`, så måste du själv först göra om heltalet `3` till strängen `"3"`. Det kan du gära med hjälp av funktionen `str` som gör om olika typer av värden till strängar:

```python
str(3) + "vligt"
```

**Uppdrag:** Ta reda på typen av ovanstående uttryck.

Man kan omvandla strängar till tal med funktionen `int`.

**Uppdrag:** Ta reda på typen för `int("42")`

### 4. Kvadrera talet

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
print("Kvadraten av " + str(tal) + " är " + str(kvadrat))
</pre>
</details>

### 5. Beräkna hypotenusan av en rätvinklig triangel

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

### 6. Extra: Hitta på en egen beräkning

**Uppdrag:** Hitta på en egen beräkning där användaren skriver in tal och programmet räknar ut något. Några ideer:
  * Arean på en rätvinklig triangel
  * Omkretsen på en cirkel (använd `math.pi`)
  * Volymen på ett rätblock
  * ...
