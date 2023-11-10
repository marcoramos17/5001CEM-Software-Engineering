from mlearnTrainer import *
from guizero import App, Text, PushButton, Picture


def get_file():
    filePath                = app.select_file()
    animal, accuracy        = make_animal_prediction_to_user(filePath)
    animalMessage.value     = animal
    accuracyMessage.value   = accuracy
    picture.value           = filePath
    postResizePicture.value = get_scaled_image(filePath)

app = App()

Text(app, text = "Uploaded Image")
picture = Picture(app, 
                  image= rootDir + "/data/ML/classifierSplash.png",
                  width=200,
                  height=200)

Text(app, text = "Post-Resized Image")
postResizePicture = Picture(app, 
                            image= rootDir + "/data/ML/classifierSplash.png",
                            width=64,
                            height=64)
                  
animalMessage   = Text(app, text = "Animal: ")
accuracyMessage = Text(app, text = "Accuracy: ")

PushButton(app, command=get_file, text="Upload Animal Image")

file_name = Text(app)

app.display()
