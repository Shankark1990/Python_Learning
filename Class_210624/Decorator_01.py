import time


def note_time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time taken: " + str(end_time - start_time))

    return wrapper()


@note_time_decorator
def log_time():
    time.sleep(5)
    print("Print the log of time taken")
