from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras import losses
from keras import optimizers
import pandas as pd
import numpy as np

#input_a = pd.read_csv("./out2_vec.txt", delimiter=" ").to_numpy()
add_with4  = pd.read_csv("../vecs/add_with4.txt", delimiter=" ").to_numpy()
add_with8  = pd.read_csv("../vecs/add_with8.txt", delimiter=" ").to_numpy()
add_with16 = pd.read_csv("../vecs/add_with16.txt", delimiter=" ").to_numpy()
add_with32 = pd.read_csv("../vecs/add_with32.txt", delimiter=" ").to_numpy()
add_with64 = pd.read_csv("../vecs/add_with64.txt", delimiter=" ").to_numpy()
sub_with4  = pd.read_csv("../vecs/sub_with4.txt", delimiter=" ").to_numpy()
sub_with8  = pd.read_csv("../vecs/sub_with8.txt", delimiter=" ").to_numpy()
sub_with16 = pd.read_csv("../vecs/sub_with16.txt", delimiter=" ").to_numpy()
sub_with32 = pd.read_csv("../vecs/sub_with32.txt", delimiter=" ").to_numpy()
sub_with64 = pd.read_csv("../vecs/sub_with64.txt", delimiter=" ").to_numpy()

add_with4  = np.delete(add_with4, 0, 1) 
add_with8  = np.delete(add_with8, 0, 1) 
add_with16  = np.delete(add_with16, 0, 1) 
add_with32  = np.delete(add_with32, 0, 1) 
add_with64  = np.delete(add_with64, 0, 1) 

sub_with4  = np.delete(sub_with4, 0, 1) 
sub_with8  = np.delete(sub_with8, 0, 1) 
sub_with16  = np.delete(sub_with16, 0, 1) 
sub_with32  = np.delete(sub_with32, 0, 1) 
sub_with64  = np.delete(sub_with64, 0, 1) 

print(add_with4.shape)
print(add_with8.shape)
print(add_with16.shape)
print(add_with32.shape)
print(add_with64.shape)

print(sub_with4.shape)
print(sub_with8.shape)
print(sub_with16.shape)
print(sub_with32.shape)
print(sub_with64.shape)


print(add_with4)

#input_a  = input_a[np.newaxis, ..., np.newaxis] 
add_with4  = add_with4[np.newaxis, ..., np.newaxis] 
add_with8  = add_with8[np.newaxis, ..., np.newaxis] 
add_with16 = add_with16[np.newaxis, ..., np.newaxis]
add_with32 = add_with32[np.newaxis, ..., np.newaxis]
add_with64 = add_with64[np.newaxis, ..., np.newaxis]
sub_with4  = sub_with4[np.newaxis, ..., np.newaxis] 
sub_with8  = sub_with8[np.newaxis, ..., np.newaxis] 
sub_with16 = sub_with16[np.newaxis, ..., np.newaxis]
sub_with32 = sub_with32[np.newaxis, ..., np.newaxis]
sub_with64 = sub_with64[np.newaxis, ..., np.newaxis]

 
print(add_with4.shape)
print(add_with8.shape)
print(add_with16.shape)
print(add_with32.shape)
print(add_with64.shape)

print(sub_with4.shape)
print(sub_with8.shape)
print(sub_with16.shape)
print(sub_with32.shape)
print(sub_with64.shape)

add_with4 = np.pad(add_with4, [(0, 0), (0, 710 - add_with4.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0) 
add_with8 = np.pad(add_with8, [(0, 0), (0, 710 - add_with8.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0) 
add_with16 = np.pad(add_with16, [(0, 0), (0, 710 - add_with16.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0)
add_with32 = np.pad(add_with32, [(0, 0), (0, 710 - add_with32.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0)
add_with64 = np.pad(add_with64, [(0, 0), (0, 710 - add_with64.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0)
sub_with4 = np.pad(sub_with4, [(0, 0), (0, 710 - sub_with4.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0) 
sub_with8 = np.pad(sub_with8, [(0, 0), (0, 710 - sub_with8.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0) 
sub_with16 = np.pad(sub_with16, [(0, 0), (0, 710 - sub_with16.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0)
sub_with32 = np.pad(sub_with32, [(0, 0), (0, 710 - sub_with32.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0)
sub_with64 = np.pad(sub_with64, [(0, 0), (0, 710 - sub_with64.shape[1]), (0,0), (0,0)], mode='constant', constant_values=0)


print(add_with4)

print(add_with4.shape)
print(add_with8.shape)
print(add_with16.shape)
print(add_with32.shape)
print(add_with64.shape)

print(sub_with4.shape)
print(sub_with8.shape)
print(sub_with16.shape)
print(sub_with32.shape)
print(sub_with64.shape)

model = Sequential()
model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(710,128,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(1))

adam = optimizers.Adam(lr=0.00001, beta_1=0.9, beta_2=0.999, amsgrad=False)
model.compile(loss='mean_squared_error', optimizer='adam')
x = np.concatenate((add_with4, add_with8, add_with16, add_with32, add_with64, sub_with4, sub_with8, sub_with16, sub_with32, sub_with64), axis = 0)
print(x.shape)
y = np.concatenate(([17.02], [34.048], [93.1], [186.200001], [458.584003], [20.216], [39.368], [113.82001], [226.632002], [472.948003]), axis = 0)
print(y.shape)
model.fit(x, y, batch_size=1, nb_epoch=50, verbose=1)


