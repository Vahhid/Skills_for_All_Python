
#1 American mile = 1609.344 metres;;
#1 American gallon = 3.785411784 litres.

def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    return liters *100 *(3.785411784 * 1.609344 )

def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here.
    return miles  

print("test results")
print(liters_100km_to_miles_gallon(3.9) == 60.31143162393162)
print(liters_100km_to_miles_gallon(7.5) == 31.36194444444444)
print(liters_100km_to_miles_gallon(10.) == 23.52145833333333)

print(liters_100km_to_miles_gallon(3.9) )
print(liters_100km_to_miles_gallon(7.5) )
print(liters_100km_to_miles_gallon(10.) )

"""
print(miles_gallon_to_liters_100km(60.3) == 3.9007393587617467)
print(miles_gallon_to_liters_100km(31.4) == 7.490910297239916)
print(miles_gallon_to_liters_100km(23.5) == 10.009131205673757)
"""