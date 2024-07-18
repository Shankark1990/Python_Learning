# Lambda function used where no multiple lines in function
# defined in one line
# use lambda keyword
# Syntax --> lambda argument:expression


def double_salary(salary):
    salary = salary * 2
    return salary


print(double_salary(85000))

f_double_function = lambda salary: salary * 2
print(f_double_function(85000))

check_odd_even = lambda number: "Even" if number % 2 == 0 else "Odd"
print(check_odd_even(11))

squar_num = lambda: int(input("Enter a number")) ** 2
print("Square the number:", squar_num())

my_list = [4, 5, 6, 9, 8, 7]

# def double_num(num):
#     return num * 2
#
#
# double_list = list(map(double_num, my_list))
# print(double_list)
print(list(map(lambda num: num ** 2, [4, 5, 6, 9, 8, 7])))
