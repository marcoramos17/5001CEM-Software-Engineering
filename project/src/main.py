""" Main project file executable """
import accounts

if __name__ == "__main__":
    new_acc = accounts.Account(True, "pass123", "RegularUserAcc1", "John",
                               "Smith", "s", "aaa", "Yardbird" )
    print("usrnm: \t",new_acc.username)

    biz_acc = accounts.CollectiveAccount(True, "pass345", "BusinessAccount1", "Jimmy",
                               "J. Junior", "aaa", "Yardbird")
    print("usrnm: \t",biz_acc.username)
