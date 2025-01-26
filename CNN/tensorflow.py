# cai dat thu vien
# pip install tensorflow 

import numpy as np 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.datasets import mnist
scalar = tf.constant(5)
print(scalar)  # Tensor("Const:0", shape=(), dtype=int32)

tensor1 = tf.constant([1, 2, 3])
tensor2 = tf.constant([4, 5, 6])
result = tensor1 + tensor2
print(result)  # tf.Tensor([5 7 9], shape=(3,), dtype=int32)
