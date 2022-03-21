""" UKOL-03: SMS BRÁNA
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

  - Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
  - Zeptá se uživatele na zprávu, kterou chce zaslat. Nakonec vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

  - První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolby "+420"). kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
  - Druhá funkce spočte cenu zpráv. Uživatel platí 3 Kč za každých započatých 180 znaků.
Program Tvůj nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživatelé. 

BONUS
Zkus svoji první funkci vytunit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš tak, že použiješ replace()a tečkovou notaci. První parametr je znak, který chceš nahradit, a druhý parametr nový znak. Níže je příklad použití."""


def kontrola_cisla (cislo):
  tel_cislo = cislo.replace(" ","")
  delka_cisla = len(tel_cislo)
  if delka_cisla == 13:
    bez_predcisli = tel_cislo[4:13]
    if tel_cislo[0:4] == "+420" and bez_predcisli.isnumeric()==True:
      return True
    else: return False
  elif delka_cisla == 9:
    if tel_cislo.isnumeric()==True:
      return True
    else: return False
  else: return False


from math import ceil

def cena_zpravy (text):
  delka_zpravy = len(text)
  pocet_sms = ceil(delka_zpravy/180)
  cena = pocet_sms * 3
  print(f"Délka vaší zprávy je přes {pocet_sms} SMS. Cena vaší zprávy je {cena} Kč.")
  return cena


telefonni_cislo = input("Zadejte své telefonní číslo (bez mezer): ")

kontrola_cisla(telefonni_cislo)

if kontrola_cisla(telefonni_cislo)==True:
  sms_zprava = input("Zadejte svou sms: ")
  cena_zpravy(sms_zprava)
else: print("Vaše telefonní číslo není ve správném formátu.")