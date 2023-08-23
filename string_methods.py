myParagraph = """Let's go through some standard Python string 
methods. We're going to go through them in alphabetical order 
 to be honest, any order has as many disadvantages as advantages,
 so the choice may as well be random.
"""
shortStr = "ALL CAPS"

#print(shortStr.capitalize())
#print(myParagraph.capitalize())
toCenter = "gong"
#print(toCenter +"end")
#print(toCenter.center(20,"/")+"end")
#print(toCenter.endswith("ng"))
#print(myParagraph.find("gong"))
#print("gong" in myParagraph)
#print(shortStr.find("A",1))
myNum = 123
#print(myNum.isalnum())
#print("123".isalnum())
#print("Gong".isalnum())
#print("123Gong".isalnum())
#print("123".islower())
#print("gong".islower())
def mysplit(strng):
    #
    # put your code here
    #
    i = 0
    spaces = []
    spli = []
    for s in strng:
        if s == " ":
            spaces.append(i)
        i += 1
    if spaces == [] or strng.isspace():
        return []
    else:
        spli.append(strng[0:spaces[0]].strip())
        for i in range(len(spaces)-1):
            spli.append(strng[spaces[i]:spaces[i+1]].strip())
        spli.append(strng[spaces[-1]:].strip())
        return spli



    


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
#print("gong123".islower())
