class BankAccount:
    def __init__(self, account_number, name, balance, password):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.password = password

    def withdraw_cash(self, amount, password):
        if password == self.password:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. Your new balance is: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid password.")

    def credit_cash(self, amount):
        self.balance += amount
        print(f"Cash credited. Your new balance is: ${self.balance:.2f}")

    def change_password(self, old_password, new_password):
        if old_password == self.password:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Invalid old password.")

def main():
    # Example account setup
    account = BankAccount("12345678", "John Doe", 1000.0, "password123")

    while True:
        print("\nBank System Menu:")
        print("1. Withdraw Cash")
        print("2. Credit Cash")
        print("3. Change Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to withdraw: "))
            password = input("Enter your password: ")
            account.withdraw_cash(amount, password)
        elif choice == "2":
            amount = float(input("Enter amount to credit: "))
            account.credit_cash(amount)
        elif choice == "3":
            old_password = input("Enter your old password: ")
            new_password = input("Enter your new password: ")
            account.change_password(old_password, new_password)
        elif choice == "4":
            print("Exiting the bank system.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()