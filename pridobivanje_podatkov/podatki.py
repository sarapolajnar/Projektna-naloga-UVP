import requests 
from bs4 import BeautifulSoup
import json
import os
import pandas as pd

podatki = []

i = 1

while True:
    try:
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
                mark = celica[1].text.strip() 
                competitor_link = celica[3].find('a')    #ime tekmovalke je za linkom med a-ji
                competitor = competitor_link.text.strip() if competitor_link else 'N/A'
                dob = celica[4].text.strip()  
                country = celica[5].text.strip()
                position = celica[6].text.strip()         
                date = celica[9].text.strip()   
                result_score = celica[10].text.strip()
                
                #naredimo slovar
                podatki_tekmovalke = {
                    'uvrstitev': rank,
                    'rezultat [s]': mark,
                    'ime tekmovalke': competitor,
                    'datum rojstva': dob,
                    'država': country,
                    'pozicija' : position,
                    'datum dogodka': date,
                    'skupne točke' : result_score
                }
                podatki.append(podatki_tekmovalke)

        i += 1

    except Exception as e:          #ce se zgodi napaka...npr tudi ko zmanjka strani se zanka ustavi
        print(f"Napaka pri strani {i}: {e}")
        break

ime_mape = "pridobivanje_podatkov"

if not os.path.exists(ime_mape):        #zaradi urejenosti dodamo shranimo v posebno mapo
    os.makedirs(ime_mape)

pot_do_json = os.path.join(ime_mape, 'podatki.json')

with open(pot_do_json, 'w', encoding='utf-8') as json_file:
    json.dump(podatki, json_file, ensure_ascii=False, indent=4)

with open(pot_do_json, 'r', encoding='utf-8') as json_file:     #odpremo le za branje
    podatki_json = json.load(json_file)

data_frame = pd.DataFrame(podatki_json)     #shranis v pandas obliki
pot_do_csv = os.path.join(ime_mape, 'podatki.csv')      #kam naj shrani
data_frame.to_csv(pot_do_csv, index=False, encoding='utf-8')        #pretvori v csv

print("Prenos uspešen")





