#This program will request the user to provide a number and display as a seven segment
#decimals = list(range(10))
#print(decimals)
#Function for displaying individual decimals
def draw(z):
    def horizontal(side):
        if side == 1:
            print(8*"#")
        elif side == 2:
            print(" "," "*4 , "#")
        elif side == 3:
            print("#"," "*4 , "#")
    def vertical(side):
        if side == 1:
            for i in range(3):
                print("#",4*" ","#")
        elif side == 2:
            for i in range(3):
                print(" ",4*" ","#")
        elif side == 3:
            for i in range(3):
                print("#",4*" "," ")
    mp = [[1,1,3,1,1], [2,2,2,2,2], [1,2,1,3,1], [1,2,1,2,1], [3,1,1,2,2], \
            [1,3,1,2,1], [1,2,1,1,1], [1,2,2,2,2], [1,1,1,1,1], [1,1,1,2,2] ]  
    horizontal(mp[z][0])
    vertical(mp[z][1])
    horizontal(mp[z][2])
    vertical(mp[z][3])
    horizontal(mp[z][4])
    print(" ")
    
    """
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
        [1,2,1,3,1]
      

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
"""
for i in range(10):
    print(i,"/n")
    draw(i)        
    



