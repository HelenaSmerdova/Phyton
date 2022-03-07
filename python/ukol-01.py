# ukol-01: Balíky

from pickle import TRUE


baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod = input("Zadej kód balíku: ")

if kod in baliky:
  if baliky[kod] == True:
    print (f"Balík {kod} byl již předán dopravci.")
  else: print (f"Balík {kod} ještě nebyl předán dopravci.")
else: print ("Tento balík není v seznamu.")