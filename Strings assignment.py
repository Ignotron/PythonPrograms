# -*- coding: utf-8 -*-
print("Created by Ashmit Nene 11B ME11 5")
print("")
print("Q1")
str=input("Please enter a string as you wish: ");
vowels=0
consonants=0
for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;#vowel counter is incremented by 1
    else:
        consonants=consonants+1;
#consonant counter is incremented by 1
print("The number of vowels:",vowels);
print("\nThe number of consonant:",consonants);
print("")
print("End of Q1")
print("Q2")
print("")
print("Enter a word")
St=input()
my_str = St

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
print("")
print("End of Q2")
print("")
print("Q4")
word_count = 0
char_count = 0

#2
usr_input = input("Enter a sentence : ")

#3
split_string = usr_input.split()

#4
word_count = len(split_string)

#5
for word in split_string:
    #6
    char_count += len(word)

#7
print("Total words : {}".format(word_count))
print("Total characters : {}".format(char_count))
print("")
print("End of Q4")

