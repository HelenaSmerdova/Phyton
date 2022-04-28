""" ukol-08: Prodej vstupenek
Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.
Datum	 -> Cena
1. 7. 2021 - 10. 8. 2021	> 250 Kč
11. 8. 2021 - 31. 8. 2021	 > 180 Kč
Mimo tato data je středisko zavřené.
Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().
Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování. """

from datetime import datetime

print("Vítejte v LETNÍM KINĚ!")
print("Hrajeme celé léto, od 1. 7. do 31. 8. 2021")
termin = input("Na kdy chcete lístky? ")

#definice intervalů
zacatek_prvni_obdobi = datetime (2021,7,1)
konec_prvni_obdobi = datetime (2021,8,10)
zacatek_druhe_obdobi = datetime(2021,8,11)
konec_druhe_obdobi = datetime(2021,8,31)

#úprava formátu vstupního data
termin = termin.replace(" ","")
termin = termin.replace(",",".")
termin = termin.replace("/",".")
termin = termin.replace("-",".")
termin_datum = datetime.strptime(termin, "%d.%m.%Y")

if termin_datum < zacatek_prvni_obdobi or termin_datum > konec_druhe_obdobi:
  print("V tomto termínu je kino uzavřeno.")
else:
  if termin_datum < zacatek_druhe_obdobi:
    # "Prvni obdobi"
    cena_vstupenky = 250
  else: 
    termin_datum <= konec_druhe_obdobi
    # "Druhe obdobi"
    cena_vstupenky = 180
  vstupenky = input("Kolik si přejete vstupenek? ")
  celkova_cena = int(vstupenky) * cena_vstupenky
  termin_datum=termin_datum.strftime("%d. %m. %Y")
  print(f"Na termín {termin_datum} vás bude vstupné stát celkem {celkova_cena} Kč.")
