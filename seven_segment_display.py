#This program will request the user to provide a number and display as a seven segment
#decimals = list(range(10))
#print(decimals)
#Function for displaying individual decimals
def draw(decimal):
    def horizontal(side):
        if side =="a":
            print(8*"#")
        elif side == "b":
            print(" "," "*4 , "#")
        elif side == "c":
            print("#"," "*4 , "#")
    def vertical(side):
        if side == "x":
            for i in range(3):
                print("#",4*" ","#")
        elif side == "y":
            for i in range(3):
                print(" ",4*" ","#")
        elif side == "z":
            for i in range(3):
                print("#",4*" "," ")
          
    if decimal == 1:
        horizontal("b")
        vertical("y")
        horizontal("b")
        vertical("y")
        horizontal("b")
        print(" ")
    elif decimal == 0:
        horizontal("a")
        vertical("x")
        horizontal("c")
        vertical("x")
        horizontal("a")
        print(" ")

       
    elif decimal == 2:
        horizontal("a")
        vertical("y")
        horizontal("a")
        vertical("z")
        horizontal("a")
        print(" ")

    elif decimal == 3:
        horizontal("a")
        vertical("y")
        horizontal("a")
        vertical("y")
        horizontal("a")
        print(" ")

    elif decimal == 4:
        horizontal("c")
        vertical("x")
        horizontal("a")
        vertical("y")
        horizontal("b")
        print(" ")

    elif decimal == 5:
        horizontal("a")
        vertical("z")
        horizontal("a")
        vertical("y")
        horizontal("a")
        print(" ")

    elif decimal == 6:
        horizontal("a")
        vertical("y")
        horizontal("a")
        vertical("x")
        horizontal("a")
        print(" ")

    elif decimal == 7:
        horizontal("a")
        vertical("y")
        horizontal("b")
        vertical("y")
        horizontal("b")
        print(" ")
    elif decimal == 8:
        horizontal("a")
        vertical("x")
        horizontal("a")
        vertical("x")
        horizontal("a")
        print(" ")
    elif decimal == 9:
        horizontal("a")
        vertical("x")
        horizontal("a")
        vertical("y")
        horizontal("b")
        print(" ")
draw(0)
draw(1)
draw(2)
draw(3)
draw(4)
draw(5)
draw(6)
draw(7)
draw(8)
draw(9)


