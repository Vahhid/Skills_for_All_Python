#This program will request the user to provide a number and display as a seven segment
decimals = list(range(10))
print(decimals.reverse())
#Function for displaying individual decimals
def draw(z):
    def horizontal(side):
        if side == 1:
            return 8*"#"
        elif side == 2:
            return " "*7 + "#"
        elif side == 3:
            return "#"+" "*6 + "#"
    def vertical(side):
        endStr = ""
        if side == 1:
            endStr ="#"+6*" "+"#"
        elif side == 2:
            endStr =" "+6*" "+"#"
        elif side == 3:
            endStr ="#"+6*" "+" "
        return endStr
    mp = [[1,1,3,1,1], [2,2,2,2,2], [1,2,1,3,1], [1,2,1,2,1], [3,1,1,2,2], \
            [1,3,1,2,1], [1,3,1,1,1], [1,2,2,2,2], [1,1,1,1,1], [1,1,1,2,2] ] 
    for i in range(len(z)):
        print(horizontal(mp[z[i]][0]), end= "   ")
    print("")
    for j in range(3):
        for i in range(len(z)):
            print(vertical(mp[z[i]][1]), end= "   ")
        print("")
    
    for i in range(len(z)):
        print(horizontal(mp[z[i]][2]), end= "   ")
    print("")
    for j in range(3):
        for i in range(len(z)):
            print(vertical(mp[z[i]][3]), end= "   ")
        print("")
    for i in range(len(z)):
        print(horizontal(mp[z[i]][4]), end= "   ")

draw(decimals)

