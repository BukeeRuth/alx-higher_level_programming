#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Error: Division by zero")
    except Exception as e:
        result = None
        print("Error:", e)
    finally:
        print("Inside result: {}".format(result))
        return result
