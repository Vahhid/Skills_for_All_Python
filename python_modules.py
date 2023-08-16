import math
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

          
"""
for i in range(0, 361,5):
    print("Sine of ", i, " degrees or ", \
          round(math.radians(i)/math.pi,2), "PI radians is "
          ,round(math.sin(math.radians(i)),2))