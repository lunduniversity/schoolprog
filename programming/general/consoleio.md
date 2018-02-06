Inläsning och utskrifter
========================

Här kommer lite tips om hur man läser in och skriver ut text på "console-fönstret"<sup>1</sup>.

Utskrift
--------
|                    | Scala              | Python       |
|:-                  |:------------------|:------------|
|Skriv ut text       |`println("hej")`    |`print("hej")`|
|Skriv ut tal        |`println(5)`        |`print(5)`    |
|Skriv ut variabel   |`println(x)`        |`print(x)`    |

Man kan blanda olika slags värden i en utskrift. I Scala:

    # Scala:
    println("Jag är " + 172 + " cm lång.")

I Python: (talen behöver göras om till strängar med `str`)
    # Python:
    print("Jag är " + str(172) + " cm lång.")



Inläsning
---------
|                    | Scala              | Python       |
|:-                  |:------------------|:------------|
|Läs in en text      |`val namn = readLine("Vad heter du? ")`|`print("Vad heter du?")`<br>`namn = input()`|
|Läs in ett heltal   |`print("Hur gammal är du?")`<br>`val age = readInt()` |`print("Hur gammal är du?")`<br>`age = int(input())`    |

BRASKLAPP 1: Jag får inte Scala-inläsningen ovan att fungera i online-kojo. Hur gör man??



<sup>1</sup>Ofta startar man ett program genom att klicka på en ikon, t.ex. på en mobiltelefon eller på en vanlig dator. Man kan också starta ett program genom att skriva dess namn i ett "terminalfönster" på datorn, eller genom att klicka RUN inifrån en programmeringsmiljö.

Terminalfönstret kallas ofta "console", och även om man startar programmet genom att klicka igång det, så har man ofta ett "console-fönster" där programmet kan skriva ut och läsa in text..
