import unittest
import accounts as acc
import database as dbase

class TestAccounts(unittest.TestCase):
    password = "testpass123"
    f_name = "Test"
    l_name = "User"
    code = "829854"
    d_birth = "2000-12-31"
    loc = "Coventry"
    usrnm = ""
    def test_account(self):
        ## Account class registration
        reg_user = acc.Account(True,
                                password=self.password,
                                fst_name=self.f_name,
                                lst_name=self.l_name,
                                access_code=self.code,
                                date_birth=self.d_birth,
                                location=self.loc )
        
        
        ## Account class login
        self.usrnm = dbase.generate_username(self.f_name, self.l_name, self.code)
        log_user = acc.Account(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account creation/login worked
        self.assertTrue(reg_user)
        self.assertTrue(log_user)
        # Test the account registration and login share the same values 
        # (i.e. they're the same account)
        self.assertEqual(reg_user.username, log_user.username)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.lst_name, log_user.lst_name)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.date_birth, log_user.date_birth)
        self.assertEqual(reg_user.location, log_user.location)
        self.assertEqual(reg_user.role_id, log_user.role_id)

        # Deleting Test Account from database
        dbase.dbCursor.execute(
            "DELETE FROM Users "
            "WHERE firstName = ? AND lastName = ? ;",
            (self.f_name, self.l_name)
        )
        dbase.dbCursor.execute(
            "DELETE FROM Accounts "
            "WHERE username = ? ;",
            (self.usrnm,)
        )
        dbase.db.commit()

        ## Confirm Account Deletion
        confirm_user = acc.Account(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account login doesn't work for deleted account
        self.assertFalse(confirm_user)
    
    def test_collective_account(self):
        ## Account class registration
        reg_user = acc.CollectiveAccount(True,
                                password=self.password,
                                fst_name=self.f_name,
                                lst_name=self.l_name,
                                date_birth=self.d_birth,
                                location=self.loc )
        
        
        ## Account class login
        self.usrnm = dbase.generate_username(self.f_name, self.l_name, self.code)
        log_user = acc.CollectiveAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account creation/login worked
        self.assertTrue(reg_user)
        self.assertTrue(log_user)
        # Test the account registration and login share the same values 
        # (i.e. they're the same account)
        self.assertEqual(reg_user.username, log_user.username)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.lst_name, log_user.lst_name)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.date_birth, log_user.date_birth)
        self.assertEqual(reg_user.location, log_user.location)
        self.assertEqual(reg_user.role_id, log_user.role_id)
        self.assertEqual(reg_user.role_id, "3")
        self.assertEqual(reg_user.access_code, "100000")

        # Deleting Test Account from database
        dbase.dbCursor.execute(
            "DELETE FROM Users "
            "WHERE firstName = ? AND lastName = ? ;",
            (self.f_name, self.l_name)
        )
        dbase.dbCursor.execute(
            "DELETE FROM Accounts "
            "WHERE username = ? ;",
            (self.usrnm,)
        )
        dbase.db.commit()

        ## Confirm Account Deletion
        confirm_user = acc.CollectiveAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account login doesn't work for deleted account
        self.assertFalse(confirm_user)

    def test_personal_account(self):
        ## Account class registration
        reg_user = acc.PersonalAccount(True,
                                password=self.password,
                                fst_name=self.f_name,
                                lst_name=self.l_name,
                                access_code=self.code,
                                date_birth=self.d_birth,
                                location=self.loc )
        
        
        ## Account class login
        self.usrnm = dbase.generate_username(self.f_name, self.l_name, self.code)
        log_user = acc.PersonalAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account creation/login worked
        self.assertTrue(reg_user)
        self.assertTrue(log_user)
        # Test the account registration and login share the same values 
        # (i.e. they're the same account)
        self.assertEqual(reg_user.username, log_user.username)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.lst_name, log_user.lst_name)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.date_birth, log_user.date_birth)
        self.assertEqual(reg_user.location, log_user.location)
        self.assertEqual(reg_user.role_id, log_user.role_id)
        self.assertEqual(reg_user.role_id, "6")

        # Deleting Test Account from database
        dbase.dbCursor.execute(
            "DELETE FROM Users "
            "WHERE firstName = ? AND lastName = ? ;",
            (self.f_name, self.l_name)
        )
        dbase.dbCursor.execute(
            "DELETE FROM Accounts "
            "WHERE username = ? ;",
            (self.usrnm,)
        )
        dbase.db.commit()

        ## Confirm Account Deletion
        confirm_user = acc.PersonalAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account login doesn't work for deleted account
        self.assertFalse(confirm_user)
    
    def test_professor_account(self):
        ## Account class registration
        reg_user = acc.ProfessorAccount(True,
                                password=self.password,
                                fst_name=self.f_name,
                                lst_name=self.l_name,
                                access_code=self.code,
                                date_birth=self.d_birth,
                                location=self.loc )
        
        
        ## Account class login
        self.usrnm = dbase.generate_username(self.f_name, self.l_name, self.code)
        log_user = acc.ProfessorAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account creation/login worked
        self.assertTrue(reg_user)
        self.assertTrue(log_user)
        # Test the account registration and login share the same values 
        # (i.e. they're the same account)
        self.assertEqual(reg_user.username, log_user.username)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.lst_name, log_user.lst_name)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.date_birth, log_user.date_birth)
        self.assertEqual(reg_user.location, log_user.location)
        self.assertEqual(reg_user.role_id, log_user.role_id)
        self.assertEqual(reg_user.role_id, "2")

        # Deleting Test Account from database
        dbase.dbCursor.execute(
            "DELETE FROM Users "
            "WHERE firstName = ? AND lastName = ? ;",
            (self.f_name, self.l_name)
        )
        dbase.dbCursor.execute(
            "DELETE FROM Accounts "
            "WHERE username = ? ;",
            (self.usrnm,)
        )
        dbase.db.commit()

        ## Confirm Account Deletion
        confirm_user = acc.ProfessorAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account login doesn't work for deleted account
        self.assertFalse(confirm_user)
    
    def test_student_account(self):
        ## Account class registration
        reg_user = acc.StudentAccount(True,
                                password=self.password,
                                fst_name=self.f_name,
                                lst_name=self.l_name,
                                access_code=self.code,
                                date_birth=self.d_birth,
                                location=self.loc )
        
        
        ## Account class login
        self.usrnm = dbase.generate_username(self.f_name, self.l_name, self.code)
        log_user = acc.StudentAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account creation/login worked
        self.assertTrue(reg_user)
        self.assertTrue(log_user)
        # Test the account registration and login share the same values 
        # (i.e. they're the same account)
        self.assertEqual(reg_user.username, log_user.username)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.lst_name, log_user.lst_name)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.date_birth, log_user.date_birth)
        self.assertEqual(reg_user.location, log_user.location)
        self.assertEqual(reg_user.role_id, log_user.role_id)
        self.assertEqual(reg_user.role_id, "1")

        # Deleting Test Account from database
        dbase.dbCursor.execute(
            "DELETE FROM Users "
            "WHERE firstName = ? AND lastName = ? ;",
            (self.f_name, self.l_name)
        )
        dbase.dbCursor.execute(
            "DELETE FROM Accounts "
            "WHERE username = ? ;",
            (self.usrnm,)
        )
        dbase.db.commit()

        ## Confirm Account Deletion
        confirm_user = acc.StudentAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account login doesn't work for deleted account
        self.assertFalse(confirm_user)

    def test_school_account(self):
        ## Account class registration
        reg_user = acc.SchoolAccount(True,
                                password=self.password,
                                fst_name=self.f_name,
                                lst_name=self.l_name,
                                access_code=self.code,
                                date_birth=self.d_birth,
                                location=self.loc )
        
        
        ## Account class login
        self.usrnm = dbase.generate_username(self.f_name, self.l_name, self.code)
        log_user = acc.SchoolAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account creation/login worked
        self.assertTrue(reg_user)
        self.assertTrue(log_user)
        # Test the account registration and login share the same values 
        # (i.e. they're the same account)
        self.assertEqual(reg_user.username, log_user.username)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.lst_name, log_user.lst_name)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.date_birth, log_user.date_birth)
        self.assertEqual(reg_user.location, log_user.location)
        self.assertEqual(reg_user.role_id, log_user.role_id)
        self.assertEqual(reg_user.role_id, "4")

        # Deleting Test Account from database
        dbase.dbCursor.execute(
            "DELETE FROM Users "
            "WHERE firstName = ? AND lastName = ? ;",
            (self.f_name, self.l_name)
        )
        dbase.dbCursor.execute(
            "DELETE FROM Accounts "
            "WHERE username = ? ;",
            (self.usrnm,)
        )
        dbase.db.commit()

        ## Confirm Account Deletion
        confirm_user = acc.SchoolAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account login doesn't work for deleted account
        self.assertFalse(confirm_user)

    def test_business_account(self):
        ## Account class registration
        reg_user = acc.BusinessAccount(True,
                                password=self.password,
                                fst_name=self.f_name,
                                lst_name=self.l_name,
                                date_birth=self.d_birth,
                                location=self.loc )
        
        
        ## Account class login
        self.usrnm = dbase.generate_username(self.f_name, self.l_name, self.code)
        log_user = acc.BusinessAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account creation/login worked
        self.assertTrue(reg_user)
        self.assertTrue(log_user)
        # Test the account registration and login share the same values 
        # (i.e. they're the same account)
        self.assertEqual(reg_user.username, log_user.username)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.lst_name, log_user.lst_name)
        self.assertEqual(reg_user.fst_name, log_user.fst_name)
        self.assertEqual(reg_user.date_birth, log_user.date_birth)
        self.assertEqual(reg_user.location, log_user.location)
        self.assertEqual(reg_user.role_id, log_user.role_id)
        self.assertEqual(reg_user.role_id, "3")

        # Deleting Test Account from database
        dbase.dbCursor.execute(
            "DELETE FROM Users "
            "WHERE firstName = ? AND lastName = ? ;",
            (self.f_name, self.l_name)
        )
        dbase.dbCursor.execute(
            "DELETE FROM Accounts "
            "WHERE username = ? ;",
            (self.usrnm,)
        )
        dbase.db.commit()

        ## Confirm Account Deletion
        confirm_user = acc.BusinessAccount(False,
                                    password=self.password,
                                    username=self.usrnm)

        # Test account login doesn't work for deleted account
        self.assertFalse(confirm_user)

if __name__ == '__main__':
    unittest.main()