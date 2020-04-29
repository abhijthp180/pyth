import time
import datetime
import sys
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M"))
d2 = datetime.datetime(2020, 3, 26,21,7) 
print(d2)
while 1 :
  now = datetime.datetime.now()  
  if(now.strftime("%Y-%m-%d %H:%M")==d2.strftime("%Y-%m-%d %H:%M")):
    print("its time")
    sys.exit()
  print (now.strftime("%Y-%m-%d %H:%M"))
  print(d2.strftime("%Y-%m-%d %H:%M"))
  time.sleep(10)

