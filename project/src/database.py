# API for using the database
# Tutorial on use of sqlite3 in python can be found at: 
#   https://docs.python.org/3/library/sqlite3.html
import sqlite3
import time

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

def db_add_school(f_name: str) -> bool:
    """
    This function is used to add a school to the database.

    :param str f_name: Name of the school to be added
    :return bool: Result
    """
    # We only need the name of the school to add it
    #   since the access code is generated automatically
    dbCursor.execute("INSERT INTO Schools (name) VALUES "
                     "(?)", (f_name,))
    db.commit()
    return True

def db_bind_school_teacher(f_username: str) -> bool:
    """
    This function is used to bind a teacher to a school

    :param str f_username: Name of the teacher to bind to their stored school
    :return bool: Result
    """
    schoolID = dbCursor.execute("SELECT Schools_group FROM Accounts WHERE Username = ?", 
                                (f_username,)).fetchone()[0]
    dbCursor.execute("UPDATE Schools SET teacher = ? WHERE schoolID = ?", 
                     (f_username, schoolID))
    db.commit()
    return True

def db_get_teacher_from_username(f_username: str) -> str:
    teacher = dbCursor.execute("SELECT Schools.teacher FROM Accounts "
                               "INNER JOIN Schools ON Schools.schoolID = Accounts.Schools_group "
                               "WHERE Accounts.username = ?", (f_username,)).fetchone()[0]
    return teacher

def db_create_account(f_firstName: str, 
                      f_lastName: str, 
                      f_password: str, 
                      f_acesssCode: str,
                      f_dob: str,
                      f_location: str,
                      f_role: int) -> bool:
    """
    This function is used to add an account to the database.

    :param str f_firstName: First name of the user
    :param str f_lastName: Last name of the user
    :param str password: Chosen password of the user (validation by GUI stage)
    :param str acesssCode: Access code (to link to school)
    :param str dob: Date of birth of the user
    :param str location: Location of the user
    :param int role: The role ID of the user
    :return bool: Result
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

    return True

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
    account = dbCursor.execute("SELECT Accounts.username, "
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
        "WHERE Accounts.username = ?", (f_username,)).fetchone()
    return account 

def db_print_account_data(f_username: str) -> None:
    """
    This function is used to read account data for a user, from the database.

    :param str f_username: Username to print account data for
    """
    loggedIn = db_read_account_data(f_username)
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
                    f_userTo: str,
                    f_body) -> bool:
    """
    This function is used to send a message between two users in the database.

    :param str f_userFrom: User that sends the message
    :param str f_userTo: User that recieves the message
    :param str f_body: Body of the message
    :return bool: Result
    """
    dbCursor.execute("INSERT INTO Messages ("
                        "Accounts_senderID, "
                        "accounts_recieverID, "
                        "body) "
                    "VALUES (?, ?, ?)", (f_userFrom, f_userTo, f_body))
    db.commit()
    return True
    

def db_read_messages_between(f_userFrom: str, f_userTo: str) -> tuple [str, str, str]:
    messages = dbCursor.execute("SELECT Accounts_senderID, Accounts_recieverID, body "
                     "FROM Messages "
                     "WHERE Accounts_senderID = ? OR "
                        "(Accounts_recieverID = ? AND Accounts_senderID = ?)", 
                        (f_userFrom, f_userFrom, f_userTo)).fetchall()
    return messages

if __name__ == "__main__":
    try:
        # Create an account examples
        # db_create_account('Jimmy', 'Cricket', 'ilovepeas', '582874', '2020-12-30', 'London', 1)
        # db_create_account('Teacher', 'Covson', 'coventryadmin', '582874', '2000-05-12', 'London', 2)

        # Check username/password combinations example
        # Correct password
        # print(db_check_account_login('JimmCric582874', 'ilovepeas'))
        # Incorrect password
        # print(db_check_account_login('JimmCric582874', 'ilovepeasWRONG'))

        # Add school example
        # db_add_school("London Modern")

        # Bind teacher to school example
        # db_bind_school_teacher("TeacCovs582874")
        # Read account data example
        # loggedIn = db_read_account_data("JimmCric582874")

        # Print account data example (debug)
        # db_print_account_data("JimmCric582874")
        # db_print_account_data("TeacCovs582874")

        # Get teacher from username example
        # print(db_get_teacher_from_username("JimmCric582874"))

        # Send message example
        # db_send_message("TeacCovs582874", "JimmCric582874", "Test message to s1")
        # time.sleep(1)
        # db_send_message("JimmCric582874", "TeacCovs582874", "Test message to t2")
        # time.sleep(1)
        # db_send_message("TeacCovs582874", "JimmCric582874", "Test message to s2")

        # Print messages between example
        messages = db_read_messages_between("TeacCovs582874", "JimmCric582874")
        for message in messages:
            print("FROM: {}\nTO:   {}\nBODY: {}\n\n".format(message[0], 
                                                            message[1], 
                                                            message[2]))
        None
    except Exception as err:
        print("ERROR:\n", err)
    dbCursor.close()
