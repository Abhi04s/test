# from functools import reduce
# numbers=[2,4,5,6,8]

# def Mysum(a,b):
#     return a+b
# sum=reduce(Mysum,numbers)
# print(sum)


import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

