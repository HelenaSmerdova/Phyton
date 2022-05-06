# ukol-08: Adopce zvířat

# Stáhni si dataset, který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je Národní katalog otevřených dat.
# Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.

import pandas

zoo = pandas.read_csv("adopce-zvirat.txt", sep=";")

# Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?

zoo.info()

# Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině.

print(zoo.iloc[33,1:3])

# Bonus
# V lekci jsme zmínili, že existují i jiné typy indexů, než jen číselný, který sám vyrobí pandas. Například v kontextu souboru se zvířaty se nabízí hned několik sloupců, které bychom mohli využít jako index, které nejsou číselné.
# Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině. Všimni si, že sloupec teď povýší na index a už se nenachází mezi "běžnými" sloupci.

zoo_2 = pandas.read_csv("adopce-zvirat.txt", sep=";", index_col="nazev_cz")
#print(zoo_2)

# Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.

unikatnost = zoo_2.index.is_unique
print(unikatnost)

# Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index(). Bacha, metoda vrátí novou tabulku se seřazeným indexem. Budeš tedy chtít přepsat původní tabulku.

zoo_2 = zoo_2.sort_index()
#print(zoo_2)

# Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.

print(zoo_2.loc["Outloň váhavý"])

# Rozsahy fungují podobně jako u číselných indexů. Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá".

print(zoo_2.loc["Želva Smithova":"Želva žlutočelá"])
