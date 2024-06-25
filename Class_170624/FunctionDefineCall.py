def say_hello():
    print("Function called...")


say_hello()


def say_hello_arg(name):
    print("Function parameter with arguments :", name)

say_hello_arg("Shankar")

def say_hello_arg_default(name="Shankar"):
    print("Hello",name)

#say_hello_arg_default()   #If nothing is passed in the parmeter then default argument will pick.
say_hello_arg_default("Ram") #If parameter is passed then default argument will be ignored.

