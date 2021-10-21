Finish=False
print("Enter a value")
x=int(input())
print("Enter another value")
n=int(input())
sum = 0
sign=+1
for a in range(n+1):
    term=(x**a)*sign
    sum+=term
    sign*=-1
print("Sum is",sum)
print("Q2")
x=int(input("Enter a value:"))
y=int(input("Enter another value:"))
sum=x
sign=+1
for a in range(2,n+1):
    f=1
    for i in range(1,a+1):
        f*=i
    term=((x**a)*sign)/f
    sum+=term
    sign*=-1
print("Sum is", sum)
print("Part 3")
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
sum=a
for d in range(2,b+1):
    f=1
    for i in range(1,d+1):
        f*=1
    term=((x**d))/f
    sum+=term
print("Sum is:", sum)
print("Part 4")
for c in range(4):
    for p in range(4,c,1):
      print('&')
      p+=1
