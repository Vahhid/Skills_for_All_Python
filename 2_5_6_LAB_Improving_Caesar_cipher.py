"""
This module will perform the following:
    - asks the user for one line of text to encrypt; (Done)
    - asks the user for a shift value (an integer number from the range 1..25 
     note: you should force the user to enter a valid shift value 
     (don't give up and don't let bad data fool you!) (Done)
    - prints out the encoded text. 
Test your code using the data we've provided.
A is number 65
Z is number 90
a is number 97
z is number 122
"""
"""
text = input("Enter your message")
shift_is_invalid = True
while shift_is_invalid:
    try:
        shift_no = int(input("Enter the shift number i.e. integer from 1 to 25"))
        if shift_no > 0 and shift_no < 26:
            shift_is_invalid = False
    except:
        print("Please enter an integer value between 1 and 26")
"""
def improved_ceasar(ch, shift):
    if (ord(ch) >= 65 and ord(ch) <= 90): 
        if ord(ch) + shift <=90:
            return chr(ord(ch)+shift)
        else:
            return chr((ord(ch)+shift)-26)
    elif (ord(ch) >= 97 and ord(ch) <= 122):
        if ord(ch) + shift <=122:
            return chr(ord(ch)+shift)
        else:
            return chr((ord(ch)+shift)-26)

    return ch
def cipher(phrase,offset):
    cifer = ""
    for j in phrase:
        cifer +=improved_ceasar(j,offset)
    return cifer
print("")
#Test letters
my_list_capital = list(range(65,91)) 
my_list_small = list(range(97,123))

#print(my_list)
latin_alph_capital = [chr(x) for x in my_list_capital]
latin_alph_small = [chr(x) for x in my_list_small]
capital_test = ""
for i in latin_alph_capital:
    capital_test +=i

small_test = ""
for i in latin_alph_small:
    small_test +=i

print(capital_test)
print("capital shifted 3 is \n ", cipher(capital_test,3))
print(small_test)
print("Small shifted 1 is \n ", cipher(small_test,1))








#print(latin_alph)

