import math 
import random 

def loss_funcion(num_samples, loss_name):
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return None
    num_samples = int(num_samples)
    
    #random
    predict = [random.uniform(1, 10) for i in range(num_samples)]
    target  = [random.uniform(1, 10) for i in range(num_samples)]
    
    if loss_name == 'MAE':
        loss = sum(abs(y - y_hat) for y, y_hat  in zip(target, predict)) / num_samples
    elif loss_name == 'MSE':
        loss = sum(math.pow(y - y_hat, 2) for y, y_hat in zip(target, predict)) / num_samples
    elif loss_name == 'RMSE':
        loss = math.sqrt(sum(math.pow((y - y_hat), 2) for y, y_hat in zip(target, predict)) / num_samples)
    else:
        print(f"{loss_name} is not support")
        return None
    
    #Output
    print(f"lost name: {loss_name}, sample: {num_samples}, pred: {predict}, target: {target}")
    print("loss:", loss)   

#nhap so luong samples
num_samples = input("So luong samples =")
#nhap ten loss funcion 
loss_name = input("Ten loss funcion =")     

loss_funcion(num_samples, loss_name)

