#ÚKOL Č. 10 TEPLOTA VE MĚSTECH

import pandas

data = pandas.read_csv("temperature.txt")

#Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
#print(data.head)

#Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.¨
praha = data[data["City"] == "Prague"]
print(praha) 
## průměrné teploty jsou ve Farenheitově stupnici.
## stupně Farenheita 0°C = 32°F, 1°C = 5/9°F

#Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
osmdesat_plus = data["AvgTemperature"]>80
print(data[osmdesat_plus])
##vysledkem je 722řádků s odpovídající prům.teplotou

#Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
evropa = data["Region"]=="Europe"
#evropa2 = data["Region"].isin(["Europe"])
sedesat = data["AvgTemperature"]>60
print(data[evropa & sedesat])

#Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
minus_dvacet = data["AvgTemperature"]<(-20)
chybka_99 = data["AvgTemperature"]<=(-99.0)
##s hodnotou -99.0 je 49 řádků, což se jeví jako chyba, zvláště když jde často o Afriku - předpokládám, že namísto prázdné hodnoty tam bylo vyplněno -99.0¨

print(data[osmdesat_plus | minus_dvacet])
print(data[osmdesat_plus | minus_dvacet & ~chybka_99])

###BONUS
#přidání sloupce a převedení na °C
import pytemperature
data["AvgTemperatureCelsia"] = pytemperature.f2c(data["AvgTemperature"])

#Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
plus_tricet = data[data["AvgTemperatureCelsia"]>30]
print(plus_tricet)

#Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
plus_patnact = data["AvgTemperatureCelsia"]>15
evropa = data["Region"]=="Europe"
print(data[plus_patnact & evropa])

#Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?
minus_10 =data["AvgTemperatureCelsia"]<-10
plus_30 = data["AvgTemperatureCelsia"]>30
#extrémy:
print(data[minus_10 | plus_30])
#podezřelé hodnoty viz "chybka_99"

###BONUS2
#Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
trinacteho = data["Day"]==13
print(data[trinacteho])

#Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
usa = data["Country"]=="US"
usa_13 = data[usa & trinacteho]
print(usa_13)

#Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
washing_philad = (usa_13["City"]== "Washington") | (usa_13["City"]=="Philadelphia")
print(usa_13[washing_philad])