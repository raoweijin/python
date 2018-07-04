from datetime import datetime
import time
#start_time = datetime.now()
old_time = datetime.now()
print(old_time)

time.sleep(1)
#start_time = 
print(datetime.now())
start_time = datetime.now()
print(start_time.year,start_time.month,start_time.day,start_time.hour,start_time.minute,start_time.second,start_time.microsecond)
deltatime = start_time.microsecond - old_time.microsecond
print(deltatime)
