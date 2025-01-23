#activation funcion 

import numpy as np 

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# sigmoid funcion 
def sigmoid(x):
    print(1/(1 + np.exp(-x)))
    return 

# Relu funcion 
def relu(x):
    print(np.maximum(0, x))
    return 

#Elu funcion 
def elu(x):
    print(0.01*(np.exp(x) - 1))
    return 

#activation funcion 
def activation_funcion(funcion_name, x):
    if not is_number(x):
        print("x must be a number")
        return None
    x = float(x)
    if funcion_name == 'sigmoid':
        return sigmoid(x)
    elif funcion_name == 'relu':
        return relu(x)
    elif funcion_name == 'elu':
        return elu(x)
    else: 
        print(funcion_name,"is not supported")


x = input("Input x =")
funcion_name = 'elu'
activation_funcion(funcion_name, x)