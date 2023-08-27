"""
assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check treat them as non-existent
"""
txt1 = input("Enter first phrase \n")
txt2 = input("Enter second phrase \n")
def check_anagrams(text_1, text_2):
    lst1 = []
    lst2 = []
    for t in text_1:
        if t.isalpha():
            lst1.append(t.lower())

    for t in text_2:
        if t.isalpha():
            lst2.append(t.lower())    
    return sorted(lst1) == sorted(lst2)

print(check_anagrams(txt1,txt2))