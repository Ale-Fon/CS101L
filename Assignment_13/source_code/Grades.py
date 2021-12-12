import math


def total(values : list) -> float:
    total = 0
    for item in values:
        total = total + item
    return total

def average(values : list) -> float:
    if len(values) == 0:
        return math.nan
    return total(values) / len(values)

def median(values: list) -> float:
    try:
        data = sorted(values)
        index = len(values) // 2
        if len(values) % 2 != 0:
            return data[index]
        return (data[index - 1] + data[index]) / 2
    except:
        if len(values) == 0:
            raise ValueError('Empty List')
    
