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

"""
calculate the days in a given month given the Year and month in number
"""
def days_in_month(year, month):
    # Write your new code here.
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 31, 31, 30, 31]
    #Remove invalid month and year from result
    if year < 1582 or (month < 1 or month > 12):
        print ("Invalid input")
        return None
    else:
        if is_year_leap(year) and month == 2:
            return days_in_months[month -1] + 1
        else:
            return days_in_months[month -1]
in_month = int(input("Now enter the month in number: "))
print("The month ", in_year, "-", in_month , "has ",days_in_month(in_year, in_month)," days")