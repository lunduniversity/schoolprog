# Math Exerciser

## Motivering

Du har hört det sägas att "repetition är kunskapens moder" och vill därför sitta och göra så många mattetal du kan. Matteboken är bra men den har vissa begränsningar:
- att bläddra sidor slösar på din dyrbara övningstid
- du kan inte öva på vad du vill
- uppgifterna kan när som helst ta slut!

Du hade kanske kunnat använda dina nyvunna programmeringskunskaper för att skriva ett matte-övningsprogram!

## Outline

1. Skriv en lista med frågor.
2. Använd `input` funktionen för att be användaren om svaret till frågan.
3. Jämför användarens svar med det sanna svaret och ge feedback t.ex. "Rätt svar!"

## Genomgång

Vi vill göra en lista med de frågor vi vill ställa och deras svar. Ett sådant par av en fråga och frågans svar kan man i python skriva med en `tuple`:

```python
question = ("Vad är kunskapens moder?", "repetition")
```

dessa par kan man sen spara i en lista

```python
questions = [("Vad är kunskapens moder?", "repetition"),("Vilken funktion används i python för att skriva text till kommandotolken?", "print")]
```

Ditt program kan sen plocka en slumpmässig fråga ur listan och presentera den till användaren.

