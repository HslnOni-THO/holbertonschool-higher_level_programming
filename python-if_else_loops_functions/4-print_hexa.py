#!/usr/bin/python3

for i in range(0, 99):
    print("{:d} = {:x}".format(i, i), end="\n" if i < 98 else "")