#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                # Try to perform the division
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                # Handle division by zero
                result = 0
                print("division by 0")
            except (TypeError, ValueError):
                # Handle non-numeric elements
                result = 0
                print("wrong type")
            except IndexError:
                # Handle out of range
                result = 0
                print("out of range")
            finally:
                # Append the result to the result_list
                result_list.append(result)
    finally:
        # Return the final result_list
        return result_list

