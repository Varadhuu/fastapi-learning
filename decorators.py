def mydecorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@mydecorator
def hello():
    print("Hiii brooo")

hello()