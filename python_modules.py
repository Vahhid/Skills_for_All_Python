import math, random, platform
"""
for name in dir(math):
    print(name, end = "\t")
"""
#print(math.pi)
"""
for i in range(10):
    print (i * math.pi , "in radians is ", \
           math.degrees( i * math.pi) , "in degrees")

for i in range(0,361,5):
    print( i , "in degrees is ",\
          round(math.radians(i)/math.pi,2),\
          " PI radians")

          

for i in range(0, 361,5):
    print("Sine of ", i, " degrees or ", \
          round(math.radians(i)/math.pi,2), "PI radians is "

for i in range(5):
    print(random.random())
random.seed(0)
print("\n" *5)
for i in range(5):
    print(random.random())
          ,round(math.sin(math.radians(i)),2))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random.choice(my_list))
print(random.sample(my_list, 5))
print(random.sample(my_list, 10))
"""
print(platform.platform())

print(platform.platform(aliased= True, terse= True))

print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.python_implementation())
print(platform.python_version_tuple())
