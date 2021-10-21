# -*- coding: utf-8 -*-

print("Welcome")
print("")
print("END OF Q1")
print("")
print("This program is made by Ashmit Nene, roll,no 5, Ref,no: ME11,from 11B")
print("")
print("Enter any 2 digit number")
num1=input()
print("Now enter another 2 digit different number")
num2=input()
if(num1 >= num2):
   print(num1, "is greater than")
else:
    print(num2, "is greater than")
print("")
print("END OF Q2")
print("")
print("Enter a 2 digit number")
a=input()
print("Now enter another 2 digit number")
b=input()
print("Excellent! Now enter another 2 digit number")
c=input()
print("")
if(a>=b and a>=c):
    print(a, "is the largest number")
if(b>=a and b>=c):
    print(b, "is the largest number")
if(c>=a and c>=b):
    print(c, "is the largest number")
print("")
print("END OF Q3")
print("")
num1=int(input("Enter your number:"))
if(num1%3==0 and num1%5==0):
    print("{} is divisible by both 3 and 5".format(num1))
elif(num1%3==0):
    print("{} is divisible by 3 ".format(num1))
elif(num1%5==0):
    print("{} is divisible by 5 ".format(num1))
else:
    print("{} is not divisible by 3 or 5".format(num1))
print("")
print("END OF Q4")
print("")
print("Now I have generated a random sentence, type a word and I will check if it is in the present sentence")
W=input()
def isWordPresent(sentence, word):
    s = sentence.split(" ")
 
    for i in s:
        if (i == word):
            return True
    return False
s = "On offering to help the blind man, the man who then stole his car, had not, at that precise moment, had any evil intention, quite the contrary, what he did was nothing more than obey those feelings of generosity and altruism which, as everyone knows, are the two best traits of human nature and to be found in much more hardened criminals than this one, a simple car-thief without any hope of advancing in his profession, exploited by the real owners of this enterprise, for it is they who take advantage of the needs of the poor."
w = W 
if (isWordPresent(s, w)):
    print("Yes it is present in the sentence")
else:
    print("Not present in the sentence")
print("")
print("END OF Q5")
