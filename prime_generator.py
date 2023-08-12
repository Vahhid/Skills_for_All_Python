def is_prime(num):
    #
    # Write your code here.
    counter = 2
    result = True
    if num == 1:
        return False
    elif num == 2 or num ==3:
        return True
    else:
        while counter < num:
            if num % counter == 0:
                return False
            counter += 1
        return result     
        
    

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
