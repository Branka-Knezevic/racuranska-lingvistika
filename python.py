# -*- coding: utf-8 -*-
x = "loš"
y = "Miloš"
z = "dobar"

print(x in y) #print("loš" in "Miloš")
print(z in y) #print("dobar" in "Miloš")


lista_brojeva = [1, 2, 2.5]
lista_niski = ["ovo", "je", "lista", "niski", "ova", "lista", "je", "kul"]
lista_svega = [True, "može", "i", "ovo", 5.0, [1, 2, "tri"]]
print(lista_brojeva[2])
print(lista_niski[0])
print(lista_svega[-1])
print(lista_svega[-1][2])

print(lista_brojeva)
lista_brojeva[2] = 3
print(lista_brojeva)



priča= "bla. bla. bla. bla. bla."
rečenice= priča.split(". ")
print(rečenice)
rečenice_prvi_deo=rečenice[0:-1]
print(rečenice_prvi_deo)
q="bla. bla."
x=rečenice_prvi_deo.append(q)
print(rečenice_prvi_deo)

ponovo_niska=". ".join(rečenice_prvi_deo)
print(ponovo_niska)

rečenice_bez_tačke=rečenice_prvi_deo [-1][0:-1] 
print(rečenice_bez_tačke)


lista_svega.insert(2,"brokoli")
print(lista_svega)

print(lista_niski)
skup=set(lista_niski)
print(skup)


tekst="Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: \"Ju, Mitre, uplašio si me!\". Ali Mitar se na to nije obazirao - žustro je skočio u Mileninom pravcu. Videvši to, Milena polete preko dvorišta i polete ka stacionaru brzinom svetlosti. Nažalost, svetlost je brža od automatskog mehanizma za otvaranje vrata. I tako ostade Milenin trag na ulaznim vratima IS Petnica."
tekst=tekst.lower()
lista_reči=tekst.split(" ")
print (lista_reči)
lista_reči[4]=lista_reči[4][:-1]
lista_reči[5]=lista_reči[5][:-1]
lista_reči[13]=lista_reči[13][1:-1]


lista_reči[12]=lista_reči[12][:-1]
lista_reči[14]=lista_reči[14][:-1]
lista_reči[17]=lista_reči[17][:-3]
lista_reči[25]=lista_reči[25][:-1]
lista_reči[31]=lista_reči[31][:-1]
lista_reči[33]=lista_reči[33][:-1]
lista_reči[43]=lista_reči[43][:-1]
lista_reči[44]=lista_reči[44][:-1]
lista_reči[53]=lista_reči[53][:-1]
lista_reči[63]=lista_reči[63][:-1]
print(lista_reči[63])
print(lista_reči[63][0:-1])


telefonski_imenik = {"Paja Patak": 123456, "Mini Maus": 234567, "Šilja": 345678}
vukajlija = {"sojanica": "Posna pljeskavica. Garantovano bez trihinele.", "jahanje": "Omiljena aktivnost šefova za koju je potrebno da radnik ima konjske živce.", "šef": "Čovek koji nema smisao za umor."}
vrste_reči = {"imenice": ["polaznik", "seminar", "lingvistika", "Isidora"], "glagoli": ["slušati", "crtati", "jesti"], "zamenice": ["on", "ona", "ono"]}

print(telefonski_imenik["Mini Maus"])
print(vukajlija["šef"])
print(vrste_reči["imenice"])
print(telefonski_imenik)
vukajlija["šef"]="Miloš"
print(vukajlija)


print(telefonski_imenik.keys())
print(telefonski_imenik.values())

print(vrste_reči["imenice"][2])