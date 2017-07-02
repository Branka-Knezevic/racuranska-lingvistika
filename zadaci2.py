# -*- coding: utf-8 -*-
reči = ["novinar", "trener", "muzičar", "pekar", "lekar", "apotekar"]
sufiks = "ka"

for i in range(len(reči)):
	reči[i] = reči[i] + sufiks
    
print(reči)
   
for i in range(len(reči)):
    reči[i] = reči[i][:-2]
print(reči)

lavica = 0
tigrica = 0
sve_reči=set()
korpus = "Juče sam bio u zoo vrtu. Video sam tri lava i bila je tu jedna lavica. Lavica nije imala grivu, jer to imaju samo muški lavovi. Bila je u zoo vrtu i jedna tigrica. Ona je imala jako lepo krzno. Bilo mi je žao što tigrica i lavica ne mogu da se druže, jer mislim da bi se baš lepo slagale pošto su obe mačke."

tokeniziraniKorpus = korpus.split(" ")

for reč in tokeniziraniKorpus:
    # prebacivanje reči u mala slova
    reč = reč.lower()
    # uklanjanje interpunkcijskih znakova
    reč = reč.strip(",.")
    
    sve_reči.add(reč)
    
    if reč == "lavica":
        lavica += 1 # lavica = lavica + 1
    elif reč == "tigrica":
        tigrica += 1 # tigrica = tigrica + 1

print("Broj javljanja reči lavica:", lavica)
print("Broj javljanja reči tigrica:", tigrica)

print(len(sve_reči))




brojPriloga = 0
prilozi = ["ovde", "tamo", "tu", "desno", "negde"]
korpus = "Ovde mi je baš lepo. Džunglu ne volim. Ne bih volela da sam tamo. Moje mesto je tu. Tu se osećam kao da sam kod kuće. Stavila sam svoju šoljicu kafe desno, e baš tu."

tokeniziraniKorpus = korpus.split(" ")

for reč in tokeniziraniKorpus:
    # prebacivanje reči u mala slova
    reč = reč.lower()
    # uklanjanje interpunkcijskih znaka
    reč = reč.strip(",.")
    len(broj_priloga)


print(n_prilozi)
print(set(n_prilozi))






korpus = "Ovaj korpus sam sastavljala dok je Isidora sedela u kancelariji i puštala pesme benda The National. Pitala me je da li mi se bend sviđa i rekla je da ona misli da je to super muzika za preko dana. Pošto bukvalno više nemam ideja šta da kucam ovde, nastaviću da ispisujem šta se sve nalazi oko mene. Levo od mene su dva tanjira koje je Milena oprala. Deluju čisto. S leve strane računara nalazi se tirkizni lak čije je ime u stvari Green. Nije mi baš najjasnije ko tu ne vidi boje. S desne strane računara nalazi se providni lak, ali je bočica obojena u crno, pa je Tijana zbog toga prošlog seminara mislila da je crn. Nejasni su mi proizvođači lakova. "

korpus = korpus.lower()
digrami = list()

for i in range(len(korpus)):
   digram = korpus[i:i+2]
   digrami.append(digram)

print(digrami)

print(set(digrami))
ttr=len(set(digrami))/len(digrami)
print(ttr)
