Använd riktig väderdata för att analysera hur temperaturen förändrats i Sverige de senaste 50 åren.
==========================================================================================================

I den här uppgiften kommer vi använda python för att analysera data som är jobbig att räkna på för hand.

Datan har hämtats från SMHIs öppna databas, men den är redan nedladdad åt dig.

I filen ```api.py``` finns det några funktioner som är användbara för att lösa den här uppgiften.

Det finns en funktion som heter ```get_station_data```, denna funktion öppnar och läser en komprimerad fil med väderdata.
Datan returneras i en ```dict```, som använder väderstationsnamn som nycklar. 

För att skriva ut vilka väderstationer som finns kan ni skriva följande:

```python
import api
data = api.get_station_data()
print(data.keys())
```

Om ni lägger till följnade 
```python
lund = data['Lund']
print(lund[:10])
```
Hamnar Lunds data i variabeln `lund` och ni printar de `10` första datapunkterna för Lund.

# Uppgifter
- Skapa två listor `time` och `temp` som innehåller tiden repsektive temperatur för varje datapunkt. 
- Plotta temperaturerna genom `api.plot(y=temp)`. Vill ni själva välja filnamnet kan detta göras genom `api.plot(temp, fname='myplot.png')`.
- Filtrera ut alla temperaturer uppmätta under 2016 och plotta dessa, för att se hur temperaturen varierar under ett år.
- Skapa en funktion `avg(temp)` som beräknar medelvärdet av en lista med temperaturer.
- Använd funktionen `avg` för att beräkna medeltemperaturen i lund för varje år och platta alla dessa.
- Använd funktionen `avg` för att beräkna medeltemperaturen i varje stad som finns i datasetet för varje år. Beräkna sedan medelvärdet av dessa medelvärden och plotta det gemensamma medelvärdet för varje år.



# Fortsättningsuppgifter
- Instructions for calculating yearly average (standard deviation) for a station.
- Download more data from SMHI by exploring their API
- Download more data from other sources?
