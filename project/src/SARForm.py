from guizero import App, Text, PushButton, ButtonGroup
import database as db
# GUIZero documentation linked below
# https://lawsie.github.io/guizero/about/
def SARForm(name):
    
    def confirmClicked():
        if choice.value == "No":
            SARFormGUI.destroy()
        if choice.value == "Yes":
            finalText.show()
            file = open("Your-Data.txt", "w") 
            for item in db.db_get_forum_replies_from_user(name):
                item = str(item)
                file.write("Forum Replies - ")
                file.write(item)
                file.write("\n")
            for item in db.db_get_forum_posts_from_user(name):
                item = str(item)
                file.write("Forum Posts - ")
                file.write(item)
                file.write("\n")
            for item in db.db_get_user_tickets(name):
                item = str(item)
                file.write("User Tickets - ")
                file.write(item)
                file.write("\n")
            for item in db.db_get_sar_messages(name):
                item = str(item)
                file.write("Messages - ")
                file.write(item)
                file.write("\n")
            for item in db.db_read_account_data(name):
                item = str(item)
                file.write("Account Data - ")
                file.write(item)
                file.write("\n")
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
# SARForm("JimmCric582874") # Test value 

