# -*- coding: utf-8 -*-
print("Ashmit Nene ME11 11B 5")
print("")
print("Random numbers assignment")
print("")
print("Enter a word")
w=input()
print("Enter 5 random numbers one after another, and press enter after each number")
num1=input()
num2=input()
num3=input()
num4=input()
num5=input()
print("")
import random
 
# prints a random value from the list
print("This is a randomly chosen number out of the 5 you entered")
list1 = [num1, num2, num3, num4, num5]
print(random.choice(list1))
print("")
 
# prints a random item from the string
print("This is a random letter from the word you entered")
string = w
print(random.choice(string))