from datetime import datetime
import datetime

def say_whee():
    print("whee!")

def my_decorator(func):

    def wrapperfunc():
        print("Pre")
        func()
        print("Post")

    return wrapperfunc



def run_twice_decorator(func):

    def wrapper_func():
        func()
        func()
    return wrapper_func

def not_at_night(func):

    def wrapper():
        if 8<= datetime.now().hour <21:
            func()
        else:
            pass
    return wrapper


# say_whee = my_decorator(say_whee)

# say_whee = run_twice_decorator(say_whee)

say_whee = not_at_night(say_whee)

say_whee()
