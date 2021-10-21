# -*- coding: utf-8 -*-
print("Revision for CS Practical")
print("")
amt = int(input("Enter Sale Amount: "))
if(amt>0):
    if amt<=5000:
       disc = amt*0.05
    elif amt<=15000:
        disc=amt*0.12
    elif amt<=25000:
        disc=0.2 * amt
    else:
         disc=0.3 * amt

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
else:
    print("Invalid Amount")

print("")
print("Q2")
print("")
price = float(input("Enter the product price: "))

# declare begin and end variables as empty strings to start
begin = ""
end = ""
# the while loops are to make sure the user inputs a tax rate that 
# is more than 0 and less than 10
while (begin < 0 or begin > 10):
    begin = int(input("Enter tax rate: "))

while (end < 0 or end > 10):
    end = int(input("Enter end tax rate: "))    

# does the math for every integer between beginning and end, prints a 'table'   
for x in range(begin,end+1):
    total = price + price * x/100
    print ("Price: "+str(price)+"\tTax: "+str(x)+"\tTotal: "+str(total))
    x += 1



