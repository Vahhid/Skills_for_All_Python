#In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

#   1. take any non-negative and non-zero integer number and name it c0;
#   2. if it's even, evaluate a new c0 as c0 ÷ 2;
#   3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#   4. if c0 ≠ 1, go back to point 2.
#The hypothesis says that regardless of the initial value of c0, it will always go to 1.
#This code tests the hypothesis for numbers up to a maximum limit given by the user
max_num = int(input("Enter the limit of the test"))
co = 2
while co <= max_num:
    #co = int(input("Enter your posetive number"))
    count = 1
    reSult = co
    while reSult !=1:
        if reSult % 2:
            reSult = 3 * reSult + 1
            #print("(",reSult,",",count,")")
        else:
            reSult = reSult // 2
            #print("(",reSult,",",count,")")
        count+=1   
    print("for ", co, "needed steps ", count)
    co +=1
