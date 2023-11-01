class Account:
    """
    Class for Accounts
    """

    def __init__(self, username, password, is_new,
                  role_id = 0, community = 0):
        """
        Constructor for the Account objects
        """
        self.username = username
        
        if is_new:
            self.register(role_id, community, password)            

        else:
            self.login(password)
            

    def register(self, role_id, community, password):
        """ user registration function """
        print("new account - registration")
        # self.user_id = <last user id in database> + 1
        # new entry in db; send -> username, pass, user_id, role_id, community
        self.role_id = role_id
        self.community = community
        del password

    def login(self, password):
        """ user login function """
        print("existing account - logging in")
        #self.user_id = <user's id in db>
        #self.role_id = <user's role id in db>
        #self.community = <user's community in db>
        del password

