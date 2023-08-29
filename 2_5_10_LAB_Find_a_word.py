"""
Your task is to write a program which answers the following question: 
are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no 
(as the letters "d", "o", or "g" don't appear in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
"""
in_word = input("Enter the word to be searched \n")
in_phrase = input("Enter the character stream to check")
def check_for_hidden (word, phrase):
    counter = 0
    subStrCounter = 0
    while counter < len(word):
        try:
            subStrCounter = phrase[subStrCounter:].index(word[counter]) + 1
            #print(word[counter], " located at ", subStrCounter-1)
        except:
            return "No"
        counter +=1
    return "Yes"

print(check_for_hidden(in_word, in_phrase))