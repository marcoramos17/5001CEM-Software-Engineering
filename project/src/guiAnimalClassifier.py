from mlearnTrainer import *
from guizero import App, Text, PushButton, Picture


def get_file():
    filePath                = animalClassifier.select_file()
    animal, accuracy        = make_animal_prediction_to_user(filePath)
    animalMessage.value     = animal
    accuracyMessage.value   = accuracy
    picture.value           = filePath
    postResizePicture.value = get_scaled_image(filePath)

animalClassifier = App()

Text(animalClassifier, text = "Uploaded Image")
picture = Picture(animalClassifier, 
                  image= rootDir + "/data/ML/classifierSplash.png",
                  width=200,
                  height=200)

Text(animalClassifier, text = "Post-Resized Image")
postResizePicture = Picture(animalClassifier, 
                            image= rootDir + "/data/ML/classifierSplash.png",
                            width=64,
                            height=64)
                  
animalMessage   = Text(animalClassifier, text = "Animal: ")
accuracyMessage = Text(animalClassifier, text = "Accuracy: ")

PushButton(animalClassifier, command=get_file, text="Upload Animal Image")

file_name = Text(animalClassifier)

animalClassifier.display()
