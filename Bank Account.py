class BankAccount:
    def __init__(self, accountholder_name, initial_balance=0):
        self.accountholder_name = accountholder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit Rs{amount} into {self.accountholder_name} has been successful.")
            print(f"The new balance is Rs{self.balance}.")
        else:
            print(f"Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Rs{amount} from {self.accountholder_name} account has been Withdraw.")
            print(f"The new balance is Rs{self.balance}")
        else:
            print(f"Invalid amount {amount}.")

    def Show_Account_Details(self):
        print("\n----Account Details----")
        print(f"The account holder name is {self.accountholder_name}.")
        print(f"The balance is Rs{self.balance}.")

accounts = {}
def create_Account():
    name = input("Enter the account holder name: ").strip()
    initial_deposit = float(input("Enter the initial deposit: "))
    account = BankAccount(name, initial_deposit)
    accounts[name] = account
    print(f"Account has been created successfully!")


def Access_Account():
    name = input("Enter the account holder name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n---Account Menu---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Account Details")
            print("4. Exit")
            choice = input("Enter your choice(1-4): ").strip()
            if choice == "1":
                deposit = float(input("Enter the deposit: "))
                account.deposit(deposit)
            elif choice == "2":
                withdraw = float(input("Enter the withdrawal: "))
                account.withdraw(withdraw)
            elif choice == "3":
                account.Show_Account_Details()
            elif choice == "4":
                print("Thank you for using this program!")
            else:
                print("Invalid choice.")
    else:
        print("Account does not exist.")


while True:
    print("\n---Bank Account---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    choice = input("Enter your choice(1-3): ").strip()
    if choice == "1":
        create_Account()
    elif choice == "2":
        Access_Account()
    elif choice == "3":
        print("Thank you for using this program!")
    else:
        print("Invalid choice.")
