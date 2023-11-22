"""All account related code - documentation #07"""
import database as dtbase

class Account:
    """
    Class for general account processes
    """
<<<<<<< HEAD
    err = False
    def __init__(self, is_new, password, fst_name = "", lst_name = "",
                access_code = "", date_birth = "", role_id = "",
=======

    def __init__(self, is_new, password, fst_name = "", lst_name = "",
                access_code = "", date_birth = "", 
>>>>>>> origin/unittesting-oop
                location = "", username = "", email = ""):
        """
        Constructor for the Account objects
        """
<<<<<<< HEAD
        if role_id != "":
            self.role_id = role_id
        else:
            self.role_id = 1
=======
        self.role_id = 1
>>>>>>> origin/unittesting-oop

        if is_new:
            self.username = dtbase.generate_username(fst_name,lst_name, access_code)
            if not dtbase.db_check_username_exists(self.username):
                self.register(fst_name, lst_name, password,
                          access_code, date_birth, location, self.role_id)

            else:
                print("Temporary Err Message - Account already exists")
<<<<<<< HEAD
                self.err = True
=======
>>>>>>> origin/unittesting-oop
        else:
            if dtbase.db_check_username_exists(username):
                self.login(username, password)
            else:
                print("Temporary Err Message - Account doesn't exists")
<<<<<<< HEAD
                self.err = True
=======
>>>>>>> origin/unittesting-oop


    def register(self, fst_name, lst_name, password,
                access_code, date_birth, location, role_id, email = ""):
        """ user registration function """
        print("Regular account - registration -> ", fst_name, " ", lst_name)

        self.fst_name = fst_name
        self.lst_name = lst_name
        self.access_code = access_code
        self.date_birth = date_birth
        self.location = location
        self.role_id = role_id
        self.username = dtbase.db_create_account(fst_name, lst_name, password,
                                    access_code, date_birth, location, role_id)
        self.email = email

        del password

    def login(self, username, password):
        """ user login function """
        print("existing account - logging in")
        self.username = username
        #check login through Dylan's login function
        if dtbase.db_check_account_login(self.username, password):
            print(">> ",username," Logged In successful!!")
            user_details = dtbase.db_read_account_data(self.username)
            self.fst_name = user_details[1]
            self.lst_name = user_details[2]
            self.date_birth = user_details[3]
            self.location = user_details[4]
            ###self.schoolID = user_details[5]
            ###self.school = user_details[6]
            self.role_id = user_details[7]
            self.role = user_details[8]
            if user_details[9] == None:
                self.email = "No email"
            else:
                self.email = user_details[9]
            print(self.date_birth)
        else:
            print("The password is wrong")
<<<<<<< HEAD
            self.err = True
            raise Exception("Incorrect Password")
        del password

    def __bool__(self):
        if self.err:
            return False
        else:
            return True

=======
            raise Exception("Incorrect Password")
        del password

>>>>>>> origin/unittesting-oop

class CollectiveAccount(Account):
    """" Class for collective account processes
    (i.e. accounts that aren't managed by a single person) """
    def __init__(self, is_new, password, username = "",  access_code = "",
                fst_name = "", lst_name = "", date_birth = "", location = "",
<<<<<<< HEAD
                role_id = "",email = ""):
        self.access_code = "100000"
        self.role_id = "3"
=======
                email = ""):
        self.access_code = "100000"
        self.role_id = 3
>>>>>>> origin/unittesting-oop
        super().__init__(is_new,
                         password = password,
                         username = username,
                         fst_name = fst_name,
                         lst_name = lst_name,
                         access_code = self.access_code,
<<<<<<< HEAD
                         role_id = self.role_id,
=======
>>>>>>> origin/unittesting-oop
                         date_birth = date_birth,
                         location = location,
                         email=email)


class PersonalAccount(Account):
    """" Class for personal account processes
    (i.e. accounts that are managed by a single person) """
    def __init__(self, is_new, password, username = "", access_code = "",
<<<<<<< HEAD
                 role_id ="", fst_name = "", lst_name = "", date_birth = "",
                 location = "", email=""):
        self.role_id = "6"
=======
                fst_name = "", lst_name = "", date_birth = "", location = "",
                email=""):
        self.role_id = 6
>>>>>>> origin/unittesting-oop
        super().__init__(is_new,
                         password = password,
                         username = username,
                         fst_name = fst_name,
                         lst_name = lst_name,
                         date_birth = date_birth,
                         access_code = access_code,
<<<<<<< HEAD

                         role_id = self.role_id,
                         location = location,
                         email=email)
=======
                         location = location,
                         email=email)
        print(f"In Class Personal Usr: {username}")
        print(f"In Class Personal Pwd: {password}")
>>>>>>> origin/unittesting-oop


class ProfessorAccount(PersonalAccount):
    """" Class for professor account processes (include the ability
    to send quizzes and tasks to student accounts) """
    def __init__(self, is_new, password, username = "", access_code = "",
                fst_name = "", lst_name = "", date_birth = "", location = "",
                email=""):
<<<<<<< HEAD
        self.role_id = "2"
=======
        self.role_id = 2
>>>>>>> origin/unittesting-oop
        super().__init__(is_new,
                         password = password,
                         username = username,
                         fst_name = fst_name,
                         lst_name = lst_name,
                         access_code = access_code,
                         date_birth = date_birth,
<<<<<<< HEAD
                         role_id = self.role_id,
=======
>>>>>>> origin/unittesting-oop
                         location = location,
                         email=email)


class StudentAccount(PersonalAccount):
    """" Class for student account processes
    (include the ability to complete quizzes or minigames) """
    def __init__(self, is_new, password, username = "", access_code = "",
                fst_name = "", lst_name = "", date_birth = "", location = "",
                email=""):
<<<<<<< HEAD
        self.role_id = "1"
=======
>>>>>>> origin/unittesting-oop
        super().__init__(is_new,
                         password = password,
                         username = username,
                         fst_name = fst_name,
                         lst_name = lst_name,
                         access_code = access_code,
                         date_birth = date_birth,
<<<<<<< HEAD
                         role_id = self.role_id,
                         location = location,
                         email=email)
        
=======
                         location = location,
                         email=email)
        self.role_id = 1
        print(f"In Class St Usr: {username}")
        print(f"In Class St Pwd: {password}")
>>>>>>> origin/unittesting-oop



class GuestAccount(PersonalAccount):
    """" Class for guest account processes (i.e. accounts that aren't
    saved and don't require details, merely for browsing purposes) """
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        #self.access_code = "999999"
        self.role_id = 5
        super().__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Business account registration -> ", fst_name, " ", lst_name)

    # PECULIARITY OF THIS ACCOUNT: When logging off, uses it's own register/login function that
    # doesn't save any details to the database

class SchoolAccount(CollectiveAccount):
    """" Class for school management account processes (accounts that own student accounts,
    and represent the school entity)"""
    def __init__(self, is_new, password, username = "", access_code = "",
                fst_name = "", lst_name = "", date_birth = "", location = "",
                email=""):
        self.role_id = 4
        super().__init__(is_new,
                         password = password,
                         username = username,
                         fst_name = fst_name,
                         lst_name = lst_name,
                         access_code = access_code,
                         date_birth = date_birth,
                         location = location,
                         email=email)

class BusinessAccount(CollectiveAccount):
    """" Class for business account processes (accounts owned by businesses) """
    def __init__(self, is_new, password, username = "", access_code = "",
                fst_name = "", lst_name = "", date_birth = "", location = "",
                email=""):
        self.role_id = 3
        super().__init__(is_new,
                         password = password,
                         username = username,
                         fst_name = fst_name,
                         lst_name = lst_name,
                         access_code = access_code,
                         date_birth = date_birth,
                         location = location,
                         email=email)