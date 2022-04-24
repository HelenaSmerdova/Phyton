#ukol-07: Pošta
# Česká pošta má stránku na webu, která radí, jak správně nadepsat zásilku. Uvádí i několik vzorů pro české i zahraniční zásilky.
# V souboru posta.html nalezneš zdrojový kód této stránky v HTML (to je značkovací jazyk, ve kterém jsou napsané některé webové stránky, nebo části některých webových stránek.).
# 1. Soubor si načti do proměnné tak, aby se celý jeho obsah nacházel jako jeden řetězec v proměnné. Můžeš využít metodu read() (doplň název souboru a název své proměnné):

with open("posta.html", encoding='utf-8') as vstup:
    vstup_posta = vstup.read()
#print(vstup_posta)

# 2. Nahraď znaky odřádkování (zapisuje se jako '\n') jednoduchou mezerou pomocí metody replace().¨

bez_odradkovani = vstup_posta.replace("\n"," ")
#print(bez_odradkovani)

# 3. Nahraď po sobě jdoucích víc mezer jedinou mezerou: Sestav regulární výraz, který označuje jednu nebo více mezer. Pak pomocí re.sub() nahraď takové sekvence jedinou mezerou. První parametr metody re.sub() je regulární výraz, který nahrazujeme, druhý parametr je řetězec, který nahrazujeme, a třetí parametr je řetězec, ve kterém nahrazujeme.

import re
reg_vice_mezer = re.compile("  *")        #funguje i s reg.výrazem ("\s\s*")
bez_mezer = re.sub(reg_vice_mezer, " ", bez_odradkovani)
#print(bez_mezer)

# 4. Najdi v datech všechna česká a slovenská města a jejich PSČ, která se nacházejí v ukázkových adresách. Mají format PSČ MĚSTO, kde PSČ se skládá ze tří číslic, mezery a dvou číslic, a MĚSTO se skládá z jednoho nebo více slov oddělených mezerou, za kterými může ještě následovat číslo pošty.

reg_psc_mesto = re.compile("\d{3} \d{2} \w+ ?[\w* ]*") 
adresy = reg_psc_mesto.findall(bez_mezer)
print(adresy)