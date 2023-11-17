from guizero import *

def change_message():
    message.value = "Not working you silly goose"

app = App(title="Hello world")
message = Text(app, text="Welcome to the Hello world app!")
button = PushButton(app, text="Home Page", command=change_message)

app.display()