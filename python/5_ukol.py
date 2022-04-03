#ukol-05: Streamovací služba
""" Uvažuj, že pokračuješ software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku au počtu epizod a délku seriálu jedné epizody.

Vytvořit program, který bude obsahovat tři třídy - Polozka, Filma Serial.
Třída Polozkabude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr. Oba atributy nastav ve funkci __init__, žánr získej jako parametr funkce.
Třída Filmbude potomkem třídy Polozka. Film má kromě názvu a atributu žánru délka.
Třída Serialbude potomkem třídy Polozka. Má kromě názvu a atributů žánru počet epizod a délka epizod.
Všem třídám přidej funkci get_info, která vypíše informace o položce, resp. o filmu a seriálu. Funkce u třídy Polozkavypíše název a žánr. Následně tuto funkci využijete ve funkcích u tříd Filma přidejte Serialk této informaci o délce, resp. počet epizod.
Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověř, že vše funguje. """


class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def get_info (self):
    return f"{self.nazev}, {self.zanr}"

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def get_info(self):
    return f"{super().get_info()}, délka filmu je {self.delka} min."
  def celkova_delka(self):
    return self.delka

class Serial(Polozka):
  def __init__(self, nazev, zanr, epizody, delka_epizod):
    super().__init__(nazev, zanr)
    self.epizody = epizody
    self.delka_epizod = delka_epizod
  def get_info(self):
    return f"{super().get_info()}, {self.epizody} epizod o délkách {self.delka_epizod} min."
  def celkova_delka(self):
    celkova_del = int(self.delka_epizod) * int(self.epizody)
    return celkova_del


class Uzivatel:
  def __init__(self, uzivatelske_jmeno, delka_sledovani = 0):
    self.uzivatelske_jmeno = uzivatelske_jmeno
    self.delka_sledovani = delka_sledovani
  def pripocti_zhlednuti(self,x):
    self.x = x
    self.delka_sledovani += int(x)
    if self.delka_sledovani < 60:
      y = print(f"Uživatel {self.uzivatelske_jmeno} má nasledováno {self.delka_sledovani} min.")
      return y
    else: 
      hodin = self.delka_sledovani//60
      minut = self.delka_sledovani % 60
      y = print(f"Uživatel {self.uzivatelske_jmeno} má nasledováno {hodin} hod {minut} min.")
      return y



trhak = Film("Trhák", "komedie", 94)
rozpusteny = Film("Rozpuštěný a vypuštěný", "komedie", 80)
humoresky= Serial("Cetnicke humoresky", "krimikomedie", 39, 70)
krtek = Serial("Krtkova dobrodružství", "pohádka", 49, 5)

karel = Uzivatel("Karel K.")
 
print(trhak.get_info())
print(rozpusteny.get_info())
print(humoresky.get_info())
print(krtek.get_info())


delka_trhak = trhak.celkova_delka()
delka_rozpusteny = rozpusteny.celkova_delka()
delka_humoresky = humoresky.celkova_delka()
delka_krtek = krtek.celkova_delka()


karel.pripocti_zhlednuti(delka_trhak)
karel.pripocti_zhlednuti(delka_humoresky)
karel.pripocti_zhlednuti(delka_krtek)
karel.pripocti_zhlednuti(delka_rozpusteny)
