# Projektna-naloga-UVP: 
## Analiza teka žensk na 60m

Avtorica: Sara Polajnar

Oktober 2024

### Uvod 
Glavna ideja analize in navdih izhajata iz vprašanja: "Ali res ljudje afriškega porekla dosegajo najboljše rezultate predvsem na šprintih in tekih na srednje razdalje?" V nalogi sem za ciljno skupino vzela ženske rojene med letoma 1967 in 2012 iz celega sveta ter naredila analizo teka na 60m v letu 2024. Vsi podatki so bili dne 10.10.2024 zajeti iz [spletne strani](https://worldathletics.org/records/toplists/sprints/60-metres/all/women/senior/2024?regionType=world&timing=electronic&windReading=regular&page=1&bestResultsOnly=true&maxResultsByCountry=all&eventId=10229684&ageCategory=senior). Tekom analize pa so se pojavile še različne druge možnosti za primerjavo podatkov:

#### Kako se rezultati razlikujejo:
- glede na državljanstvo,
- glede na starost,
- glede na čas/mesec dogodka (vpliv zunanjih dejavnikov),
- glede na kontinent

### Navodila za uporabo
Za uspešen vpogled v analizo mora imeti uporabnik nameščene naslednje knjižnice: beautifulsoup, pandas, requests, os, csv, json in matplotlib.pyplot.
Celotna analiza se nahaja v datoteki z imenom: 'analiza.ipynb'.

### Opis datotek
- 'podatki.py' pobere iz spletne strani html, izlušči podatke (uvrstitev, rezultat, ime tekmovalke, datum rojstva, državljanstvo, pozicijo, skupne točke, in datum dogodka, na katerem je bil rezultat dosežen), jih pretvori in shrani v json ('podatki.json'), nato pa še v csv ('podatki.csv')
- 'dodatek_kontinenti' glede na državo, ki jo zastopa posamezna tekmovalka v 'podatki.csv' doda še podatke o kontinentu na katerem živi
- 'analiza.ipynb' vsebuje zaključeno analizo z grafi in histogrami


