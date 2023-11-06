import unittest
import database as db

'''
Functions to test, tested functions are marked with 1's
    IMPL    db_sqlite3_init():      
    YES     db_add_school():
    YES     db_get_schools():
    NO      db_bind_school_teacher():
    NO      db_get_access_code_from_account():
    YES     db_get_access_code_from_school():
    NO      db_get_teacher_from_username():
    YES     db_create_account():
    NO      db_update_user_secret():
    NO      db_get_user_secret():
    NO      db_check_account_login():
    NO      db_update_password():
    YES     db_read_account_data():
    NO      db_print_account_data():
    NO      db_send_message():               
    NO      db_get_inbox_users():
    NO      db_read_messages_between():
'''

class DatabaseTesting(unittest.TestCase):
    # Load the testing database by overwriting the standard cursor
    db.db, db.dbCursor = db.db_sqlite3_init('testDB')
    # Set the debug flag to false, removes excess printing
    db.debug = False
    schoolOne = "London High"
    schoolTwo = "Coventry High"

    def test_adding_schools(self):
        # Empty the table for testing
        db.dbCursor.execute(
            "DELETE FROM Schools"
        )
        # Add the schools
        db.db_add_school(self.schoolOne)
        db.db_add_school(self.schoolTwo)
        # Get the list of schools
        schoolsList = db.db_get_schools()
        # Check that the schools we made are in that list
        self.assertIn(self.schoolOne, schoolsList)
        self.assertIn(self.schoolTwo, schoolsList)
        # Check that an erroneous school is not in the list
        self.assertNotIn("Manchester High", schoolsList)

    def test_create_account(self):
        # Empty table for testing
        db.dbCursor.execute(
            "DELETE FROM Accounts"
        )
        # Empty table for testing
        db.dbCursor.execute(
            "DELETE FROM Users"
        )
        # Get the access codes for both schools
        bhamAccess = db.db_get_access_code_from_school(self.schoolOne)
        covAccess = db.db_get_access_code_from_school(self.schoolTwo)
        
        # Add a student account for Coventry
        covStdName = db.db_create_account(
            "Covent",
            "Stewdent",
            "CoventryLove!234",
            str(covAccess),
            "2002-12-31",
            "Coventry",
            1
        )
        self.assertEqual(covStdName, "CoveStew" + covAccess)
        # Add a teacher account for Coventry
        covTchName = db.db_create_account(
            "Covent",
            "Teechar",
            "ih8teaching",
            str(covAccess),
            "1978-10-23",
            "Coventry",
            2
        )
        self.assertEqual(covTchName, "CoveTeec" + covAccess)
        # Add a student account for Birmingham
        bhmStdName = db.db_create_account(
            "Bhrum",
            "Learnah",
            "iluvdirt",
            str(bhamAccess),
            "2003-01-28",
            "Coventry",
            1
        )
        self.assertEqual(bhmStdName, "BhruLear" + bhamAccess)
        # Add a teachher account for Birmingham
        bhmTchName = db.db_create_account(
            "Bh",
            "Tch",
            "ilov3stella",
            str(bhamAccess),
            "1979-09-21",
            "Birmingham",
            2
        )
        self.assertEqual(bhmTchName, "BhTch" + bhamAccess)


if __name__ == '__main__':
    unittest.main()