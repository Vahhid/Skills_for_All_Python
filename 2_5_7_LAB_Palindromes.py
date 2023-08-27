"""
Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints the result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check – treat them as non-existent;
there are more than a few correct solutions – try to find more than one.
"""
text = input("Enter the phrase to be checked \n")
def check_for_palidrome(txt):
    txt = txt.lower()
    lst= []
    for t in txt:
        if t.isalpha():
            lst.append(t)
    return lst == list(reversed(lst))

print(check_for_palidrome(text))
 