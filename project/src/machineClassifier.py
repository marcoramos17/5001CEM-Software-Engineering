import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
from keras import Sequential
from keras.layers import Conv2D,\
                        MaxPooling2D,\
                        Dense,\
                        Flatten,\
                        Dropout
import numpy as np

import cv2

rootDir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
animalsDir = rootDir + "/data/animals/"

# Only run if the data has been cached previously
animals = np.load(rootDir + "/data/animalCache.npy")
labels  = np.load(rootDir + "/data/labelsCache.npy")

randomShuffle = np.arange(len(animals))
rngShuffle = np.random.permutation(len(animals))
animals = animals[rngShuffle]
labels = labels[rngShuffle]

with open(animalsDir + "names.txt", 'r') as names:
    animalNames = []
    for name in names:
        animalNames.append(name.rstrip('\n'))

# The following code is only required on first run, data is saved to numpy files
# for easy access in later file runs

# USE IF ARRAYS NOT CACHED
'''print("caching arrays")
animals = []
labels = []
counter = 0
for animal in animalNames:
    fileList = os.listdir(rootDir + "\\data\\animals\\" + animal)
    for image in fileList:
        cv2Image = cv2.imread(rootDir + "\\data\\animals\\" + animal + "\\" + image)
        PILImage = Image.fromarray(cv2Image, 'RGB')
        resizedImage = PILImage.resize((64, 64))
        animals.append(np.array(resizedImage))
        labels.append(counter)
    counter += 1

animals=np.array(animals)
labels=np.array(labels)

np.save(rootDir + "/data/animalCache",animals)
np.save(rootDir + "/data/labelsCache",labels)
print("done caching arrays")'''
# END USE


# Get the size of the dataset, and the number of different animals
classesAmount = len(animalNames)
dataSize      = len(animals)

# USE IF MODEL NOT TRAINED
# Split data into test and train
(x_train, x_test) =  animals[(int)(0.1 * dataSize):],\
                     animals[:(int)(0.1 * dataSize)]
# Split labels into test and train 
(y_train, y_test) =  labels[(int)(0.1*dataSize):],\
                     labels[:(int)(0.1*dataSize)]

x_train = x_train.astype('float32') / 255
x_test  = x_test.astype('float32')  / 255

# Get size of the training data, and the testing data\
train_length = len(x_train)
test_length  = len(x_test)

# Change from integer classes to binary matrices, better for training since the-
# re is no ordering between the class labels\
y_train = tf.keras.utils.to_categorical(y_train, classesAmount)
y_test  = tf.keras.utils.to_categorical(y_test,  classesAmount)


# USE the below code if training hasn't been performed yet
# These parameters are a combination of various configurations that I have seen
# online whilst passing through various CNN optimation pages
data_augmentation = tf.keras.Sequential([
  tf.keras.layers.RandomFlip("horizontal_and_vertical"),
  tf.keras.layers.RandomRotation(0.2),
])

trainingModel = Sequential()
trainingModel.add(Conv2D(16, 2, activation = "relu", input_shape=(64, 64, 3)))
trainingModel.add(MaxPooling2D())
trainingModel.add(Conv2D(32, 2, activation = "relu", padding="same"))
trainingModel.add(MaxPooling2D())
trainingModel.add(Conv2D(64, 2, activation = "relu", padding="same"))
trainingModel.add(MaxPooling2D())
# I have read that this helps to protect against overfitting
trainingModel.add(Dropout(0.5))
trainingModel.add(Flatten())
trainingModel.add(Dense(512, activation = "relu"))
trainingModel.add(Dropout(0.5))
trainingModel.add(Dense(classesAmount, activation = "softmax"))

trainingModel.compile(loss='categorical_crossentropy', 
                      optimizer='adam', 
                      metrics=['accuracy'])

# trainingModel.fit(x_train, 
#                   y_train, 
#                   batch_size = 100,
#                   epochs = 100,
#                   validation_data = (x_test, y_test))
#
# # Save the trained model to file, to skip training later
# trainingModel.save(rootDir + "/data/model2.keras")

# END USE
# Use if model has been trained already
trainingModel = keras.models.load_model(rootDir + "/data/model2.keras")

def image_to_array(f_imagePath: str) -> np.ndarray:
    cv2Image = cv2.imread(f_imagePath)
    pilImage = Image.fromarray(cv2Image, 'RGB')
    image = pilImage.resize((64, 64))
    return np.array(image)

def show_scaled_image(f_filePath: str) -> None:
    imageArray  = image_to_array(f_filePath)
    plt.figure()
    plt.imshow(imageArray)
    plt.colorbar()
    plt.grid(False)
    plt.show()

def predict_animal_from_file(f_filePath: str) -> tuple[str, str]:
    imageArray  = image_to_array(f_filePath)
    imageArray  = imageArray / 255
    imageArray  = np.array([imageArray])
    score       = trainingModel.predict(imageArray) #type: ignore
    label_index = np.argmax(score)
    acc         = np.max(score)
    return animalNames[label_index], str(acc)

def make_animal_prediction_to_user(f_filePath: str) -> tuple[str, str]:
    prediction, accuracy = predict_animal_from_file(f_filePath)
    if float(accuracy) >= 0.75:
        return prediction, accuracy + " (High)"
    elif float(accuracy) >= 0.40:
        return prediction, accuracy + " (Moderate)"
    else:
        return prediction, accuracy + " (Low)"


if __name__ == "__main__":
    # animal, acc = predict_animal_from_file(animalsDir + "cat/0b54dde5f5.jpg")
    # print("Prediction: {}\nAccuracy: {}".format(animal, acc))
    None
