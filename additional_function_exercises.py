def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
#print("Is 1, 3, 4 and triangle? ", is_triangle(1, 3, 4))

def is_right_angled_triangle (a, b, c):
    if (is_triangle(a,b,c)):
        if (a > b and a > c):
            return a **2 == b **2 + c **2
        elif (b > a and b > c):
            return b**2 == a **2 + c**2
        else:
            return c**2 == a **2 + b**2

    else:
        print("This is not a tringle")
        return None
#print("Is 1, 1, 4 a right angled triange?", is_right_angled_triangle(1, 1, 4))
#print("Is 1, 1, 1 a right angled triange?", is_right_angled_triangle(1, 1, 1))
#print("Is 3, 4, 5 a right angled triange?", is_right_angled_triangle(3, 4, 5))
def area_triangle (a, b, c):
    if (is_triangle(a,b,c)):
        s = ( a + b + c)
        return (s *(s-a )+ (s-b)+ (s-c))**0.5
    else:
        print("This is not a tringle")
        return None  

#print("Area of 1, 1, 4 is?", area_triangle(1, 1, 4))
#print("Area of 1, 1, 1 is?", area_triangle(1, 1, 1))
#print("Area of 3, 4, 5 is?", area_triangle(3, 4, 5))
def factorial_function(num):
    if num < 0:
        return None
    elif num < 2:
        return 1
    else:
        factorial_value = 1
        for i in range(1, num+1):
            factorial_value *= i
        return factorial_value

for n in range(1, 6): # testing
    print(n, factorial_function(n))