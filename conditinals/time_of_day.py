#andrea lugo, how to get the time of day python

import time 
#first instance of time in python
#print(time.gmtime())

#current time in second since gmtime
current = time.time()

#current time as were are used to seeing it
now = time.ctime(current)
print(now)

#get just the hour
local_time = time.localtime(current)
hour = local_time.tm_hour
minutes = local_time.tm_min
print(minutes)

if hour >6 and hour <12:
    print("good morning")
elif hour >12 and hour <18: 
    print("good afternoon")
elif hour >18 and hour <22:
    print("good evening")