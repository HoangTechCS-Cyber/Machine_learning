#Hãy tự viết code thực hiện các yêu cầu sau: 
#1️⃣ Tạo một tensor có kích thước (4,4) chứa toàn số 7.
#2️⃣ Tạo một tensor ngẫu nhiên có kích thước (3,3) với giá trị từ -5 đến 5.
#3️⃣ Tạo hai ma trận 2x2 và thực hiện phép nhân ma trận.
#4️⃣ Chuyển một tensor sang kiểu float32

import tensorflow as tf
import numpy as np

tensor_1 = tf.fill([4, 4], 7) # 1
tensor_random = tf.random.uniform([3, 3], minval = -5, maxval = 5)# 2
#3
array1 = tf.constant([2, 1]) 
array2 = tf.constant([1, 2])
#arr_device = tf.device(array1, array2) 

tensor = tf.cast(tensor_1, dtype= tf.float32 ) #4

print(tensor_1)
print(tensor_random)