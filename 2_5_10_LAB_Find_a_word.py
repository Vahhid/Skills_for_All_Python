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
word = input("Enter the word to be searched")
phrase = input("Enter the character stream to check")
