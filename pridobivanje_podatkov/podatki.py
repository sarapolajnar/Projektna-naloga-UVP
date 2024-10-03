import requests
from bs4 import BeautifulSoup
import json
import os

podatki = []

for i in range(1, 93): 
    url = (f"https://worldathletics.org/records/toplists/sprints/60-metres/all/women/senior/2024?"
            f"regionType=world&timing=electronic&windReading=regular&page={i}&bestResultsOnly=true&"
            f"maxResultsByCountry=all&eventId=10229684&ageCategory=senior")

    odziv = requests.get(url)

    if odziv.status_code != 200:
        print("Prišlo je do napake")
        continue 

    soup = BeautifulSoup(odziv.text, 'html.parser')

    tabela = soup.find('table')

    # Preberi vrstice iz tabele
    for vrstica in tabela.find_all('tr')[1:]:  # preskočimo prvo vrstico (glave), poiscemo tr
        celica = vrstica.find_all('td')         #vsi podatki se nahajajo med td

        if celica:
            rank = celica[0].text.strip()   
            wind = celica[2].text.strip()  
            competitor_link = celica[3].find('a')  
            competitor = competitor_link.text.strip() if competitor_link else 'N/A' #ime tekmovalke je za linkom med a-ji
            dob = celica[4].text.strip()  
            country = celica[5].text.strip()
            position = celica[6].text.strip()         
            date = celica[9].text.strip()   
            
            #naredimo slovar
            podatki_tekmovalke = {
                'uvrstitev': rank,
                'veter': wind,
                'ime tekmovalke': competitor,
                'datum rojstva': dob,
                'država': country,
                'pozicija' : position,
                'datum dogodka': date,
            }
            podatki.append(podatki_tekmovalke)

ime_mape = "pridobivanje_podatkov"

if not os.path.exists(ime_mape):        #zaradi urejenosti dodamo shranimo v posebno mapo
    os.makedirs(ime_mape)

pot_do_datoteke = os.path.join(ime_mape, 'podatki.json')

with open(pot_do_datoteke, 'w', encoding='utf-8') as json_file:
    json.dump(podatki, json_file, ensure_ascii=False, indent=4)

print("Prenos uspešen")





