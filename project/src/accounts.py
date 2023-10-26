class Account:
    """
    Class for Accounts
    """
    def __init__(self, acc_id, username):
        """
        Constructor for the Account objects
        """
        self.id = acc_id
        self.username = username
        print (self.username)
