# -*- coding: utf-8 -*-
x=int(input("ENter no.of years worked:"))
y=int(input("Enter salary:"))
if x >10:
    print("Bonus:",y*(10/100))
elif x>=6 or x<=10:
    print("Bonus:",y*(8/100))
else:
    print("Bonus:",y*(5/100))


print("")
a=int(input("Enter percentage of marks:"))
if a<40:
    print("Fail")
elif a>=40 or a<=55:
    print("Fair")
elif a>=55 or a<=65:
    print("Good")
else:
    print("Excellent")




