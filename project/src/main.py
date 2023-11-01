import accounts

if __name__ == "__main__":
    new_acc = accounts.Account("TestUser", "pass123", False, 1, 1, 1)
    print(new_acc.username)
    