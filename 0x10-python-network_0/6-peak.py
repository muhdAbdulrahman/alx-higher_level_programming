#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""

    if list_of_integers == []:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        peak = list_of_integers[mid]

        if (peak > list_of_integers[mid + 1]):
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
