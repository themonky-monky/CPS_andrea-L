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

if hour >7 and hour <8:
    print("good morning")
elif hour >11 and hour <12: 
    print("good afternoon")
elif hour >18 and hour <19:
    print("good evening")