# -*- coding: utf-8 -*-
print("Project by Ashmit Nene from 11B Ref.No:ME11 and Roll.No:5")
print("")
print("This is the sypnosis project and this will be a calculator.")
print("")
print("A calculator was chosen because I wanted to explore advanced python code and to help people in calculations")
print("")
print("             Calculator             ")
print("")
print("If you want to solve using 2 numbers, enter 'TWO', if you want to use three numbers, enter 'THREE'.")
option1=str(input())
if(option1 == "TWO" or option1 == "2"):
    num1=int(input("Enter your first integer:"))
    num2=int(input("Enter your second integer:"))
    calc=str(input("Enter + or - or / or *:"))
    if(calc=="+"):
        print("The result is->",num1+num2)
    elif(calc=="-"):
        print("The result is->",num1-num2)
    elif(calc=="*"):
        print("The result is->",num1*num2)
    elif(calc=="/"):
        print("The result is->",num1/num2)
    else:
        print("Error..........")
        print("")
        print("Restart the program please")
elif(option1 == "THREE" or option1 == "3"):
    n1=int(input("Enter your first number:"))
    n2=int(input("Enter your second number:"))
    n3=int(input("Enter your third number:"))
    cal=str(input("Enter + or - or * or / for the first two numbers:"))
    if(cal=="+"):
        cal2=str(input("Enter + or - or * or / for the last two numbers"))
        if(cal2=="+"):
            print("The result is->",n1+n2+n3)
        elif(cal2=="-"):
            print("The result is->",n1+n2-n3)
        elif(cal2=="*"):
            print("The result is->",n1+n2*n3)
        elif(cal2=="/"):
            print("The result is->",n1+n2/n3)
        else:
            print("Error......")
            print("Restart the program please.")
    if(cal=="-"):
        cal3=str(input("Enter + or - or * or / for the last two numbers"))
        if(cal3=="+"):
            print("The result is->",n1+n2+n3)
        elif(cal3=="-"):
            print("The result is->",n1+n2-n3)
        elif(cal3=="*"):
            print("The result is->",n1+n2*n3)
        elif(cal3=="/"):
            print("The result is->",n1+n2/n3)
        else:
            print("Error......")
            print("Restart the program please.")
    if(cal=="*"):
        cal4=str(input("Enter + or - or * or / for the last two numbers"))
        if(cal4=="+"):
            print("The result is->",n1+n2+n3)
        elif(cal4=="-"):
            print("The result is->",n1+n2-n3)
        elif(cal4=="*"):
            print("The result is->",n1+n2*n3)
        elif(cal4=="/"):
            print("The result is->",n1+n2/n3)
        else:
            print("Error......")
            print("Restart the program please.")
    if(cal=="/"):
        cal5=str(input("Enter + or - or * or / for the last two numbers"))
        if(cal5=="+"):
            print("The result is->",n1+n2+n3)
        elif(cal5=="-"):
            print("The result is->",n1+n2-n3)
        elif(cal5=="*"):
            print("The result is->",n1+n2*n3)
        elif(cal5=="/"):
            print("The result is->",n1+n2/n3)
        else:
            print("Error......")
            print("Restart the program please.")
    else:
        print("ERROR...........")
        print("")
        print("Restart the program please")
else:
    print("Error........")
    print("")
    print("Restart the program and try again.")
    
print("For review or remarks please send a mail on 'me11@myshala.com'")
print("")
print("To end the program please enter 'END'")
end=str(input())
if(end=="END"):
    print("Thank You, Bye")
    bye=str(input("Type 'BYE'"))
else:
    print("Retry please")
    