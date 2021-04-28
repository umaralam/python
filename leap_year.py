#!/usr/bin/python3
def is_leap(year):
    leap = False
    if 1900<= year <=pow(10,5):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        else:
            return False
    return leap

year = int(input())
print(is_leap(year))
