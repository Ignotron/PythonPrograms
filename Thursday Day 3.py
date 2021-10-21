# -*- coding: utf-8 -*-
st=input("Enter a string in which if you want, you may enter numbers: ")
sum=0
length=len(st)
for i in range(length):
    try:
        sum+=int(st[i])
    except:
        pass
print(sum)        

s=input("Enter a string:")
sum=0
lengt=len(s)
for v in range(lengt):
    try:
        sum+=int(s[v])
    except:
        pass
print(sum)

