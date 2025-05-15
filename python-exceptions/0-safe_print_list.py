#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for item in my_list[:x]:
        print(item, end="")
        n += 1
    print()
    return n
