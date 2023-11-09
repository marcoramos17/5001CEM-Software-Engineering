""" Main project file executable """
import accounts

if __name__ == "__main__":
    new_acc = accounts.Account(True,
                               password="pass123",
                               fst_name="Pete",
                               lst_name="Smith",
                               access_code="829854",
                               date_birth="1979-10-20",
                               location="Yardbird" )
    print("usrnm: \t",new_acc.username)

    logging_acc = accounts.Account(False,
                                   password="pass123",
                                   username="PeteSmit829854")

    new_biz = accounts.CollectiveAccount(True,
                                         password="testpass123",
                                         fst_name="Yardbird",
                                         lst_name="Co.",
                                         date_birth="2020-10-17",
                                         location="Hub")
    print("usrnm: \t",new_biz.username)

    logging_biz = accounts.CollectiveAccount(False,
                                   password="testpass123",
                                   username="PeteSmit829854")
    #biz_acc = accounts.CollectiveAccount(True, "pass345", "Jimmy",
    #                           "J. Junior", "829854", "Yardbird")
    #print("usrnm: \t",biz_acc.username)
