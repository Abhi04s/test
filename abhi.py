from functools import reduce
numbers=[2,4,5,6,8]

def Mysum(a,b):
    return a+b
sum=reduce(Mysum,numbers)
print(sum)
