#ukol-06: Půjčovna aut
""" Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najela dohromady kilometrů. V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrech. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.
>>Napište program, který na výstup vypíše součet všech ujetých kilometrů. """
""" BONUS:
Upravte váš program tak, aby jméno souboru k otevření zadal uživatel, abychom mohli takto zpracovat výkazy z různých, aniž bychom museli upravovat samotný kód programu. Program ověřte tak, že si auta.txtpřejmenujete, nebo si soubor nový. """


print("Vítejte v naší půjčovně aut")
zdrojovy_soubor = input("zadejte název zdrojového souboru: ")


##načtení souboru
#from encodings import utf_8
with open(zdrojovy_soubor) as vstup: 
  auta = vstup.readlines()
# print(auta)


##do seznamu
seznam_aut = [auto.strip() for auto in auta]
# print(seznam_aut)


##odstranění prázdných řádků (\n, resp."")
if "" in seznam_aut:
  seznam_aut.remove("")


##čárky na tečky
seznam_aut = [auto.replace(",",".") for auto in seznam_aut]
# print(seznam_aut)


##očištění
seznam_aut = [auto.split() for auto in seznam_aut]
# print(seznam_aut)


##pokračovat - převést druhou část na float
seznam_aut = [[auto[0], float(auto[1])] for auto in seznam_aut]
# print(seznam_aut)


##součet všech najetých km
jednotlive_km = [auto[1] for auto in seznam_aut]
#print(jednotlive_km)
km_celkem = sum(jednotlive_km)
print(f"Auta najela celkem {km_celkem} tis. km.")
