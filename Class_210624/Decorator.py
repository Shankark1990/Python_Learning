"""   Decorator
A function which takes another function as an argument
which return a new function
"""


def my_decorator(callable):
    def wrapping():
        print("Starting......")
        print("************************")
        callable()
        print("Ended......")
        print("************************")

    return wrapping()


@my_decorator
def say_hello():
    print("Say Hello...")

# say_hello()
