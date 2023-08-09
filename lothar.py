#In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

#   1. take any non-negative and non-zero integer number and name it c0;
#   2. if it's even, evaluate a new c0 as c0 ÷ 2;
#   3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#   4. if c0 ≠ 1, go back to point 2.
#The hypothesis says that regardless of the initial value of c0, it will always go to 1.

co = int(input("Enter your posetive number"))
count = 1
while co !=1:
    if co % 2:
        co = 3 * co + 1
        print(count, "Count", co)
    else:
        co = co // 2
        print(count, "Count", co)
    count+=1    
