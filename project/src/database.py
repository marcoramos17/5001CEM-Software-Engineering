# API for using the database
# Tutorial on use of sqlite3 in python can be found at: 
#   https://docs.python.org/3/library/sqlite3.html

'''
--------------------------------------------------------------------------------
 - - - - - - - - - - - - - - - FUNCTIONS OVERVIEW - - - - - - - - - - - - - - - 
--------------------------------------------------------------------------------
db_sqlite3_init():
    Initialise the database, return a handle to database, and its cursor

db_add_school():
    Add a school to the database

db_bind_school_teacher():
    Given a teacher, find their school and update the entry to the teacher

db_get_teacher_from_username():
    Given a username, find the teacher for their school

db_create_account():
    Create an account for a user, this will make both a Users, and Account entry

db_update_user_secret():
    Given a user, update the secret attribute by serialising a TOTP instance

db_get_user_secret():
    Given a user, return an unserialised instance of a TOTP object 

db_check_account_login():
    Given a user, return a bool based on if their login credentials match

db_update_password():
    Given a user, their old password, and current, update the password in the db

db_read_account_data():
    Given a user, return a tuple of their account data in this order:
        (
            First Name,
            Last Name,
            Date of Birth,
            Location,
            School ID (INTEGER),
            School (String),
            Role ID (INTEGER),
            Role (String),
        )

db_print_account_data():
    Expansion on previous, mainly for demonstration purposes

db_send_message(): 
    Given two users and a message, add an entry in the database to represent a
    message sent between them, timestamps and read attribute are generated 
    automatically

db_get_inbox_users():
    Get a list of DM contacts, will be used in the DM functionality to display
    different message sections (corresponding to DMs between different users)

db_read_messages_between():
    Given two users, return a list of tuples, containing the messages between t-
    hem. Each tuple has the following format:
        (
            Username of sender,
            Username of recipient,
            Body of message,
            Timestamp
        )







--------------------------------------------------------------------------------
- 
--------------------------------------------------------------------------------
'''
# For the database handles
import sqlite3

# For sleeping (used in the examples)
import time

# For OTPs (used in the examples)
from pyotp import random_base32, TOTP
try:
    # Try to import a more efficient implementation
   import cPickle as pickle
except:
    # Else, fallback
   import pickle

# For using our password generation
from password import *

# For absolute file location
import os.path

# To print debug strings
debug = True

def db_sqlite3_init() -> tuple [sqlite3.Connection, sqlite3.Cursor]:
    """
    Init for the database connections, this will connect to the database
    contained within the repository.

    :return tuple [sqlite3.Connection, sqlite3.Cursor]: two handles to the DB
    """ 
    # Get file path
    baseDir = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(baseDir, "../data/db.db")
    # Create a connection to our database
    db = sqlite3.connect(dbPath)
    # Create a cursor to do commands
    return db, db.cursor()

'''
The following variables are available for use upon importing this file. Although
    it is not suggested to use them at all. Hopefully the functions in this file
    should be enough to perform all the tasks that we need - if not, then more
    functions can be added to the file.

    The reason for this is that interactions with these functions have had tests
    performed, untested use of the database handle and cursor may result in some
    errors or even break the database completely.
'''
db, dbCursor = db_sqlite3_init()

def db_add_school(f_name: str) -> None:
    """
    This function is used to add a school to the database.

    :param str f_name: Name of the school to be added
    """
    # We only need the name of the school to add it
    #   since the access code is generated automatically
    dbCursor.execute("INSERT INTO Schools (name) VALUES "
                     "(?)", (f_name,))
    db.commit()
    return

def db_bind_school_teacher(f_username: str) -> None:
    """
    This function is used to bind a teacher to a school

    :param str f_username: Name of the teacher to bind to their stored school
    """
    schoolID = dbCursor.execute("SELECT Schools_group FROM Accounts WHERE Username = ?", 
                                (f_username,)).fetchone()[0]
    dbCursor.execute("UPDATE Schools SET teacher = ? WHERE schoolID = ?", 
                     (f_username, schoolID))
    db.commit()
    return

def db_get_teacher_from_username(f_username: str) -> str:
    '''
    This function returns the teacher assigned to a school, given any user from
        that specific school.

    :param str f_username: The username to check the teacher for
    :return str: 
    '''
    teacher = dbCursor.execute("SELECT Schools.teacher FROM Accounts "
                               "INNER JOIN Schools ON Schools.schoolID = Accounts.Schools_group "
                               "WHERE Accounts.username = ?", (f_username,)).fetchone()[0]
    return teacher

def db_create_account(f_firstName:  str, 
                      f_lastName:   str, 
                      f_password:   str, 
                      f_acesssCode: str,
                      f_dob:        str,
                      f_location:   str,
                      f_role:       int) -> None:
    """
    This function is used to add an account to the database.

    :param str f_firstName: First name of the user
    :param str f_lastName: Last name of the user
    :param str password: Chosen password of the user (validation by GUI stage)
    :param str acesssCode: Access code (to link to school)
    :param str dob: Date of birth of the user
    :param str location: Location of the user
    :param int role: The role ID of the user
    """
    # Use statments on the cursor, remembering to use placeholders (?) to 
    #   prevent against SQL injection attacks
    dbCursor.execute("INSERT INTO Users(firstName, lastName, dob, location) "
                     "VALUES (?, ?, ?, ?)", 
                     (f_firstName, f_lastName, f_dob, f_location))

    # Fetch the access code
    schoolID = dbCursor.execute("SELECT schoolID FROM Schools WHERE accessCode = ?", 
                                (f_acesssCode,)).fetchone()
    # If the access code is invalid (null return)
    if schoolID == None:
        raise Exception("Access code invalid.\n")
    # If not, then first entry of tuple is the f_schoolID
    schoolID = schoolID[0]
    
    # Username generation rule, is unique (enough in this prototype)
    username = f_firstName[:4] + f_lastName[:4] + f_acesssCode

    # Get our salt
    salt = generate_salt()
    # And our hashed, salted password
    password = hash_password(f_password, salt)

    # Then create our account
    dbCursor.execute("INSERT INTO Accounts "
                     "(salt, password, username, Roles_roleID, Users_userID, Schools_group) VALUES "
                     "(?, ?, ?, ?, ?, ?)", (salt, password, username, f_role, dbCursor.lastrowid, schoolID))
    
    # Commit writes
    db.commit()

    # Debug printing
    if debug:
        print("School ID is: {}\n".format(schoolID))
        print("Username is: {}\n".format(username))
        print("Salt is: {}\n".format(salt))

    return

def db_update_user_secret(f_username: str, 
                          f_totp:     TOTP):
    blob = pickle.dumps(f_totp, pickle.HIGHEST_PROTOCOL)
    dbCursor.execute(
        "UPDATE Accounts "
        "SET secret = ? "
        "WHERE username = ?", (blob, f_username))
    db.commit()
    return

def db_get_user_secret(f_username: str) -> TOTP:
    blob = dbCursor.execute(
        "SELECT secret "
        "FROM Accounts "
        "WHERE username = ?", (f_username,)
    ).fetchone()[0]
    return pickle.loads(blob)

def db_check_account_login(f_username: str,
                           f_password: str) -> bool:
    """
    This function is used to check that a password is correct for a given user.

    :param str f_username: Username to grab password for
    :param str f_password: Password to compare to stored hash
    :return bool: Result (True if password is correct, False otherwise)
    """
    # Get the hashed password, and the salt from the accounts list, from the username
    login = dbCursor.execute("SELECT password, salt FROM Accounts WHERE username = ?", 
                             (f_username,)).fetchone()
    # If the hashed password is the same as the hash of the input password, then the 
    #   given password is correct. Here we can just return a bool
    return (login[0] == hash_password(f_password, login[1]))


def db_update_password(f_username:    str,
                       f_oldPassword: str,
                       f_newPassword: str) -> None:
    """
    This function is used to change a user's password, it performs a basic password
    check first.

    :param str f_username: Username to change password for
    :param str f_oldPassword: Password to compare to stored hash
    :param str f_newPassword: Password to update to
    """
    if not db_check_account_login(f_username, f_oldPassword):
        raise Exception("Old password incorrect\n")
    dbCursor.execute(
        "UPDATE Accounts "
        "SET password = ? "
        "WHERE username = ? ", (f_newPassword, f_username)
    )
    db.commit()
    return



def db_read_account_data(f_username: str) -> tuple [str, 
                                                    str, 
                                                    str, 
                                                    str, 
                                                    str, 
                                                    str, 
                                                    str, 
                                                    str, 
                                                    str]:
    """
    This function is used to read account data for a user, from the database.
    The

    :param str f_username: Username to read user data for
    :return tuple: Return a tuple containing multiple attributes
    """
    account = dbCursor.execute(
        "SELECT Accounts.username, "
            "Users.firstName, "
            "Users.lastName, "
            "Users.dob, "
            "Users.location, "
            "Accounts.Schools_group, "
            "Schools.name, "
            "Accounts.Roles_roleID, "
            "Roles.description "
        "FROM Users "
        "INNER JOIN Accounts ON Accounts.Users_userID = Users.userID "
        "INNER JOIN Schools ON Accounts.Schools_group = Schools.schoolID "
        "INNER JOIN Roles ON Accounts.Roles_roleID = Roles.roleID "
        "WHERE Accounts.username = ?", (f_username,)
    ).fetchone()
    return account 

def db_print_account_data(f_username: str) -> None:
    """
    This function is used to read account data for a user, from the database.

    :param str f_username: Username to print account data for
    """
    # Read account data tuple
    loggedIn = db_read_account_data(f_username)
    # Print string, format with tuple indexes (like list)
    print("Username: {}\n"
        "First Name: {}\n"
        "Last Name: {}\n"
        "Date of Birth: {}\n"
        "Location: {}\n"
        "School ID: {}\n"
        "School Name: {}\n"
        "Role ID: {}\n"
        "Role Name: {}\n".format(loggedIn[0],
                                    loggedIn[1],
                                    loggedIn[2],
                                    loggedIn[3],
                                    loggedIn[4],
                                    loggedIn[5],
                                    loggedIn[6],
                                    loggedIn[7],
                                    loggedIn[8]))

def db_send_message(f_userFrom: str,
                    f_userTo:   str,
                    f_body) -> None:
    """
    This function is used to send a message between two users in the database.

    :param str f_userFrom: User that sends the message
    :param str f_userTo: User that recieves the message
    :param str f_body: Body of the message
    """
    # Insert data into table
    dbCursor.execute("INSERT INTO Messages ("
                        "Accounts_senderID, "
                        "accounts_recieverID, "
                        "body) "
                    "VALUES (?, ?, ?)", (f_userFrom, f_userTo, f_body))
    # Ensure that changes are committed to the DB
    db.commit()
    return
    
def db_get_inbox_users(f_username: str) -> list[tuple[str]]:
    '''
    This function is used to get the list of users in the DMs section for a given
    user, this includes one way messsages from either side.

    :param str f_username: The user to get the list for
    :return list[tuple[str]]: A list of tuples of length 1, each contains a 
        message recipient, there is no particular sorting to this yet though
    '''
    inboxList = dbCursor.execute(
        "SELECT DISTINCT Accounts_senderID "
        "FROM Messages "
        "WHERE Accounts_recieverID = ? "
        "UNION "
        "SELECT DISTINCT Accounts_recieverID "
        "FROM Messages "
        "WHERE Accounts_senderID = ?", (f_username, f_username)).fetchall()
    return inboxList

def db_read_messages_between(f_userFrom: str, 
                             f_userTo:   str) -> list [tuple [str, str, str, str]]:
    messages = dbCursor.execute(
        "SELECT Accounts_senderID, Accounts_recieverID, body, timestamp "
        "FROM Messages "
        "WHERE Accounts_senderID = ? OR "
            "(Accounts_recieverID = ? AND Accounts_senderID = ?)", 
        (f_userFrom, f_userFrom, f_userTo)).fetchall()
    return messages


if __name__ == "__main__":
    try:
        # ----------------------------------------------------------------------
        # Create an account examples
        # ----------------------------------------------------------------------
        # db_create_account('Jimmy', 
        #                   'Cricket', 
        #                   'ilovepeas', 
        #                   '582874', 
        #                   '2020-12-30', 
        #                   'London', 
        #                   1)
        # db_create_account('Teacher', 
        #                    'Covson', 
        #                    'coventryadmin', 
        #                    '582874', 
        #                    '2000-05-12', 
        #                    'London', 
        #                    2)
        # db_create_account('Elizabeth',
        #                     'Brummie',
        #                     'iLoveBirmingham!',
        #                     '829854',
        #                     '2000-11-23',
        #                     'Birmingham',
        #                     1)
        # db_create_account('James',
        #                     'Dudley',
        #                     'teachingKidz',
        #                     '829854',
        #                     '1978-02-27',
        #                     'Birmingham',
        #                     2)
        # db_bind_school_teacher('JameDudl829854')

        # ----------------------------------------------------------------------
        # Check username/password combinations example
        # ----------------------------------------------------------------------
        # Correct password
        # print(db_check_account_login('JimmCric582874', 'ilovepeas'))
        # Incorrect password
        # print(db_check_account_login('JimmCric582874', 'ilovepeasWRONG'))

        # ----------------------------------------------------------------------
        # Add school example
        # ----------------------------------------------------------------------
        # db_add_school("London Modern")

        # ----------------------------------------------------------------------
        # Bind teacher to school example
        # ----------------------------------------------------------------------
        # db_bind_school_teacher("TeacCovs582874")
        # Read account data example
        # loggedIn = db_read_account_data("JimmCric582874")

        # ----------------------------------------------------------------------
        # Print account data example (debug)
        # ----------------------------------------------------------------------
        # db_print_account_data("JimmCric582874")
        # db_print_account_data("TeacCovs582874")

        # ----------------------------------------------------------------------
        # Get teacher from username example
        # ----------------------------------------------------------------------
        # print(db_get_teacher_from_username("JimmCric582874"))

        # ----------------------------------------------------------------------
        # Send message example
        # ----------------------------------------------------------------------
        # db_send_message("TeacCovs582874", 
        #                 "JimmCric582874", 
        #                 "Test message to s1")
        # time.sleep(1)
        # db_send_message("JimmCric582874", 
        #                 "TeacCovs582874", 
        #                 "Test message to t2")
        # time.sleep(1)
        # db_send_message("TeacCovs582874", 
        #                 "JimmCric582874", 
        #                 "Test message to s2")
        # db_send_message("JameDudl829854", 
        #                 "ElizBrum829854", 
        #                 "Hey student, bham?")
        # time.sleep(1)
        # db_send_message("ElizBrum829854", 
        #                 "JameDudl829854", 
        #                 "Yes teach, brummie")
        # time.sleep(1)
        # db_send_message("JameDudl829854", 
        #                 "ElizBrum829854", 
        #                 "No way stu, das crazy")
        # time.sleep(1)
        # db_send_message("TeacCovs582874", 
        #                 "ElizBrum829854", 
        #                 "hey student from another school!")

        # ----------------------------------------------------------------------
        # Print messages between example
        # ----------------------------------------------------------------------
        # print("Messages between {} and {}".format("TeacCovs582874", "JimmCric582874"))
        # messages = db_read_messages_between("TeacCovs582874", "JimmCric582874")
        # for message in messages:
        #     print("FROM: {}\nTO:   {}\nBODY: {}\n".format(message[0], 
        #                                                   message[1], 
        #                                                   message[2]))

        # print("Messages between {} and {}".format("JameDudl829854", "ElizBrum829854"))
        # messages = db_read_messages_between("JameDudl829854", "ElizBrum829854")
        # for message in messages:
        #     print("FROM: {}\nTO:   {}\nBODY: {}\nAT:   {}\n".format(message[0], 
        #                                                             message[1], 
        #                                                             message[2],
        #                                                             message[3]))
    
        # ----------------------------------------------------------------------
        # Show inbox users example
        # ----------------------------------------------------------------------
        # inbox = db_get_inbox_users("TeacCovs582874")
        # print("TeacCovs582874's Inbox:")
        # for username in inbox:
        #     print("- " + username[0])
        # print('')
        # inbox = db_get_inbox_users("JimmCric582874")
        # print("JimmCric582874's Inbox:")
        # for username in inbox:
        #     print("- " + username[0])
        # print('')
        
        # ----------------------------------------------------------------------
        # Update and read TOTP example
        # ----------------------------------------------------------------------
        # randomRNG = random_base32()
        # pyotpTotp = TOTP(randomRNG)

        # db_update_user_secret('JimmCric582874', pyotpTotp)
        # newTotp = db_get_user_secret('JimmCric582874')
        # if newTotp.secret == pyotpTotp.secret:
        #     print("The stored and calculated TOTP secrets are equal")

        # ----------------------------------------------------------------------
        # 
        # ----------------------------------------------------------------------

        None
    except Exception as err:
        print("ERROR:\n", err)
    dbCursor.close()
