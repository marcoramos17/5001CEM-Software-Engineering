from guizero import *
import database as dtbase

def window_close(tab_window):
    tab_window.hide()

def initialization():
    pass


# This function is responsible for updating the inbox GUI
def update_inbox():
    user_inbox = dtbase.db_get_inbox_users("ElizBrum829854")
    # list of buttons
    message_buttons = [chat_1, chat_2, chat_3, chat_4, chat_5]
    # app only displays 5 most recent messages
    size = 4 if len(user_inbox) > 5 else len(user_inbox)-1

    for i in range(len(user_inbox)):
        texting = str(user_inbox[size-i])[2:-3]
        message_buttons[i].text = texting
        message_buttons[i].visible = True 
    
    for button in message_buttons[size+1:]:
        button.visible = False

def update_messages():
    pass

def msg_send(msg_inp):
    print(msg_inp.value)
    msg_inp.value = ""

def enter_key_press(event):
    if event.key == "\r":
        msg_send()

# Private Message Window
def private_message(x):
    # list of buttons
    message_buttons = [chat_1, chat_2, chat_3, chat_4, chat_5]

    pm_wind = Window(app, title = message_buttons[x-1].text)

    # Basic GUI for messaging page
    back_button = PushButton(pm_wind, 
                        text = "Return",
                        command = window_close,
                        args = [pm_wind],
                        align = 'top',
                        width = 'fill',
                        height = 1)
    send_box = Box (pm_wind,
                    width = 'fill',
                    align = 'bottom')
    message_input = TextBox(send_box,
                            width = 'fill',
                            height = 'fill',
                            align = 'left')
    message_input.when_key_pressed = enter_key_press
    send_button = PushButton(send_box, 
                        text = "Send",
                        align = 'right',
                        width = 3,
                        height = 1,
                        command = msg_send,
                        args = [message_input])
    message_container = Box(pm_wind,
                            width = 'fill',
                            height = 'fill')

    # Messages
    message_1 = Text(pm_wind,
                    width = 'fill',
                    height = 2,
                    text = "message 1")
    message_2 = Text(pm_wind,
                    width = 'fill',
                    height = 2,
                    text = "message 2")    
    message_3 = Text(pm_wind,
                    width = 'fill',
                    height = 2,
                    text = "message 3")
    message_4 = Text(pm_wind,
                    width = 'fill',
                    height = 2,
                    text = "message 4")
    message_5 = Text(pm_wind,
                    width = 'fill',
                    height = 2,
                    text = "message 5")
    message_6 = Text(pm_wind,
                    width = 'fill',
                    height = 2,
                    text = "message 6")
    message_7 = Text(pm_wind,
                    width = 'fill',
                    height = 2,
                    text = "message 7")


    pm_wind.show()
    pass

app = App(title="Private Messages")


#message = Text(app, text="Welcome to the Hello world app!")
back_button = PushButton(app, 
                        text = "Return",
                        command = update_inbox,
                        align = 'top',
                        width = 'fill',
                        height = 1)


# Message buttons - display the latest 5 messages
inbox_container = Box(app, border = True, width = 'fill', height = 'fill')
chat_1 = PushButton(inbox_container,
                    text="first fella",
                    command=private_message,
                    args = [1],
                    width = 'fill',
                    height = 3,
                    visible = False)

chat_2 = PushButton(inbox_container,
                    text="first fella",
                    command=private_message,
                    args = [2],
                    width = 'fill',
                    height = 3,
                    visible = False)

chat_3 = PushButton(inbox_container,
                    text="first fella",
                    command=private_message,
                    args = [3],
                    width = 'fill',
                    height = 3,
                    visible = False)

chat_4 = PushButton(inbox_container,
                    text="first fella",
                    command=private_message,
                    args = [4],
                    width = 'fill',
                    height = 3,
                    visible = False)

chat_5 = PushButton(inbox_container,
                    text="first fella",
                    command=private_message,
                    args = [5],
                    width = 'fill',
                    height = 3,
                    visible = False)


## MESSAGE PAGE


app.display()