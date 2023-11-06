'''
--------------------------------------------------------------------------------
 - - - - - - - - - - - - - -UNLESS STATED OTHERWISE - - - - - - - - - - - - - - 
 - - - - - - - - - - - -DYLAN CALLAGHAN 13306573 5000CEM - - - - - - - - - - - -
--------------------------------------------------------------------------------
 - - - - - - - - - - - - - - - - - FILE NOTES - - - - - - - - - - - - - - - - - 
--------------------------------------------------------------------------------

This file defines functions and creates handles to the project's database in or-
der to be used as an API. This is a foundation for other files in the project, 
as it allows other developers to utilize the database without having to constru-
ct any SQL commands and run them themselves, although the option is available w-
ith the handles that are created upon importing this file.

Examples are at the bottom of the file, and only ran if called from main. To use
the examples, uncomment the relevant portions of code. Note that some examples
may fail due to uniqueness constraints in the database (if ran more than once) 
so to avoid this, either only read the examples for usage, or delete the releva-
nt rows from the database directly before running (perhaps in sqlitestudio or s-
imilar).

Tutorial on use of sqlite3 in python can be found at: 
  https://docs.python.org/3/library/sqlite3.html

If you contribute to this file, please add your name and id ABOVE the function
signature, as this will help to clearly show that it is yours. Alternatively ap-
end a comment at the end of any LINES that you added, if not a whole function b-
elongs to you.
Additionally, please try to use type hints and follow the style guide for this 
document.
    • Function parameters prepended with 'f_'
    • Internal variables do not have anything prepended
    • Soft character limit at 80 characters (can go over, be sensible)
    • Prefered to multiline function arguments and return types
    • Use sphinx docstring format, the details on how to use this can be found 
        at https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
        although I am using inlined types in the attributes descriptions
    • Explaination can be done with comments ABOVE the line or block of code
    • Preferable to align typehints and parameter names, see db_create_account()

--------------------------------------------------------------------------------
 - - - - - - - - - - - - - - - FUNCTIONS OVERVIEW - - - - - - - - - - - - - - - 
--------------------------------------------------------------------------------
db_sqlite3_init():
    Initialise the database, return a handle to database, and its cursor

db_add_school():
    Add a school to the database

db_get_schools():
    Get a list of schools

db_bind_school_teacher():
    Given a teacher, find their school and update the entry to the teacher

db_get_access_code_from_account():
    Given an account, get their access code

db_get_access_code_from_school():
    Given a school, get its access code

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
        0   First Name,             The user's first name
        1   Last Name,              The user's last name
        2   Date of Birth,          The user's date of birth 
        3   Location,               Real world location of the user
        4   School ID (INTEGER),    The school ID that is used in functions
        5   School (String),        The name of that school, for easy printing
        6   Role ID (INTEGER),      The role ID used in functions
        7   Role (String),          The name of the role, for easy printing
        
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
        0   Username of sender,
        1   Username of recipient,
        2   Body of message,
        3   Timestamp

--------------------------------------------------------------------------------
 - - - - - - - - - - - - - - - - CALLING ORDER - - - - - - - - - - - - - - - - -
--------------------------------------------------------------------------------
There are some caveats to think about when calling these functions so that we d-
on't run into undefined behaviour or exceptions. Whilst there is practically no
logical error checking in this API (since it is expected that others will imple-
ment this behaviour inbetween the GUI and this code) it is handy to note a few 
basic things.
    • We must make schools first to get an access code, then make an account us-
        ing that access code, then if they are a teacher, then bind them to the
        school at that point.
    • Create account also creates a user for that account that contains the per-
        sonal details for that instance. DON'T FORGET that User and Account are
        two different tables
'''
# For the database handles
import sqlite3

# For sleeping (used in the examples)
import time

# For OTPs (used in the examples)
from pyotp import random_base32, TOTP

# try:
#     # Try to import a more efficient implementation
#    import cPickle as pickle
# except:
#     # Else, fallback
#    import pickle

# The linting errors for the above were pissing me off, so here is alternative
import pickle

# For using our password generation
from password import *

# For absolute file location
import os.path

# To print debug strings
debug = True

def db_sqlite3_init(f_filename: str) -> tuple [sqlite3.Connection, 
                                               sqlite3.Cursor]:
    """
    Init for the database connections, this will connect to the database
    contained within the repository.

    :return tuple [sqlite3.Connection, sqlite3.Cursor]: two handles to the DB
    """ 
    # Get file path
    baseDir = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(baseDir, "../data/{}.db".format(f_filename))
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

The handles may be changed to a different database by doing the following:

    import database as db
    db.db, db.dbCursor = db.db_sqlite3_init(File)

Which will overwrite the handles used by the functions, although no one should 
need to do this apart from when running unit tests (in order to change to a tes-
ting database).
'''
db, dbCursor = db_sqlite3_init('db')

def db_add_school(f_name: str) -> None:
    """
    This function is used to add a school to the database.

    :param str f_name: Name of the school to be added
    """
    # We only need the name of the school to add it
    #   since the access code is generated automatically
    dbCursor.execute(
        "INSERT INTO Schools (name) VALUES "
        "(?)", 
        (f_name,)
    )
    db.commit()
    return

def db_get_schools() -> list[str]:
    """
    This function is used to get a list of the schools in the database

    :return list[str]: The list of schools
    """
    # Get a list of tuples
    schoolsTuples = dbCursor.execute(
        "SELECT name FROM Schools"
    ).fetchall()
    # Create our return list
    schoolsList = []
    # Extract names from tuples
    for school in schoolsTuples:
        schoolsList.append(school[0])
    return schoolsList

def db_bind_school_teacher(f_username: str) -> None:
    """
    This function is used to bind a teacher to a school

    :param str f_username: Name of the teacher to bind to their stored school
    """
    schoolID = dbCursor.execute(
        "SELECT Schools_group FROM Accounts WHERE Username = ?", 
        (f_username,)
    ).fetchone()[0]
    dbCursor.execute(
        "UPDATE Schools SET teacher = ? WHERE schoolID = ?", 
        (f_username, schoolID)
    )
    db.commit()
    return

def db_get_access_code_from_account(f_username: str) -> str:
    """
    This function is return the access code from a username.
    Whilst it seems this function may not make sense, it is resistant to any ch-
    anges that we might make to the username generation system.

    :param str f_username: The username to grab access code for
    :return str: The access code
    """
    accessCode = dbCursor.execute(
        "SELECT Schools.accessCode "
        "FROM Accounts "
        "INNER JOIN Schools ON Accounts.Schools_group = Schools.schoolID "
        "WHERE Accounts.username = ?",
        (f_username,) 
    ).fetchone()[0]
    return str(accessCode)

def db_get_access_code_from_school(f_school: str) -> str:
    """
    This function is used get the access code for a school

    :param str f_username: Name of the school to grab the access code for
    :return str: The access code
    """
    accessCode = dbCursor.execute(
        "SELECT accessCode "
        "FROM Schools "
        "WHERE name = ?",
        (f_school,) 
    ).fetchone()[0]
    return str(accessCode)

def db_get_teacher_from_username(f_username: str) -> str:
    '''
    This function returns the teacher assigned to a school, given any user from
    that specific school.

    :param str f_username: The username to check the teacher for
    :return str: 
    '''
    teacher = dbCursor.execute(
        "SELECT Schools.teacher FROM Accounts "
        "INNER JOIN Schools ON Schools.schoolID = Accounts.Schools_group "
        "WHERE Accounts.username = ?", 
        (f_username,)
    ).fetchone()[0]
    return teacher

def db_create_account(f_firstName:  str, 
                      f_lastName:   str, 
                      f_password:   str, 
                      f_acesssCode: str,
                      f_dob:        str,
                      f_location:   str,
                      f_role:       int) -> str:
    """
    This function is used to add an account to the database.

    :param str f_firstName: First name of the user
    :param str f_lastName: Last name of the user
    :param str password: Chosen password of the user (validation by GUI stage)
    :param str acesssCode: Access code (to link to school)
    :param str dob: Date of birth of the user
    :param str location: Location of the user
    :param int role: The role ID of the user
    :return str: The generated username from account creation
    """
    # Use statments on the cursor, remembering to use placeholders (?) to 
    #   prevent against SQL injection attacks
    dbCursor.execute(
        "INSERT INTO Users(firstName, lastName, dob, location) "
        "VALUES (?, ?, ?, ?)", 
        (f_firstName, f_lastName, f_dob, f_location)
    )

    # Fetch the access code
    schoolID = dbCursor.execute(
        "SELECT schoolID FROM Schools WHERE accessCode = ?", 
        (f_acesssCode,)
    ).fetchone()
    # If the access code is invalid (null return)
    if schoolID == None:
        raise Exception("Access code invalid.\n")
    # If not, then first entry of tuple is the f_schoolID
    schoolID = schoolID[0]
    
    # Username generation rule, is unique (enough in this prototype)
    try:
        username = f_firstName[:4] + f_lastName[:4] + f_acesssCode
    except:
        username =  f_firstName.ljust(4, 'x')[:4] + \
                    f_lastName.ljust(4, 'x')[:4] + \
                    f_acesssCode

    # Get our salt
    salt = generate_salt()
    # And our hashed, salted password
    password = hash_password(f_password, salt)

    # Then create our account
    dbCursor.execute(
        "INSERT INTO Accounts "
        "(salt, password, username, Roles_roleID, Users_userID, Schools_group) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (salt, password, username, f_role, dbCursor.lastrowid, schoolID)
    )
    
    # Commit writes
    db.commit()

    # Debug printing
    if debug:
        print("School ID is: {}\n".format(schoolID))
        print("Username is: {}\n".format(username))
        print("Salt is: {}\n".format(salt))

    return username

def db_update_user_secret(f_username: str, 
                          f_totp:     TOTP) -> None:
    '''
    This function updates a user's secret, this is a BLOB in the database which
    contains a serialized version of a `pyotp.TOTP` object.

    :param str f_username: The username to update the secret for
    :param TOTP f_totp: The TOTP class instance
    '''
    # Serialize the data into binary format
    blob = pickle.dumps(f_totp, pickle.HIGHEST_PROTOCOL)
    # Add to the table
    dbCursor.execute(
        "UPDATE Accounts "
        "SET secret = ? "
        "WHERE username = ?", (blob, f_username)
    )
    # Commit and write the changes
    db.commit()
    return

def db_get_user_secret(f_username: str) -> TOTP:
    '''
    This function gets the user's secret, and unpickles it to get an instance of
    the TOTP class.

    :param str f_username: The user to grab the secret for
    :return TOTP: The TOTP instance
    '''
    # Fetch the serialized data
    blob = dbCursor.execute(
        "SELECT secret "
        "FROM Accounts "
        "WHERE username = ?", (f_username,)
    ).fetchone()[0]
    # Unpickle and return
    return pickle.loads(blob)

def db_check_account_login(f_username: str,
                           f_password: str) -> bool:
    """
    This function is used to check that a password is correct for a given user.

    :param str f_username: Username to grab password for
    :param str f_password: Password to compare to stored hash
    :return bool: Result (True if password is correct, False otherwise)
    """
    # Get the hashed password, and the salt from the accounts list
    login = dbCursor.execute(
        "SELECT password, salt FROM Accounts WHERE username = ?", 
        (f_username,)
    ).fetchone()
    # If the hashed password is the same as the hash of the input password, then 
    #   the given password is correct. Here we can just return a bool
    return (login[0] == hash_password(f_password, login[1]))


def db_update_password(f_username:    str,
                       f_oldPassword: str,
                       f_newPassword: str) -> None:
    """
    This function is used to change a user's password, it performs a basic pass-
    word check first.

    :param str f_username: Username to change password for
    :param str f_oldPassword: Password to compare to stored hash
    :param str f_newPassword: Password to update to
    """
    # Simple check for incorrect credentials
    if not db_check_account_login(f_username, f_oldPassword):
        raise Exception("Old password incorrect\n")
    # Update with new password
    dbCursor.execute(
        "UPDATE Accounts "
        "SET password = ? "
        "WHERE username = ? ", (f_newPassword, f_username)
    )
    # Commit changes and write
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
    # Read account data into tuple
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
    dbCursor.execute(
        "INSERT INTO Messages ("
        "Accounts_senderID, "
        "accounts_recieverID, "
        "body) "
        "VALUES (?, ?, ?)", 
        (f_userFrom, f_userTo, f_body)
    )
    # Ensure that changes are committed to the DB
    db.commit()
    return
    
def db_get_inbox_users(f_username: str) -> list[tuple[str]]:
    '''
    This function is used to get the list of users in the DMs section for a giv-
    en user, this includes one way messsages from either side.

    :param str f_username: The user to get the list for
    :return list[tuple[str]]: A list of tuples of length 1, each contains a 
        message recipient, there is no particular sorting to this yet though
    '''
    # Read list of users
    inboxList = dbCursor.execute(
        "SELECT DISTINCT Accounts_senderID "
        "FROM Messages "
        "WHERE Accounts_recieverID = ? "
        "UNION "
        "SELECT DISTINCT Accounts_recieverID "
        "FROM Messages "
        "WHERE Accounts_senderID = ?", 
        (f_username, f_username)
    ).fetchall()
    return inboxList

def db_read_messages_between(f_userFrom: str, 
                             f_userTo:   str) -> list [tuple [str, 
                                                              str, 
                                                              str, 
                                                              str]]:
    # Get the list of messages as a list of tuples containing message data
    messages = dbCursor.execute(
        "SELECT Accounts_senderID, Accounts_recieverID, body, timestamp "
        "FROM Messages "
        "WHERE Accounts_senderID = ? OR "
            "(Accounts_recieverID = ? AND Accounts_senderID = ?)", 
        (f_userFrom, f_userFrom, f_userTo)
    ).fetchall()
    return messages


if __name__ == "__main__":
    '''
    Example usage of some of the above functions, some of these may fail depend-
    ing on the current state of the database. Remove offending rows to stop this
    from happening. Whilst this is not a complete guide on usage, it may help to
    understand what
    is going on in some of the functions.
    '''
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

        # 

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
        # db_bind_school_teacher('JameDudl829854')
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
        # print("Messages between {} and {}".format("TeacCovs582874", 
        #                                           "JimmCric582874")) 
        # messages = db_read_messages_between("TeacCovs582874", 
        #                                     "JimmCric582874")
        # for message in messages:
        #     print("FROM: {}\nTO:   {}\nBODY: {}\n".format(message[0], 
        #                                                   message[1], 
        #                                                   message[2]))

        # print("Messages between {} and {}".format("JameDudl829854", 
        #                                           "ElizBrum829854"))
                                                  
        # messages = db_read_messages_between("JameDudl829854", 
        #                                     "ElizBrum829854")
        # for message in messages:
        #     print(
        #         "FROM: {}\n"
        #         "TO:   {}\n"
        #         "BODY: {}\n"
        #         "AT:   {}\n"
        #         .format(message[0], message[1], message[2],message[3])
        #     )
    
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
        print('')
    except Exception as err:
        print("ERROR:\n", err)
    dbCursor.close()
