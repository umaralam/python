#!/usr/bin/python3

from datetime import datetime
import time

dt1 = datetime(2021, 3, 16)
print(dt1)

dt2 = datetime.now()
print(dt2)
##strptime converts a string to a datetime object##
dt = datetime.strptime("2021/03/16", "%Y/%m/%d")
print(dt)

dt = datetime.fromtimestamp(time.time())
print(f"{dt.year}/{dt.month}")

##converts a datetime object to a string##
print(dt.strftime("%Y/%m"))

##comparing datetime objects

print(dt1 < dt2)
