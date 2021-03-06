# -*- coding: utf-8 -*-
"""110-1-dl-app-hw1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eb-PJI-B6V-pE4QK6lMTMikpKvQtjL5l
"""
# -*- coding: UTF-8 -*-
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical



from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.callbacks import ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator



# Input data files are available in the "/kaggle/input/108-1-dl-app-hw1/" directory.

TRAIN_DATA_FILE = "C:/Users/Ping/Desktop/ntut-dl/emnist-byclass-train.npz"

TEST_DATA_FILE = "C:/Users/Ping/Desktop/ntut-dl/emnist-byclass-test.npz"

# Load training data
data = np.load(TRAIN_DATA_FILE)



train_labels = data['training_labels']
train_images = data['training_images']

trn_images = train_images.reshape(-1,28,28,1)
trn_images = trn_images.astype('float32') / 255
trn_labels = to_categorical(train_labels)
trn_labels[0]
trn_images.shape
trn_labels.shape

model = Sequential()

model.add(Conv2D(filters = 32, kernel_size =3, activation ='relu', input_shape = (28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(MaxPool2D(pool_size=2))
model.add(Conv2D(filters = 64, kernel_size = 3,activation ='relu'))
model.add(MaxPool2D(pool_size=2))
model.add(Conv2D(filters = 128, kernel_size = 3,activation ='relu'))
model.add(MaxPool2D(pool_size=2))
model.add(Flatten())
model.add(Dense(62, activation='softmax'))

model.summary()

model.compile(optimizer ="adam" , loss = "categorical_crossentropy", metrics=["accuracy"])

#train the model
model.fit(trn_images,trn_labels,validation_split=0.1, epochs=30, batch_size=86)



# Evalute our model on test data
test_images = np.load(TEST_DATA_FILE)['testing_images']

tst_images = test_images.reshape(-1,28,28,1)
tst_images = tst_images.astype('float32') / 255



results = model.predict(tst_images)
results
results = np.argmax(results,axis = 1)
# Print results in CSV format and upload to Kaggle
with open('pred_results_example.csv', 'w') as f:
    f.write('Id,Category\n')
    for i in range(len(results)):
        f.write(str(i) + ',' + str(results[i]) + '\n')

# Download your results!
from IPython.display import FileLink
FileLink("???C:/Users/Ping/Desktop/ntut-dl/pred_results_example.csv")


