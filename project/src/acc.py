import database as dtbase
class Account:
    """
    Class for general account processes
    """

    def __init__(self, is_new, password, username = "",
                fst_name = "", lst_name = "", access_code = "",
                date_birth = "", location = ""):
        """
        Constructor for the Account objects
        """
        self.username = username
        self.role_id = 0

        if is_new:
            self.register(fst_name, lst_name, password,
                          access_code, date_birth, location, self.role_id)

        else:
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
        self.username = dtbase.db_create_account(
            fst_name,
            lst_name,
            password,
            access_code,
            date_birth,
            location,
            role_id
        )
        del password
        print("USERNAME IS {}".format(self.username))

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

test = Account(True, 
               password = "password", 
               fst_name = "Paul", 
               lst_name = "Brumteach", 
               access_code = "829854", 
               date_birth = "1970-09-12", 
               location = "Birmingham")
