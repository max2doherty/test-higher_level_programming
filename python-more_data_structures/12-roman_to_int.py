#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    numerals = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    integer = 0   
    for i in range(len(roman_string)):
        if roman_string[i] not in numerals:
            return 0
        value = numerals[roman_string[i]]
        if i + 1 < len(roman_string) and numerals[roman_string[i + 1]] > value:
            integer -= value
        else:
            integer += value
    return integer
