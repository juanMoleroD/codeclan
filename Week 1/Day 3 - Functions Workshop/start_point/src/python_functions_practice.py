def return_10():
    return 10

def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a, b):
    return a / b

def length_of_string(str):
    return len(str)

def join_string(str1, str2):
    return str1 + str2

def add_string_as_number(a, b):
    return int(a) + int(b)

def number_to_full_month_name(month):
    months = ['', "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]
    return months[month]

def number_to_short_month_name(month):
    months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
    "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[month]

def volume_of_cube(side):
    return side ** 3
