"""All account related code - documentation #07"""
import database as dtbase

class Account:
    """
    Class for general account processes
    """

    def __init__(self, is_new, password, fst_name = "", lst_name = "",
                access_code = "", date_birth = "", location = "", username = ""):
        """
        Constructor for the Account objects
        """
        self.role_id = 0

        if is_new:
            self.username = dtbase.generate_username(fst_name,lst_name, access_code)
            if not dtbase.db_check_username_exists(self.username):
                self.register(fst_name, lst_name, password,
                          access_code, date_birth, location, self.role_id)

            else:
                print("Temporary Err Message - Account already exists")
        else:
            print(">> LOGGING IN")
            self.login(username, password)


    def register(self, fst_name, lst_name, password,
                access_code, date_birth, location, role_id ):
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
        
        del password

    def login(self, username, password):
        """ user login function """
        print("existing account - logging in")
        self.username = username
        #check login through Dylan's login function
        # if true obtain details from Dylan's user details account

        #self.fName = <user's first name in db>
        #self.lName = <user's last name in db>
        #self.dateBirth = <user's date of birth in db>
        #self.location = <user's location in db>
        #self.schoolID = <user's school's ID in db>
        #self.school = <user's school in db>
        #self.role_id = <user's role id in db>
        #self.role = <user's role in db>

        del password


class CollectiveAccount(Account):
    """" Class for collective account processes
    (i.e. accounts that aren't managed by a single person) """
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        self.access_code = "999999"
        self.role_id = 0
        super().__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Business account registration -> ", fst_name, " ", lst_name)

class PersonalAccount(Account):
    """" Class for personal account processes
    (i.e. accounts that are managed by a single person) """
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        self.access_code = "000000"
        self.role_id = 6
        super().__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Personal account registration -> ", fst_name, " ", lst_name)


class ProfessorAccount(PersonalAccount):
    """" Class for professor account processes (include the ability
    to send quizzes and tasks to student accounts) """
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        self.access_code = "999999"
        self.role_id = 0
        super(Account).__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Business account registration -> ", fst_name, " ", lst_name)


class StudentAccount(PersonalAccount):
    """" Class for student account processes
    (include the ability to complete quizzes or minigames) """
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        self.access_code = "999999"
        self.role_id = 0
        super(Account).__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Business account registration -> ", fst_name, " ", lst_name)


class GuestAccount(PersonalAccount):
    """" Class for guest account processes (i.e. accounts that aren't
    saved and don't require details, merely for browsing purposes) """
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        self.access_code = "999999"
        self.role_id = 0
        super(Account).__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Business account registration -> ", fst_name, " ", lst_name)

    # PECULIARITY OF THIS ACCOUNT: When logging off, uses it's own register/login function that
    # doesn't save any details to the database

class SchoolAccount(CollectiveAccount):
    """" Class for school management account processes (accounts that own student accounts,
    and represent the school entity)"""
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        self.access_code = "999999"
        self.role_id = 0
        super(Account).__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Business account registration -> ", fst_name, " ", lst_name)

class BusinessAccount(CollectiveAccount):
    """" Class for business account processes (accounts owned by businesses) """
    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", date_birth = "", location = ""):
        self.access_code = "999999"
        self.role_id = 0
        super(Account).__init__(is_new, password, username, fst_name, lst_name,
                        self.access_code, date_birth, location)

    def register(self, fst_name, lst_name, password, access_code, date_birth, location, role_id):
        print("Business account registration -> ", fst_name, " ", lst_name)
