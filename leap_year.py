"""
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
"""

def is_year_leap(year):
    # Write your code here.
    if year < 1582:
        return "Please enter year greater than 1582"
    elif year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True
    
in_year = int(input("Enter the year you need to check:"))
if is_year_leap(in_year) == True:
    print("The year ", in_year," is a leap year.")
elif is_year_leap(in_year) == False:
    print("The year ", in_year, "is ordinary year.")
else:
    print("Enter a year greater than 1582")