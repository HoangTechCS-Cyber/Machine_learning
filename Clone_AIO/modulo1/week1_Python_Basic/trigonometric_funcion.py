import math 

def factorial(n):
    if n == 0 or n==1:
        return 1
    if n > 1:
        return n*factorial(n-1)
    
def approx_sin(x, n):
    return sum(( pow(-1, i) * (pow(x, 2*i + 1)/factorial(2*i + 1)) for i in range(n)))

def approx_cos(x, n):
    return sum((pow(-1, i)* (pow(x, 2*i))/factorial(2*i))for i in range(n))

def approx_sinh(x, n):
    return sum((pow(x, 2*i+1))/factorial(2*i + 1) for i in range(n))
def approx_cosh(x, n):
    return sum(pow(x, 2*i)/factorial(2*i) for i in range(n))
x = float(input("so muon tinh toan ="))
n = int(input("so lan lap muon xap xi ="))


print(approx_sin(x=3.14, n=10)) #>> 0.0015926529267151343
print(approx_cos(x=3.14, n=10)) #>> -0.9999987316527259
print(approx_sinh(x=3.14, n=10)) #>> 11.53029203039954
print(approx_cosh(x=3.14, n=10)) #>> 11.573574828234543

