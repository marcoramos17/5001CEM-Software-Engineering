# For path tools
import os
# To stop tensorflow from printing useless information to console
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
# For image tools
from PIL import Image
# For machine learning tools
import tensorflow as tf
# For plotting
import matplotlib.pyplot as plt
# For IO manipulation
import io 
# Not strictly needed since tensorflow is included in tf, but pylance likes to -
# be picky and throw linting errors all over the place otherwise. There are also
# slight discrepancies between the versions, but that's another story
import keras
# Explicit names for the above
from keras import Sequential
from keras.layers import Conv2D,\
                        MaxPooling2D,\
                        Dense,\
                        Flatten,\
                        Dropout
# For numeric operations
import numpy as np
# For converting images to an array to then be used by other libraries
import cv2

# Get the root directory of where the project file is
rootDir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# Append to get the animals directory
animalsDir = rootDir + "/data/animals/"

# Open the file of animal names, using with so the file closes no matter what
animalNames = []
with open(animalsDir + "names.txt", 'r') as names:
    for name in names:
        animalNames.append(name.rstrip('\n'))

# Load our pretrained model if not running the training file
if __name__ != "__main__":
    trainingModel = keras.models.load_model(rootDir + 
                                            "/data/ML/modelLinux.keras")

def cache_arrays() -> None:
    print("Caching Arrays")
    animals = []
    labels = []
    counter = 0
    for animal in animalNames:
        fileList = os.listdir(rootDir + "/data/animals/" + animal)
        for image in fileList:
            cv2Image = cv2.imread(rootDir + 
                                  "/data/animals/" + animal + 
                                  "/" + image)
            PILImage = Image.fromarray(cv2Image, 'RGB')
            resizedImage = PILImage.resize((64, 64))
            animals.append(np.array(resizedImage))
            labels.append(counter)
        counter += 1

    animals=np.array(animals)
    labels=np.array(labels)
    np.save(rootDir + "/data/ML/animalCache",animals)
    np.save(rootDir + "/data/ML/labelsCache",labels)
    print("Arrays Cached")


def train_model(f_outputFilename: str) -> None:
    animals = np.load(rootDir + "/data/ML/animalCache.npy")
    labels  = np.load(rootDir + "/data/ML/labelsCache.npy")

    # Generate a list of indexes
    randomShuffle = np.arange(len(animals))
    # Give a random permutation
    rngShuffle = np.random.permutation(len(animals))
    # Shuffle both lists, this helps with training and validation
    animals = animals[rngShuffle]
    labels = labels[rngShuffle]

    # Get the size of the dataset, and the number of different animals
    classesAmount = len(animalNames)
    dataSize      = len(animals)

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

    # Change from integer classes to binary matrices, better for training since 
    # there is no ordering between the class labels\
    y_train = tf.keras.utils.to_categorical(y_train, classesAmount)
    y_test  = tf.keras.utils.to_categorical(y_test,  classesAmount)

    # These parameters are a combination of various configurations that I have 
    # seen online whilst passing through various CNN optimation pages
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

    trainingModel.fit(x_train, 
                      y_train, 
                      batch_size = 100,
                      epochs = 100,
                      validation_data = (x_test, y_test))
    
    # Save the trained model to file, to skip training later
    trainingModel.save(rootDir + "/data/{}.keras".format(f_outputFilename))

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

def get_scaled_image(f_filePath: str) -> Image.Image:
    return Image.fromarray(image_to_array(f_filePath)[:, :, ::-1])

if __name__ == "__main__":
    # # Use if arrays not cached
    # cache_arrays()
    # # Use if model not trained
    # train_model("TrainedModel")
    print("mlearnTrainer ran from main")
