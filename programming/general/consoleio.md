---
layout: page
---

Inläsning och utskrifter
========================

Här kommer lite tips om hur man läser in och skriver ut text på "console-fönstret"<sup>1</sup>.

Utskrift
--------

|                    | Scala             | Python         |
|:-------------------|:------------------|:---------------|
| Skriv ut text      | `println("hej")`  | `print("hej")` |
| Skriv ut tal       | `println(5)`      | `print(5)`     |
| Skriv ut variabel  | `println(x)`      | `print(x)`     |

<br>

Man kan också blanda olika slags värden i en utskrift.

I Scala så kan man konkatenera ihop strängar och tal direkt genom att "plussa":

```scala
// Scala
println("Jag är " + 172 + " cm lång.")
```

I Python behöver tal explicit göras om till strängar med `str` innan man "plussar" för att konkatenera:

```python
# Python
print("Jag är " + str(172) + " cm lång.")
```


Inläsning
---------

Ofta startar man ett program genom att klicka på en ikon, t.ex. på en mobiltelefon eller på en vanlig dator. Man kan också starta ett program genom att skriva dess namn i ett "terminalfönster" på datorn, eller genom att klicka RUN inifrån en programmeringsmiljö.

Terminalfönstret kallas ofta "console", och även om man startar programmet genom att klicka igång det, så har man ofta ett "console-fönster" där programmet kan skriva ut och läsa in text.

## Python

Läs in en text:

```python
print("Vad heter du?")
namn = input()
print("Hej " + namn + "!")
```

Läs in ett heltal:

```python
print("Hur gammal är du?")
age = int(input())
```

## Scala

**Notera:** Inläsning i Scala fungerar tyvärr för närvarande inte i online-miljöer som kojojs eller scalafiddle (Februari 2018), utan bara om man har laddat ner en Scala-miljö på sin dator.

Läs in en text:

```scala
val namn = scala.io.StdIn.readLine()("Vad heter du? ")
println("Hej " + namn + "!")
```

Läs in ett heltal:

```scala
print("Hur gammal är du?")
val age = scala.io.StdIn.readInt()
```
