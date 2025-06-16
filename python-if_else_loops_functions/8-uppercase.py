#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            upper_i = chr(ord(i)-32)
            result += upper_i
        else:
            result += i
    print(result)
