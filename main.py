import time
import datetime

curr_time = datetime.datetime.now()

while True:
  time.sleep(1)
  diff = (datetime.datetime.now() - curr_time).total_seconds()
  print(diff)

  # When PC/Laptop is put to sleep
  if diff > 10: 
    print("I just wake up after sleep") 
    break
  curr_time = datetime.datetime.now()