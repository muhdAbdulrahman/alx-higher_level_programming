#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list and only integers

    Args:
        my_list (list): List to print from
        x (int): the number of elements to print from my_list

    Returns:
        number of elements printed
    """
    i = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except(ValueError, TypeError):
            continue
    print()
    return i
