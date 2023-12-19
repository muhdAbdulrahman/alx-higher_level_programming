#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """This will divide two list element by element.

    Args:
        my_list_1 (list): The initial list.
        my_list_2 (list): The second list.
        list_length (int): The amount of elements to divide.

    Returns:
        new list of length list_length accomodating all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            my_func = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            my_func = 0
        except ZeroDivisionError:
            print("division by 0")
            my_func = 0
        except IndexError:
            print("out of range")
            my_func = 0
        finally:
            new_list.append(my_func)
    return (new_list)
