#lists
#numbers = [10,5,7,2,1]
#print("original contents of numbers",numbers)
#numbers[0]=111
#print("changed contents of numbers",numbers)
#del numbers[0]
#print(len(numbers))
#print("After delete: ",numbers)
#out of range
#print(numbers[4])
#Negative index
#print(numbers[-2])
"""
numbers.append("Appended")
print(numbers)
numbers.insert(1,"inserted")
print(numbers)
"""
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Write your code here.
k = len(my_list)
i = 0
#One forward run through the list while checking the rest for a similar entry
while i < k:
    if  my_list[i] in (my_list[:i] + my_list[i+1:]):
        #print("removed: ", my_list[i])
        del my_list[i]
        k = len(my_list)
        i = i -1
    #print(my_list , " on run", i, "and element ", my_list[i])
    i+=1
    

print("The list with unique elements only:")
print(my_list)

