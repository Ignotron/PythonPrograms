# -*- coding: utf-8 -*-
a=int(input("Enter age:"))
b=str(input("Enter gender as uppercase M/F:"))
c=int(input("Enter number of days worked:"))
if a>=18 or a<=30:
    if b=="M":
     print("Wage is",700*c)
    elif b=="F":
        print("Wage is",750*c)
elif a>=30 or a<=40:
    if b=="M":
        print("Wage is",800*c)
    elif b=="F":
        print("Wage is",850*c)
