from machineClassifier import *

from guizero import App, Text, PushButton, Picture

def get_file():
    filePath = app.select_file()
    animal, accuracy = make_animal_prediction_to_user(filePath)
    animalMessage.value = animal
    accuracyMessage.value = accuracy
    picture.value = filePath

app = App()

picture = Picture(app, 
                  image= rootDir + "/data/ML/classifierSplash.png",
                  width=300,
                  height=300)
animalMessage = Text(app, text = "Animal: ")
accuracyMessage = Text(app, text = "Accuracy: ")
PushButton(app, command=get_file, text="Upload Animal Image")

file_name = Text(app)

app.display()
