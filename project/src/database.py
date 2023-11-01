# API for using the database
# Tutorial on use of sqlite3 in python can be found at: 
#   https://docs.python.org/3/library/sqlite3.html
import sqlite3

# For using our password generation
from password import *

# For absolute file location
import os.path

# To print debug strings
debug = True

def sqlite3_init() -> tuple [sqlite3.Connection, sqlite3.Cursor]:
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

db, dbCursor = sqlite3_init()

def add_school(f_name: str) -> bool:
    """
    This function is used to add a school to the database

    :param str f_name: Name of the school to be added
    :return bool: Result
    """
    # We only need the name of the school to add it
    #   since the access code is generated automatically
    dbCursor.execute("INSERT INTO Schools (name) VALUES "
                     "(?)", (f_name,))
    db.commit()
    return True

def create_account(f_firstName: str, 
                           f_lastName: str, 
                           f_password: str, 
                           f_acesssCode: str,
                           f_dob: str,
                           f_location: str,
                           f_role: int) -> bool:
    """
    This function is used to add an account to the database

    :param str f_firstName: First name of the user
    :param str f_lastName: Last name of the user
    :param str password: Chosen password of the user (validation by GUI stage)
    :param str acesssCode: Access code (to link to school)
    :param str dob: Date of birth of the user
    :param str location: Location of the user
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

def check_account_login(f_username: str,
                        f_password: str) -> bool:
    """
    This function is used to check that a password is correct for a given user

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

def read_account_data(f_username: str) -> tuple [str, str, str, str, str, str, str, str, str]:
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

def print_account_data(f_username: str) -> None:
    loggedIn = read_account_data(f_username)
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


# SELECT Schools_group FROM Accounts WHERE Username = 'TeacCovs582874';
# UPDATE Schools SET teacher = 'TeacCovs582874' WHERE schoolID = 3
def bind_school_teacher(f_username: str) -> bool:
    """
    This function is used to bind a teacher to a school

    :param str f_username: Name of the teacher to bind to their stored school
    :return bool: Result
    """
    schoolID = dbCursor.execute("SELECT Schools_group FROM Accounts WHERE Username = ?", 
                                (f_username,)).fetchone()[0]
    dbCursor.execute("UPDATE Schools SET teacher = ? WHERE schoolID = ?", 
                     (f_username, schoolID))
    # db.commit()
    return True

if __name__ == "__main__":
    try:
        # Create an account example
        # create_account('Jimmy', 'Cricket', 'ilovepeas', '582874', '2020-12-30', 'London', 1)
        # create_account('Teacher', 'Covson', 'coventryadmin', '582874', '2000-05-12', 'London', 2)

        # Check username/password combinations example
        # Correct password
        # print(check_account_login('JimmCric582874', 'ilovepeas'))
        # Incorrect password
        #print(check_account_login('JimmCric582874', 'ilovepeasWRONG'))

        # Add school example
        # add_school("London Modern")

        # Bind teacher to school example
        
        # Read account data example
        # loggedIn = read_account_data("JimmCric582874")

        # Print account data example (debug)
        print_account_data("JimmCric582874")
        print_account_data("TeacCovs582874")


        None
    except Exception as err:
        print("ERROR:\n", err)
    dbCursor.close()
