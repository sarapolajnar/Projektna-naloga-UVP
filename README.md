# Projektna-naloga-UVP: 
## Analiza teka žensk na 60m

Avtorica: Sara Polajnar

### Uvod 
Glavna ideja analize in navdih izhajata iz vprašanja: "Ali res ljudje afriškega porekla dosegajo najboljše rezultate predvsem na šprintih in tekih na srednje razdalje?" V nalogi sem za ciljno skupino vzela ženske iz celega sveta in naredila analizo teka na 60m. Vsi podatki so bili dne 10.10.2024 zajeti iz [spletne strani](https://worldathletics.org/records/toplists/sprints/60-metres/all/women/senior/2024?regionType=world&timing=electronic&windReading=regular&page=1&bestResultsOnly=true&maxResultsByCountry=all&eventId=10229684&ageCategory=senior). Tekom analize pa so se pojavile še različne druge možnosti za primerjavo podatkov:

#### Kako se rezultati razlikujejo:
- glede na starost?
- glede na državljanstvo
- glede na mesec rojstva
- glede na letni čas dogodka (vpliv okoljskih dejavnikov, predvsem temperature)

### Navodila za uporabo
Za uspešen vpogled v analizo mora imeti uporabnik nameščene naslednje knjižnice: beautifulsoup, pandas, requests, os, csv, json
Celotna analiza se nahaja v datoteki z imenom: 'analiza.ipynb'

### Opis datotek
- 'podatki.py' pobere iz spletne strani html, izlušči podatke (uvrstitev, veter, ime tekmovalke, datum rojstva, državljanstvo in datum dogodka na katerem je bil rezultat dosežen), jih pretvori in shrani v json ('podatki.json'), nato pa še v csv ('podatki.csv')
- 'dodatek_kontinenti' glede na državo, ki jo zastopa v 'podatki.csv' doda še podatke o kontinentu na katerem živi posamezna tekmovalka
- 
- 'analiza.ipynb' vsebuje zaključeno analizo z grafi in histogrami


