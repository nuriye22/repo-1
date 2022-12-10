# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:10:47 2022

@author: NURİYE KARADAŞ
"""

num=int(input("bir sayı giriniz: "))
if num>1:
    for a in range(2,num):
        if (num%a)==0:
           print(num," asal değidir.")
           break
    else:
        print(num, " asal sayıdır.")
  
else:
    print(num, " asal sayı değildir.")
        
           

           
       
       
        
    
    