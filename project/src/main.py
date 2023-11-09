""" Main project file executable """
import accounts

if __name__ == "__main__":
    ## Account class testing
    new_acc = accounts.Account(True,
                               password="pass123",
                               fst_name="Pete",
                               lst_name="Smith",
                               access_code="829854",
                               date_birth="1979-10-20",
                               location="Yardbird" )
    #print("usrnm: \t",new_acc.username)

    logging_acc = accounts.Account(False,
                                   password="pass123",
                                   username="PeteSmit829854")

    ## Collective class testing
    new_biz = accounts.CollectiveAccount(True,
                                         password="testpass123",
                                         fst_name="Yardbird",
                                         lst_name="Co.",
                                         date_birth="2020-10-17",
                                         location="Hub")
    #print("usrnm: \t",new_biz.username)

    logging_biz = accounts.CollectiveAccount(False,
                                   password="testpass123",
                                   username="YardCo.100000")


    ## Professor class testing
    new_prof = accounts.ProfessorAccount(True,
                                         password="testpass123",
                                         fst_name="Timmy",
                                         lst_name="H",
                                         access_code="829854",
                                         date_birth="1980-12-13",
                                         location="Classroom")
    print("usrnm: \t",new_biz.username)

    logging_prof = accounts.ProfessorAccount(False,
                                   password="testpass123",
                                   username="YardCo.100000")
