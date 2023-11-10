from guizero import App, Text, PushButton, TextBox

def supportTicketsForm(name):
    def confirmClicked():
            finalText.show()
            databaseInput = userInput.value
            # Code for inputting the users support ticket input into the database - WORK NEEDED

    supportTicketsFormGUI = App(layout="grid")
    titleText = Text(supportTicketsFormGUI, text="Have you got an technical issue?", grid=[0,0], align="top")
    helloText = Text(supportTicketsFormGUI, text="Hello " + name, grid=[0,1], align="left")
    questionText = Text(supportTicketsFormGUI, text="Would you like to detail the issue(s) you are having?", grid=[0,2], align="left")
    userInput = TextBox(supportTicketsFormGUI, grid=[0,3], align="left", width=100)
    confirm = PushButton(supportTicketsFormGUI, text="Send?", grid=[0,4], align="left")
    confirm.when_clicked = confirmClicked
    finalText = Text(supportTicketsFormGUI, text="Your issue has been documented and a application technician will work on it shortly", grid=[0,6], align="left")
    finalText.hide()

    supportTicketsFormGUI.display()

def supportTicketAdminAccess(): # This function must be run manually by the admin technician
      # Code that prints out the support tickets for the technicians to access from the database - WORK NEEDED
      pass

supportTicketsForm("Jack")