#!/usr/bin/python3
def uniq_add(my_list=[]):
    total_sum = 0
    unique_numbers = []
    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
            total_sum += number
    return total_sum
