# very poweful feature in python
# every advanced python programmer should know it

# concept behind decoraters, function, class decoraters 

# function decorators
# allows to add new functionality to an existing function
# in the below case, mydecorator adds more functionality to dosomething

# we can use this as a template to write further decorators

#@mydecorator
def dosomething():
    pass

# functions in python are first class objects, meaning, they can be :
# defined inside another function
# pass function as argument to another function
# function can be returned from another funciton

def start_end_decorator(func):
    
    def wrapper():
        # before
        print('start')
        func()
        # after
        print('end')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# print_name = start_end_decorator(print_name)
# above is the same as @start_end_decorator

print_name()

# function with arguments

import functools

def decorator_for_func_with_params(func):
    @functools.wraps(func)  # to preserve the name and other details of the wrapped function
    def wrapper(*args, **kwargs): # use as many args and keyword args
        # before
        print("start")
        result = func(*args, **kwargs) # if the function needs to return a result, capture it and return
        # after
        print("end")
        return result
    return wrapper  # don't forget to return the wrapped function

@decorator_for_func_with_params
def add5(x):
    return x + 5

print(add5(2))

# function identities
# print(help(add5)) when wrappning a function, if the functools wrap is not in place the context of the wrapped function is not preserved


# wrapper function taking arguments

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"hello {name}")

greet("vivi")

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"calling {func.__name__} ({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@decorator_for_func_with_params
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello("vivi")


# class decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs): # this function is invoked on object call
        self.num_calls += 1
        print(f'this is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello_cd():
    print('hello from cd')

say_hello_cd()
say_hello_cd()