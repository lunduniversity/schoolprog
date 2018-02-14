---
layout: page
title: Bråkspel
permalink: /exercises/fractions/
toc: true
type: exercise
tags:
 - medel
 - bråk
 - text
---

Detta uppdrag går ut på att programmera ett spel där datorn kan hjälpa oss att summera heltalsbråk, eller kontrollera att vi summerar rätt.

Till att börja med, vet du hur man räknar ut summan av två bråk? Till exempel:

        9472     122        ?
       –––––– + –––––  =  –––––
         42      257        ?

Om du är osäker, gör följande lilla [övning](exercise1.md).

Om du vet hur man gör, skriv först ner hur man gör i det generella fallet. Alltså, vad skall resultatet bli om vi inför variablerna `a`, `b`, `c`, `d` för de två bråken?

       a     c          ?
      ––– + –––   =   –––––
       b     d          ?

När du funderat ut detta så kan du börja med uppgiften nedan.

Bråkspel
========

För att programmera spelet behöver du lösa några centrala delproblem:

* Hitta på hur ett bråk skall representeras. Vi rekommenderar *tuplar*. Se [tips om tuplar](../../programming/general/tuples.md).
* Skriva en funktion som kan summera två bråk. Se [tips om funktioner](../../programming/general/functions.md).
* Skriva en funktion som kan läsa in två bråk och skriva ut summan. Se [tips om att läsa in och skriva ut](../../programming/general/consoleio.md).

Vet du hur tuplar, funktioner och inläsning och utskrift fungerar? Då är det bara att sätta igång. Titta annars på tipsen ovan.

Tycker du att du är klar med spelet? Gå vidare:

* Låt någon annan prova spelet. Fungerar det som det ska? Är det lätt för användaren att förstå vad man skall göra när man kör spelet?
* Visa koden för någon annan. Kan de förstå vad programmet gör? Går något att förbättra så det blir tydligare?
* Hur kan du bygga ut ditt spel? Se ideerna nedan för att utöka spelet.

Utöka Bråkspelet
================

Här är ideer om hur du kan utöka spelet. Du kan säkert hitta på fler.

 - Du räknar
   - Använd random för att låta programmet skapa nya bråk där du som användare skall räkna ut summan. Låt programmet kontrollera om du räknat rätt.
 - Generera lästal
   - Matteböckerna brukar innehålla "lästal" typ "Kalle har ett halvt äpple. Lisa har två och ett kvarts. Hur många äpplen har de tillsammans?". Du kan säkert hitta på roligare lästal. Programmera dina egna lästal och låt kompisarna prova.
 - Visualisera bråk
   - Det kan vara bra att visualisera ett bråk, t.ex. genom att rita tårtbitar (fyrkantiga eller runda tårtor), eller något annat. Skriv ett program som kan visualisera bråk.
 - Förenklade bråk
   - Lägg till stöd i ditt program för att förenkla bråket så mycket som möjligt (hitta gemensamma delare för täljare och nämnare, och förkorta bort dem).
 - Lägg ihop fler än två
   - Stöd att man kan lägga ihop fler än två bråk.
 - Subtrahera
   - Stöd för att subtrahera bråk och inte bara addera.
