#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []
    for number in my_list:
        if number % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return results
