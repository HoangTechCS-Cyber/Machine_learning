import numpy as np


# Md_nRE funcion 
def md_nre(predict, target, n = 2, p = 1 ):
    return sum(pow(y - y_hat, p) for y, y_hat in zip(predict, target)) / np.size(predict)


predict = [99.5, 49.5, 19.5, 0.1]
target = [100, 50, 20, 0.6] 

# calculate sqrt for predict and target
predict = np.sqrt(predict)
target = np.sqrt(target)

print(md_nre(predict, target))

