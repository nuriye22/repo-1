# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:46:00 2022

@author: NURİYE KARADAŞ
"""



dosya=open("Data","w+")
dosya.write("Name: Nuriye\n")
dosya.write("Surname: Karadas\n")
dosya.write("Gender: Kadin\n")
dosya.write("Username: Nur\n")
dosya.write("Job: Engineer")
dosya=open("Data","r")
str=dosya.read()
str=str.split("\n")
dict={}
for i in str:
    kelime=i.split(":")
    dict[kelime[0]]=kelime[1]   
print(dict)
print(type(dict))
dosya.close()