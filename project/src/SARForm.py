from guizero import App, Text, PushButton, ButtonGroup
# GUIZero documentation linked below
# https://lawsie.github.io/guizero/about/
def SARForm(name):
    
    def confirmClicked():
        if choice.value == "No":
            SARFormGUI.destroy()
        if choice.value == "Yes":
            finalText.show()
            file = open("Your-Data.txt", "w") # Select data from database and input into txt file - WORK NEEDED
            file.close()
            
    SARFormGUI = App(layout="grid")
    titleText = Text(SARFormGUI, text="Subject Access Request Form", grid=[0,0], align="top")
    helloText = Text(SARFormGUI, text="Hello " + name, grid=[0,2], align="left")
    questionText = Text(SARFormGUI, text="Would you like to request all information and data stored about yourself?", grid=[0,3], align="left")
    choice = ButtonGroup(SARFormGUI, options=["Yes", "No",], grid=[0,4], align="left")
    confirm = PushButton(SARFormGUI, text="Download data?", grid=[0,5], align="left")
    confirm.when_clicked = confirmClicked
    finalText = Text(SARFormGUI, text="Your data has been added to a text file and downloaded", grid=[0,6], align="left")
    finalText.hide()

    SARFormGUI.display()

SARForm("Jack")

