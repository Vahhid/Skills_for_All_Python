"""
This module will perform the following:
    - asks the user for one line of text to encrypt; (Done)
    - asks the user for a shift value (an integer number from the range 1..25 
     note: you should force the user to enter a valid shift value 
     (don't give up and don't let bad data fool you!) (Done)
    - prints out the encoded text.
Test your code using the data we've provided.
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

