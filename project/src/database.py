# For using the database
# Tutorial on use at https://docs.python.org/3/library/sqlite3.html
import sqlite3
# For using our password generation
from password import *
# For absolute file location
import os.path

debug = True

def sqlite3_init() -> tuple [sqlite3.Connection, sqlite3.Cursor]:
    # Get file path
    baseDir = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(baseDir, "db.db")
    # Create a connection to our database
    db = sqlite3.connect(dbPath)
    # Create a cursor to do commands
    return db, db.cursor()

db, dbCursor = sqlite3_init()

def create_student_account(f_firstName: str, 
                           f_lastName: str, 
                           f_password: str, 
                           f_acesssCode: str,
                           f_dob: str,
                           f_location: str) -> bool:
    # Use statments on the cursor, remembering to use placeholders (?) to 
    #   prevent against SQL injection attacks
    dbCursor.execute("INSERT INTO Users(firstName, lastName, dob, location) VALUES "
                     "(?, ?, ?, ?)", (f_firstName, f_lastName, f_dob, f_location))

    # Fetch the access code
    schoolID = dbCursor.execute("SELECT schoolID FROM Schools WHERE accessCode = ?", (f_acesssCode,)).fetchone()
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
    dbCursor.execute("INSERT INTO Accounts(salt, password, username, Roles_roleID, Users_userID, Schools_group) VALUES "
                     "(?, ?, ?, ?, ?, ?)", (salt, password, username, 1, dbCursor.lastrowid, schoolID))
    
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
    # Get the hashed password, and the salt from the accounts list, from the username
    login = dbCursor.execute("SELECT password, salt FROM Accounts WHERE username = ?", (f_username,)).fetchone()
    # If the hashed password is the same as the hash of the input password, then the 
    #   given password is correct. Here we can just return a bool
    return (login[0] == hash_password(f_password, login[1]))

if __name__ == "__main__":
    try:
        #create_student_account('Jimmy', 'Cricket', 'ilovepeas', '582874', '2020-12-30', 'London')
        print(check_account_login('JimmCric582874', 'ilovepeas'))
        print(check_account_login('JimmCric582874', 'ilovepeasWRONG'))
    except Exception as err:
        print("ERROR:\n", err)
    dbCursor.close()
