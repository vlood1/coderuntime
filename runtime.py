# Import time module
import time
 
# record start time
start = time.time()
 
# define a sample code segment
a = 0
for i in range(1000):
    a += (i**100)
 
# record end time
end = time.time()
 
# print the difference between start 
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")