#!/usr/bin/env python3

import sys

def Hours():

    time=int(sys.argv[1])
    if time < 0:
        try:
            raise ValueError("the type is wrong")
        except ValueError:
            print("ValueError: Input number cannot be negative")
    else:
        hours,minutes=divmod(time, 60)
        print("{} H, {} M".format(hours, minutes))

if __name__=='__main__':

    Hours()
 
