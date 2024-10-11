import pandas as pd

def vse_drzave(pot_do_datoteke):
    data_frame = pd.read_csv(pot_do_datoteke)       #uvoz datotek iz csv-ja
    posamezne_drzave = data_frame['država'].unique()       #branje posameznih drzav
    
    print(sorted(posamezne_drzave))

#vse_drzave('pridobivanje_podatkov/podatki.csv')    #v terminalu dobimo vse drzave za lazjo obdelavo

#razporeditev drzav po kontinentih
kontinentalna_razvrstitev = {
    'Azija': ['AZE', 'BAN', 'CHN', 'GEO', 'HKG', 'IND', 'IRI', 'IRQ', 'JPN', 'KAZ', 'KOR', 'KSA', 'KUW',
              'LBN', 'MAC', 'MNT', 'MON', 'PHI', 'SRI', 'THA', 'TKM', 'UAE'],
    'Evropa': ['ALB', 'AND', 'AUT', 'BEL', 'BIH', 'BLR', 'BUL', 'CRO', 'CYP', 'CZE', 'DEN', 'ESA', 'ESP',
               'EST', 'FIN', 'FRA', 'GBR', 'GER', 'GRE', 'HUN', 'IRL', 'ISL', 'ISR', 'ITA', 'KOS', 'LAT',
               'LIE', 'LTU', 'LUX', 'MDA', 'MKD', 'MLT', 'NED', 'NOR', 'POL', 'POR', 'ROU', 'RUS', 'SLO',
               'SMR', 'SRB', 'SUI', 'SVK', 'SWE', 'TUR', 'UKR'],
    'Afrika': ['ALG', 'ANG', 'BUR', 'CAF', 'CGO', 'CIV', 'CMR', 'CPV', 'GAB', 'GAM', 'GBS', 'GHA', 'KEN',
               'MAR', 'MRI', 'NAM', 'NGR', 'RSA', 'SEN', 'SEY', 'SLE', 'STP', 'TOG', 'UGA'],
    'Severna in Srednja Amerika': ['AIA', 'ANT', 'BAH', 'BAR', 'BER', 'CAN', 'CAY', 'CRC', 'DOM', 'GRN',
                                   'GUA', 'HAI', 'IVB', 'JAM', 'LCA', 'MEX', 'PUR', 'SKN', 'TTO', 'USA', 'VIN'],
    'Oceanija': ['AUS', 'FIJ', 'NZL', 'PNG', 'SOL'],
    'Južna Amerika': ['ARG', 'BOL', 'BRA', 'CHI', 'COL', 'ECU', 'GUY', 'PAR', 'PER', 'URU', 'VEN']
}

#vsaki posamezni drzavi priredi pripadajoč kontinent
def doloci_kontinent(drzava, kontinentalna_razvrstitev):
    for kontinent, drzave in kontinentalna_razvrstitev.items():
        if drzava in drzave:
            return kontinent
        
data_frame = pd.read_csv('pridobivanje_podatkov/podatki.csv')

data_frame['kontinent'] = data_frame['država'].apply(lambda x: doloci_kontinent(x, kontinentalna_razvrstitev))
#dodamo nov stolpec imenovan kontinent z ujemajocimi imeni kontinentov

data_frame.to_csv('pridobivanje_podatkov/podatki.csv', index=False, encoding='utf-8')       #shranimo v obstojeci csv
