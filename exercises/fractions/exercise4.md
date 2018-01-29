Hur man räknar ut summan av två bråk (4:4)
==========================================

Problemet var alltså: Om du har följande två bråk, hur skall du skriva om dem för att de skall få samma nämnare?

       a     c           ??     ??         ??
      ––– + –––    =    –––– + ––––   =  ––––––
       b     d           ??     ??         ??

Jo, vi kan få en gemensam nämnare genom att multiplicera vänstra bråket med `d/d` och högra bråket med `b/b`. Både `d/d` och `b/b` har ju värdet `1`, så vi har inte ändrat värdena på bråken.

För vänstra bråket får vi alltså:

     a         a     d           ad
    –––   =   ––– . –––    =    ––––
     b         b     d           bd

Och för högra bråket får vi:

     c         b     c           bc
    –––   =   ––– . –––    =    ––––
     d         b     d           bd

Alltså kan vi skriva om summan av bråken så här:

     a     c         ad     bc        ad + bc
    ––– + –––   =   –––– + ––––   =   –––––––
     b     d         bd     bd          bd

Nu är det dags att programmera! Gå tillbaka till [uppdraget](README.md).
