
def pre_post(func):

    def wrapperfunc():
        print("Pre")
        func()
        print("Post")

    return wrapperfunc

def run_twice(func):
    def wrapper_func():
        func()
        func()
    return wrapper_func


@pre_post
@run_twice
def say_whee():
    print("whee!")
say_whee()