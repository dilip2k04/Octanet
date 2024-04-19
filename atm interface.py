class ATM:
    def __init__(self):
        self.balance = 1000
        self.transaction_history = []
        self.language = "English"

    def authenticate(self):
        
        entered_password = input("\nEnter your ATM password: ")
    
        if entered_password == "0000":
            return True
        else:
            print("Authentication failed. Incorrect password.")
            return False

    def select_language(self):
        print("\nSelect Language:")
        print("1. English")
        print("2. Hindi")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            self.language = "English"
        elif choice == '2':
            self.language = "Hindi"
        else:
            print("Invalid choice. Defaulting to English.")

    def display_menu(self):
        print(f"\nWelcome to the ATM Interface ({self.language})")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Transactions History")
        print("5. Quit")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ₹{amount}")
            print(f"\nSuccessfully withdrew ₹{amount}")
        else:
            print("\nWithdrawal failed. Insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ₹{amount}")
            print(f"\nSuccessfully deposited ₹{amount}")
        else:
            print("\nDeposit failed. Invalid amount.")

    def transfer(self, amount, recipient):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Transferred ₹{amount} to {recipient}")
            print(f"\nSuccessfully transferred ₹{amount} to {recipient}")
        else:
            print("\nTransfer failed. Insufficient funds.")

    def display_transactions_history(self):
        print("\nTransactions History:")
        for transaction in self.transaction_history:
            print(transaction)

    def run(self):
        if self.authenticate():
            self.select_language()

            while True:
                self.display_menu()
                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    amount = float(input(f"Enter amount to withdraw (₹{self.language}): "))
                    self.withdraw(amount)
                elif choice == '2':
                    amount = float(input(f"Enter amount to deposit (₹{self.language}): "))
                    self.deposit(amount)
                elif choice == '3':
                    amount = float(input(f"Enter amount to transfer (₹{self.language}): "))
                    recipient = input(f"Enter recipient's name ({self.language}): ")
                    self.transfer(amount, recipient)
                elif choice == '4':
                    self.display_transactions_history()
                elif choice == '5':
                    print("\nThank you for using the ATM Interface.")
                    break
                else:
                    print("Invalid choice. Please try again.")



if __name__ == "__main__":
    atm = ATM()
    atm.run()
