---
layout: page
title: Math Exerciser
permalink: /exercises/math-exerciser/
tags: 
 - avancerad
 - funktioner
toc: true
---

## Motivering

Du har hört det sägas att "repetition är kunskapens moder" och vill därför sitta
och göra så många mattetal du kan. Matteboken är bra men den har vissa
begränsningar:
- du kan inte öva på vad du vill
- att bläddra sidor slösar på din dyrbara övningstid
- uppgifterna kan när som helst ta slut!

Du hade kanske kunnat använda dina nyvunna programmeringskunskaper för att
skriva ett matte-övningsprogram!

## Outline

1. Skriv en lista med frågor.
2. Använd `input` funktionen för att be användaren om svaret till frågan.
3. Jämför användarens svar med det sanna svaret och ge feedback t.ex. "Rätt svar!"

## Genomgång

Vi vill göra en lista med de frågor vi vill ställa och deras svar. Ett sådant
par av en fråga och frågans svar kan man i python skriva med en `tuple`:

```python
question = ("Vad är kunskapens moder?", "repetition")
```

dessa par kan man sen spara i en lista

```python
questions = [("Vad är kunskapens moder?", "repetition"),("Vilken funktion används i python för att skriva ut text i kommandotolken?", "print")]
```

Ditt program kan sen plocka en slumpmässig fråga ur listan och presentera den
till användaren.

Vi har fortfarande inte riktig löst problemet med att uppgifterna tar slut, det
kan bli väldigt jobbigt att skriva alla matteuppgifter du vill öva på. Vi kan
använda programmeringsknep för att göra det lättare! Om du vill öva på femmans
multiplikationstabell kan du lägga till alla frågor

```python
for i in range(1, 11):
    questions.add(('Vad är "5 * {}"?'.format(i), 5 * i))
```
