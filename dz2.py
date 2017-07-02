# -*- coding: utf-8 -*-
rečnik={"smejati se":{"sinonimi":["kikotati se","smeškati se"],"antonimi":["plakati","mrštiti se"]},"dobar":{"sinonimi":["nepokvaren","milosrdan"],"antonimi":["loš","zao"]},"veliki":{"sinonimi":["ogroman","glomazan"],"antonimi":["mali","sićušan"]}}

print(rečnik["smejati se"]["sinonimi"])
print(rečnik["dobar"]["antonimi"])
print(rečnik["veliki"]["antonimi"][1])
print(rečnik["dobar"]["sinonimi"][0])

for reč in rečnik.keys():

    

    print("reč: ", reč) 

    sin = "Sinonimi: "

    ant = "Antonimi: "



    for sinonim in rečnik[reč]["sinonimi"]:

        sin += sinonim + ", "

    print(sin[:-2])



    for antonim in rečnik[reč]["antonimi"]:

        ant += antonim + ", "    

    print(ant[:-2] + "\n")