from PIL import Image
import tensorflow as tf
from keras import models
from keras.layers import Conv2D,\
                         MaxPooling2D,\
                         Dense,\
                         Flatten,\
                         Dropout
import numpy as np
import os
import cv2

rootDir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

# Only run if the data has been cached previously
animals = np.load(rootDir + "\\data\\animalCache.npy")
labels  = np.load(rootDir + "\\data\\labelsCache.npy")

with open(rootDir + "\\data\\animals\\names.txt", 'r') as names:
    animalNames = []
    for name in names:
        animalNames.append(name.rstrip('\n'))

# The following code is only required on first run, data is saved to numpy files
# for easy access in later file runs
'''
animals=[]
labels=[]

counter = 0
for animal in animalNames:
    fileList = os.listdir(rootDir + "\\data\\animals\\" + animal)
    for image in fileList:
        cv2Image = cv2.imread(rootDir + "\\data\\animals\\" + animal + "\\" + image)
        PILImage = Image.fromarray(cv2Image, 'RGB')
        resizedImage = PILImage.resize((50, 50))
        animals.append(np.array(resizedImage))
        labels.append(counter)
    counter += 1

animals=np.array(animals)
labels=np.array(labels)

np.save(rootDir + "\\data\\animalCache",animals)
np.save(rootDir + "\\data\\labelsCache",labels)
'''

# Get the size of the dataset, and the number of different animals
classesAmount = len(animalNames)
dataSize    = len(animals)

# Split data into test and train
(x_train, x_test) =  animals[(int)(0.1 * dataSize):],\
                     animals[:(int)(0.1 * dataSize)]

x_train = x_train.astype('float32') / 255
x_test  = x_test.astype('float32')  / 255

# Get size of the training data, and the testing data\
train_length = len(x_train)
test_length  = len(x_test)

# Split labels into test and train 
(y_train, y_test) =  labels[(int)(0.1*dataSize):],\
                     labels[:(int)(0.1*dataSize)]

# Change from integer classes to binary matrices, better for training since the-
# re is no ordering between the class labels\
y_train = tf.keras.utils.to_categorical(y_train, classesAmount)
y_test  = tf.keras.utils.to_categorical(y_test,  classesAmount)

# # Use the below code if training hasn't been performed yet
# trainingModel = models.Sequential()
# trainingModel.add(Conv2D(filters=16,kernel_size=2,padding="same",activation="relu",input_shape=(50,50,3)))
# trainingModel.add(MaxPooling2D(pool_size=2))
# trainingModel.add(Conv2D(filters=32,kernel_size=2,padding="same",activation="relu"))
# trainingModel.add(MaxPooling2D(pool_size=2))
# trainingModel.add(Conv2D(filters=64,kernel_size=2,padding="same",activation="relu"))
# trainingModel.add(MaxPooling2D(pool_size=2))
# trainingModel.add(Dropout(0.2))
# trainingModel.add(Flatten())
# trainingModel.add(Dense(500,activation="relu"))
# trainingModel.add(Dropout(0.2))
# trainingModel.add(Dense(classesAmount,activation="softmax"))
# trainingModel.summary()

# trainingModel.compile(loss='categorical_crossentropy', 
#                       optimizer='adam', 
#                       metrics=['accuracy'])

# trainingModel.fit(x_train, 
#                   y_train, 
#                   batch_size=50,
#                   epochs=100)

# # Save the trained model to file, to skip training later
# trainingModel.save(rootDir + "\\data\\model.keras")

# Use if model has been trained already
trainingModel = models.load_model(rootDir + "\\data\\model.keras")
score = trainingModel.evaluate(x_test, y_test)
print('\n', 'Test accuracy:', score)

def convert_to_array(img):
    im = cv2.imread(img)
    img = Image.fromarray(im, 'RGB')
    image = img.resize((50, 50))
    return np.array(image)

def predict_animal(file):
    print("Predicting .................................")
    ar=convert_to_array(file)
    ar=ar/255
    a=[]
    a.append(ar)
    a=np.array(a)
    score=trainingModel.predict(a,verbose=1)
    label_index=np.argmax(score)
    acc=np.max(score)
    print("The predicted Animal is a "+animalNames[label_index]+" with accuracy =    "+str(acc))

predict_animal(rootDir + "\\data\\animals\\coyote\\0a151f5c78.jpg")