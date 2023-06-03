"""
    Find number of days above average temperature.
    User inputs number of days and each day temperature.
"""
from array import *


def initialize() -> ArrayType:
    days_count = int(input("Input how many days you want to analyse"))
    temp = array('d')
    for i in range(days_count):
        input_temp = float(input(f"Input day {i} temperature"))
        temp.append(input_temp)

    return temp


def calculate_average(arr: ArrayType) -> float:
    return sum(arr) / len(arr)


def count_above_avg(avg: float, days: ArrayType) -> int:
    count: int = 0
    for day_temp in days:
        if day_temp > avg:
            count += 1

    return count


temperature = initialize()
average = calculate_average(temperature)
print(round(average, 2))
print(count_above_avg(average, temperature))

