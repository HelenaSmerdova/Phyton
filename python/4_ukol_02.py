# 4. úkol - Evidence aut

class Auto:
  def __init__(self, spz, znacka, typ, pocet_najetych_km):
    self.spz = spz
    self.znacka = znacka
    self.typ = typ
    self.pocet_najetych_km = int(pocet_najetych_km)
    self.pujceno = True            #tj.auto je volné

  def __srt__(self):
    print(f"Nabízíme k zapůjčení auto {self.znacka}.")

  def pujc_auto(self):
    if self.pujceno == True:
      print(f"Auto {self.znacka} je volné. Potvrzuji zapůjčení vozidla.")
      self.pujceno = False
    else: print (f"Auto {self.znacka} není k dispozici.")

  def get_info (self):
    print(f"{self.znacka} typu {self.typ} s SPZ {self.spz}, má najeto {self.pocet_najetych_km} km.")

  def vrat_auto (self, ujete_km, pocet_dnu):
    self.pocet_najetych_km += int(ujete_km)
    self.pujceno = True
    if int(pocet_dnu) <= 7:
      cena_za_pujceni = 400
    else:
      cena_za_pujceni = 300
    celkova_cena_za_pujceni = cena_za_pujceni * int(pocet_dnu)
    vystup = print(f"Vaše cena za půjčení auta je {celkova_cena_za_pujceni} Kč.")
    return vystup

#zadání objektů
skoda = Auto("1P3 4747", "Škoda", "Octavia", 41253)
peugeot = Auto("4A2 3020", "Peugeot", "403 Cabrio", 47534)

#půjčení
print ("Vítejte v naší autopůjčovně!")
co_chcete = input("Jaké auto si přejete? (Peugeot/Škoda) ")
if co_chcete == "Peugeot" or co_chcete == "peugeot":
  peugeot.get_info()
  peugeot.pujc_auto()

elif co_chcete == "Škoda" or co_chcete == "škoda" or co_chcete == "Skoda" or co_chcete == "skoda":
  skoda.get_info()
  skoda.pujc_auto()
else: print(f"Zkontrolujte název značky. Značka {co_chcete} není v naší nabídce.")

# kontrola dostupnosti auta

co_chcete = input("Jaké auto si přejete? (Peugeot/Škoda) ")
if co_chcete == "Peugeot" or co_chcete == "peugeot":
  peugeot.pujc_auto()
  peugeot.get_info()
elif co_chcete == "Škoda" or co_chcete == "škoda" or co_chcete == "Skoda" or co_chcete == "skoda":
  skoda.pujc_auto()
  skoda.get_info()
else: print(f"Zkontrolujte název značky. Značka {co_chcete} není v naší nabídce.")

#vrácení auta

auto = input("Nyní vracíte auto. Kterou značku jste meli půjčenou? ")

if auto == "peugeot" or auto == "Peugeot":
  km = input("Zadejte počet vámi ujetých km: ")
  dny = input("Kolik dní jste měli půjčené auto? ")
  peugeot.vrat_auto(km, dny)
elif auto == "skoda" or auto == "škoda" or auto == "Skoda" or auto == "Škoda":
  km = input("Zadejte počet vámi ujetých km: ")
  dny = input("Kolik dní jste měli půjčené auto? ")
  skoda.vrat_auto(km, dny)
else:
  print("Špatný název.")
