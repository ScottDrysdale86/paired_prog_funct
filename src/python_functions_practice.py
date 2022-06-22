

def return_10():
    return 10


def add(num1, num2):
    add_result = num1+num2
    return add_result


def subtract(num1, num2):
    subtract_result = num1 - num2
    return subtract_result


def multiply(num1, num2):
    multiply_result = num1 * num2
    return multiply_result


def divide(num1, num2):
    divide_results = num1 / num2
    return divide_results


def length_of_string(test_string):
    string_length = len(test_string)
    return string_length


def join_string(string_1, string_2):
    joined_string = string_1 + string_2
    return joined_string


def add_string_as_number(string1, string2):
    add_result = int(string1) + int(string2)
    return add_result


def number_to_full_month_name(month_number):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[month_number - 1]


def number_to_short_month_name(month_number):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    return months[month_number - 1]


def cube_volume(num1):
    volume_of_cube = num1*num1*num1
    return volume_of_cube


def reverse_string(string1):
    string_reverse = string1[::-1]
    return string_reverse


def fahrenheight_to_celsius(fahrenheight):
    celsius = (fahrenheight - 32) * 5/9
    return int(celsius)
