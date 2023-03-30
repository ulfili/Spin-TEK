# Spin-TEK
Spin TEK testülesanne
Juhend rakenduse kasutamiseks. 

Selleks, et rakendust avada, peab kindlaks tegema, kas Python on arvutisse seadistatud
ning kas Pythonis on sellised moodulid nagu argparse, datetime, holidays.
Kui ei ole, siis terminali saab kirjutada järmist rida "pip install argparse datetime holidays"
Nüüd peaks kõik olema seadistatud ning võib alustada järgmiste sammudega:

1. Salvestage koodi (dateCalculator.py).
2. Avage terminal (Command prompt) ning valige õige tee koodini (cd + C:\Users\User\...)
3. Looge fail. Selleks kirjutage terminalis "python dateCalculator.py year", kus "year" on aasta, 
mis kuupäevi te soovite näha. Kirjutage aasta numbritega (nt python dateCalculator.py 2023)
4. fail salvestub nimega "year.csv" (nt 2023.csv)

Fail on loodud. 
Kui te soovite avada faili excelis:
- avage fail
- valige üleval exceli menüüst "data" -> "get data" -> "from text/csv" 
- valige fail "year.csv"
- järgmisena vali "delimiter" -> "tab" -> "save"

Saab avada ka teises rakenduses, näiteks notepade'is vajutades parema hiirega faili peale, valida "open with" ning valida sobiv rakendus. 
