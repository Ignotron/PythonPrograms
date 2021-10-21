# -*- coding: utf-8 -*-
print("CALCULATOR")
print("")
print("Please enter a number")
num1=int(input())
print("Now enter another number")
num2=int(input())
print("")
print("Do you want to add, subtract, multiply, divide, remainder or exponent?")
print("Answer as any one of the following: Add, Subtract, Multiply, Divide, Remainder, Exponent")
Answer=input()
if(Answer=='Add'):
    print("Adding...")
    print(num1+num2)
elif(Answer=='Subtract'):
    print("Subtracting...")
    print(num1-num2)
elif(Answer=='Multiply'):
    print("Multiplying...")
    print(num1*num2)
elif(Answer=='Divide'):
    print("Dividing")
    print(num1/num2)
elif(Answer=='Remainder'):
    print("Finding remainder...")
    print(num1%num2)
else:
    print("Finding exponent")
    print(num1**num2)
print("This is maths, get good at it")
print("")
print("New Question")
print("")
print("Enter a number")
num=int(input())
print("Ok bye, I stole your number")
