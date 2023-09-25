import csv

stundenlohn_brutto = 0
stundenlohn_netto = 0
stunden = input("Bitte gib die Anzahl der Stunden ein")
tageslohn = stundenlohn_brutto * stunden

#bruttolohn_monat

bruttolohn_monat = float(input("Bitte gib deine Bruttolohnmonatslohn an"))

#Arbeitslosenbeitrag 
albeitrag = {
    "1.Stufe": 3, # 0-1885,0€
    "2.Stufe": 2, # 1885,01€ - 2056,0€
    "3.Stufe": 1, # 2056,01€ - 2228,0€
    "4.Stufe": 0, # > 2228,0€
}

#lohnsteuer in €

def lohnsteuer(brutto_monat):
    lohnsteuer_max = 0 
    lohnsteuer_klassen = {
        985.42 : 0,
        1605.50 : 20,
        2683.92 : 30,
        5184.33 : 41,
        7771.0 : 48,
        83344.33 : 50
    }
    lohnsteuer_liste = list(lohnsteuer_klassen)
    print(lohnsteuer_liste)

    if brutto_monat <= lohnsteuer_liste[0]:
        lohnsteuer_max = brutto_monat * (lohnsteuer_klassen[985.42]/100)
    elif brutto_monat >= lohnsteuer_liste[0] and brutto_monat <= lohnsteuer_liste[1]:
        lohnsteuer_max = brutto_monat * (lohnsteuer_klassen[1605.50]/100)
    elif brutto_monat >= lohnsteuer_liste[1] and brutto_monat <= lohnsteuer_liste[2]:
        lohnsteuer_max = brutto_monat * (lohnsteuer_klassen[2683.92]/100)
    elif brutto_monat >= lohnsteuer_liste[2] and brutto_monat <= lohnsteuer_liste[3]:
        lohnsteuer_max = brutto_monat * (lohnsteuer_klassen[5184.33]/100)
    elif brutto_monat >= lohnsteuer_liste[3] and brutto_monat <= lohnsteuer_liste[4]:
        lohnsteuer_max = brutto_monat * (lohnsteuer_klassen[7771.0]/100)
    else:
        lohnsteuer_max = brutto_monat * (lohnsteuer_klassen[83344.33]/100)

    return lohnsteuer_max

# print(f"Deine Lohnsteuer ohne Abzüge beträgt: {lohnsteuer(bruttolohn_monat)}€")

#Kind in €
kinder_anzahl = int(input("Wie viele Kinder hast du?"))
def kinderbeitrag(kinder):
    kinderbeitrag = 0
    kindbeitrag_1 = 43.33
    kindbeitrag_2 = 58.67
    kindbeitrag_3 = 19.33

    if kinder == 1:
        kinderbeitrag = kindbeitrag_1
    elif kinder == 2:
        kinderbeitrag = kindbeitrag_2
    else:
        kinderbeitrag = kindbeitrag_2 + kindbeitrag_3 * (kinder-2)

    return round(kinderbeitrag, 2)

#Familienbonus
familienbonus_erhalten = 0

def familienbonus(kinderunter18,kinderueber18):
    faboueber18 = 54.18 #Stand 2022
    fabounter18 = 166.68 #Stand 2022

    familienbonus_gesamt = float(fabounter18 * kinderunter18 + faboueber18 * kinderueber18)


    return familienbonus_gesamt 

if kinder_anzahl >= 1:
    kinderunter18 = int(input(f"Wie viele deiner {kinder_anzahl} Kinder sind unter 18 Jahre alt?: "))
    kinderueber18 = kinder_anzahl - kinderunter18
    familienbonus_erhalten = familienbonus(kinderunter18,kinderueber18)
else: 
    familienbonus_erhalten = 0

# print(f"Dein Familienbonus beträgt {familienbonus_erhalten} €")

# sonstige Bezüge
sBezüge = {
    "620,0": 0,
    "24380.0": 6,
    "25000,0": 27,
    "33333,0": 35.75
}



#Beitragsprozentsätze im Überblick: Gesamt, Dienstgeber, Dienstnehmer
bps_gesamt = 37.55
bps_gesamt_percent = {
    "Arbeiterkammer":  0.50,
    "Wohnbauförderung": 1.0,
    "Insolvenzentgelt": 0.1,
    "Schlechtwetter": 1.4,
    "Nachtschwerarbeit": 3.8,
    "Betriebl. Vorsoge": 1.53
}
bps_dg = 20.43
bps_dg_percent = {
    "Arbeiterkammer":  0,
    "Wohnbauförderung": 0.5,
    "Insolvenzentgelt": 0.1,
    "Schlechtwetter": 0.7,
    "Nachtschwerarbeit": 3.8,
    "Betriebl. Vorsoge": 1.53
}
bps_dn = 17.12
bps_dn_percent = {
    "Arbeiterkammer":  0.5,
    "Wohnbauförderung": 0.5,
    "Insolvenzentgelt": 0,
    "Schlechtwetter": 0.7,
    "Nachtschwerarbeit": 0,
    "Betriebl. Vorsoge": 0
}

#Geringfügigkeitsgrenze in €
gg = 500.91

#Selbstversicherung in €
sv = 70.72

#ecard in €
ecard = 13.25

#Dienstgeberabgabe in % DG-Grenze in €
dg_abgabe = 16.4
dg_grenze = 751.37 

#Höchstbemessungsgrundlage in €
hbgl_tgl = 195
hbgl_monatlich = 5850
hbgl_jaehrlich = 11700

#Pendlerpauschale
entfernung = int(input("Bitte gib die Anzahl der Kilometer ein: "))
#Pendlerpauschale klein für Massenverkehrsmittel(Öffis)
def pp_klein(kilometer):
    pendlerpauschale = 0
    pendlerpauschale_1 = 58.0
    pendlerpauschale_2 = 113.0
    pendlerpauschale_3 = 168.0
    if kilometer >= 20 and kilometer <= 40: 
        pendlerpauschale = pendlerpauschale_1
    elif kilometer > 40 and kilometer <= 60:
        pendlerpauschale = pendlerpauschale_2
    elif kilometer > 60:
        pendlerpauschale = pendlerpauschale_3
    else:
        pendlerpauschale = 0
    
    return pendlerpauschale

#Pendlerpauschale groß für eigenes Auto
def pp_groß(kilometer):
    pendlerpauschale = 0
    pendlerpauschale_1 = 31.0
    pendlerpauschale_2 = 123.0
    pendlerpauschale_3 = 214.0
    pendlerpauschale_4 = 306.0
    if kilometer >= 2 and kilometer <= 20: 
        pendlerpauschale = pendlerpauschale_1
    elif kilometer > 20 and kilometer <= 40:
        pendlerpauschale = pendlerpauschale_2
    elif kilometer > 40 and kilometer <= 60:
        pendlerpauschale = pendlerpauschale_3
    elif kilometer > 60:
        pendlerpauschale = pendlerpauschale_4
    else:
        pendlerpauschale = 0
    
    return pendlerpauschale

arbeitstage = int(input("Bitte gib die Anzahl deiner Arbeitstage im Monat an"))
      
def pp_aliqotierung(tage,pp):
    pp_final = 0
    if tage >= 4 and tage <= 7:
        pp_final = pp*0.33
    elif tage >=8 and tage <= 10:
        pp_final = pp*0.66
    elif tage >= 11:
        pp_final = pp
    else:
        pp_final = 0

    return pp_final



#Pendlereuro
def pendlereuro(kilometer):
    pendlereuro = 0.5 * kilometer
    return pendlereuro

#Verkehrsabsetzbetrag in €
vak = 35.08


file = open("Lohnverrechnung.csv", "a")



