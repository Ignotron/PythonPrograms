# -*- coding: utf-8 -*-
print("A program of Ashmit Nene 11B ME11 5")
print("")
print("Q1")
print("")
print("")
print("Type either an Uppercase or lower case letter or type a digit")
ch=input()
if (ch >= 'A' and ch <= 'Z'):
    print(ch,"is an UpperCase character");
elif (ch >= 'a' and ch <= 'z'):
    print(ch,"is an LowerCase character");
else:
    print(ch,"is a digit");
print("")
print("END OF Q1")
print("")
print("Q2")
print("")
print("")
print("Now we will find roots")
def findRoots(a, b, c):  
  
    dis_form = b * b - 4 * a * c  
    sqrt_val = (abs(dis_form))*(abs(dis_form))
    if dis_form > 0:  
        print(" real and different roots ")  
        print((-b + sqrt_val) / (2 * a))  
        print((-b - sqrt_val) / (2 * a))  
  
    elif dis_form == 0:  
        print(" real and same roots")  
        print(-b / (2 * a))  
  
  
    else:  
        print("Complex Roots")  
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val)  
  
  
a = int(input('Enter a:'))  
b = int(input('Enter b:'))  
c = int(input('Enter c:'))  
  
# If a is 0, then incorrect equation  
if a == 0:  
    print("Input correct quadratic equation")  
  
else:  
    findRoots(a, b, c)  

print("")
print("END OF Q2")
print("")
print("Q3")
print("")

print("Enter a number to see its multiplication table")
n=int(input())
num = n

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

print("")
print("END OF Q3")
print("")
print("Q4")
print("")
print("Enter any 5 numbers, after each number press enter")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(a*a)
print(b*b)
print(c*c)
print(d*d)
print(e*e)
print("These are square roots of the respective numbers")
print("")
print("END OF Q4")
print("")
print("Q5")
print("")
print("Give the first and last numbers of a range of 10 numbers")
print("First number")
number1=input()
print("Last number")
number2=input()
numofnums=10
print(numofnums*1/2(number1+number2))

























