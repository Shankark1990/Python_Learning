# Function with no argument..
def say_hello():
    print("Function called...")


say_hello()


# Function with argument
def say_hello_arg(name):
    print("Function parameter with arguments :", name)


say_hello_arg("Shankar")


def say_hello_arg_default(name="Shankar"):  # Default argument function
    print("Hello", name)


# say_hello_arg_default()   #If nothing is passed in the parmeter then default argument will pick.
say_hello_arg_default("Ram")  # If parameter is passed then default argument will be ignored.


def sum_number_arg_ret(a, b):  # Function with argument and returning the value
    return a + b


add = sum_number_arg_ret(1, 3)
print("Sum of numbers", add)


def print_argument(*arg):
    for i in arg:
        print(i, end="\n")


print_argument(1, 6, 6, 9, 23, "abc", 4)
