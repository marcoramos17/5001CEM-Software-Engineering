from guizero import App, Text, PushButton, TextBox
import database as db
def supportTicketsForm(name):
    def confirmClicked():
            finalText.show()
            databaseInput = userInput.value
            db.db_create_support_ticket(name, databaseInput)

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

def supportTicketAdminAccess(): # This function must be called manually by the admin technician
      for ticket in db.db_get_all_support_tickets():
            print(ticket)

def supportTicketAdminDelete(ticketID): # This function must be called manually by the admin technician
      db.db_close_ticket(ticketID)
      
