"""
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple – you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:
1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
"""
birth_day = input("Enter your birthday in YYYYMMDD format \n")
life_digit = birth_day
try:
    while len(life_digit) > 1:
        sum = 0
        for i in range(len(life_digit)):
            sum+=int(life_digit[i])
        life_digit = str(sum)
    print("Your digit of life is:", life_digit)

except:
    print("Please enter valid birth date in the correct format")
