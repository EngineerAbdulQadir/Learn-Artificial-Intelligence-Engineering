from typing import Union

# ============================================
#               CLASS DEFINITIONS
# ============================================

class BankAccount:
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number: str = account_number
        self.__balance: float = balance

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def transfer(self, target_account, amount: float) -> None:
        """
        Transfer 'amount' from this account to 'target_account', if sufficient balance.
        """
        if self.__balance >= amount:
            self.__balance -= amount
            target_account.deposit(amount)
        else:
            print("Insufficient balance to complete transfer.")

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return (f"Account Number: {self.account_number}\n"
                f"Balance: {self.__balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, interest_rate: float) -> None:
        super().__init__(account_number, balance)
        self.interest_rate: float = interest_rate

    def calculate_interest(self) -> float:
        return self.get_balance() * self.interest_rate

    def apply_interest(self) -> None:
        """
        Applies (adds) the calculated interest to the current balance.
        """
        interest = self.calculate_interest()
        self.deposit(interest)

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info}\nInterest Rate: {self.interest_rate}"


class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, balance: float, overdraft_limit: float) -> None:
        super().__init__(account_number, balance)
        self.overdraft_limit: float = overdraft_limit

    def withdraw(self, amount: float) -> None:
        # Overdraft allows the balance to go negative down to -overdraft_limit
        if self.get_balance() + self.overdraft_limit >= amount:
            self.deposit(-amount)  # Using deposit with a negative amount
        else:
            print("Overdraft limit exceeded")

    def transfer(self, target_account, amount: float) -> None:
        """
        Transfer 'amount' from this account to 'target_account'.
        This respects the overdraft limit.
        """
        if self.get_balance() + self.overdraft_limit >= amount:
            self.deposit(-amount)
            target_account.deposit(amount)
        else:
            print("Overdraft limit exceeded for transfer.")

    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info}\nOverdraft Limit: {self.overdraft_limit}"


# ============================================
#         MAIN PROGRAM WITH MENU
# ============================================

def main():
    accounts = {}  # Dictionary to store account_number -> Account object

    while True:
        print("\n====== ETNS -> Banking Management System ======")
        print("1. Create a new account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer funds between accounts")
        print("5. Show account info")
        print("6. Calculate & apply interest (Savings only)")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_to_account(accounts)
        elif choice == "3":
            withdraw_from_account(accounts)
        elif choice == "4":
            transfer_between_accounts(accounts)
        elif choice == "5":
            show_account_info(accounts)
        elif choice == "6":
            apply_interest_savings(accounts)
        elif choice == "7":
            print("Thank you for using ETNS -> Banking Management System!")
            break
        else:
            print("Invalid option. Please try again.")


# ========== HELPER FUNCTIONS FOR MENU ==========

def create_account(accounts: dict):
    """
    Prompts the user to create a new BankAccount, SavingsAccount, or CheckingAccount.
    Stores it in the 'accounts' dictionary.
    """
    print("\n--- Create a New Account ---")
    print("Choose the type of account to create:")
    print("1. Basic Bank Account")
    print("2. Savings Account")
    print("3. Checking Account")

    acct_choice = input("Enter your choice (1/2/3): ").strip()
    acct_number = input("Enter an account number: ").strip()

    if acct_number in accounts:
        print("Error: An account with that number already exists.")
        return

    bal_str = input("Enter initial balance: ").strip()
    try:
        balance = float(bal_str)
    except ValueError:
        print("Invalid balance input. Defaulting to 0.")
        balance = 0.0

    if acct_choice == "1":
        # Basic Bank Account
        new_account = BankAccount(acct_number, balance)
        accounts[acct_number] = new_account
        print(f"Created BankAccount with number {acct_number}.")

    elif acct_choice == "2":
        # Savings Account
        int_str = input("Enter interest rate (e.g. 0.05 for 5%): ").strip()
        try:
            interest_rate = float(int_str)
        except ValueError:
            print("Invalid interest rate. Defaulting to 0.")
            interest_rate = 0.0
        new_account = SavingsAccount(acct_number, balance, interest_rate)
        accounts[acct_number] = new_account
        print(f"Created SavingsAccount with number {acct_number}.")

    elif acct_choice == "3":
        # Checking Account
        od_str = input("Enter overdraft limit: ").strip()
        try:
            overdraft_limit = float(od_str)
        except ValueError:
            print("Invalid overdraft limit. Defaulting to 0.")
            overdraft_limit = 0.0
        new_account = CheckingAccount(acct_number, balance, overdraft_limit)
        accounts[acct_number] = new_account
        print(f"Created CheckingAccount with number {acct_number}.")

    else:
        print("Invalid selection. No account created.")

def deposit_to_account(accounts: dict):
    """
    Prompts user to deposit money into an existing account.
    """
    print("\n--- Deposit to Account ---")
    acct_number = input("Enter the account number: ").strip()

    account = accounts.get(acct_number)
    if not account:
        print("Account not found.")
        return

    amount_str = input("Enter deposit amount: ").strip()
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid deposit amount.")
        return

    account.deposit(amount)
    print(f"Deposited {amount} into account {acct_number}. New balance: {account.get_balance()}")

def withdraw_from_account(accounts: dict):
    """
    Prompts user to withdraw money from an existing account.
    """
    print("\n--- Withdraw from Account ---")
    acct_number = input("Enter the account number: ").strip()

    account = accounts.get(acct_number)
    if not account:
        print("Account not found.")
        return

    amount_str = input("Enter withdrawal amount: ").strip()
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid withdrawal amount.")
        return

    account.withdraw(amount)
    print(f"New balance in account {acct_number}: {account.get_balance()}")

def transfer_between_accounts(accounts: dict):
    """
    Prompts user to transfer funds from one account to another.
    """
    print("\n--- Transfer Funds ---")
    source_acct_num = input("Enter the source account number: ").strip()
    target_acct_num = input("Enter the target account number: ").strip()

    if source_acct_num not in accounts:
        print("Source account not found.")
        return
    if target_acct_num not in accounts:
        print("Target account not found.")
        return

    if source_acct_num == target_acct_num:
        print("Cannot transfer to the same account.")
        return

    amount_str = input("Enter transfer amount: ").strip()
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid transfer amount.")
        return

    source_account = accounts[source_acct_num]
    target_account = accounts[target_acct_num]

    source_account.transfer(target_account, amount)
    print(f"Transfer complete. New balances:")
    print(f"  {source_acct_num}: {source_account.get_balance()}")
    print(f"  {target_acct_num}: {target_account.get_balance()}")

def show_account_info(accounts: dict):
    """
    Displays the account info for a given account number.
    """
    print("\n--- Show Account Info ---")
    acct_number = input("Enter the account number: ").strip()
    account = accounts.get(acct_number)

    if not account:
        print("Account not found.")
        return

    print("\nAccount Details:")
    print(account)

    # Additional details if it's Savings or Checking
    if isinstance(account, SavingsAccount):
        print(f"Calculated Interest (not yet added to balance): {account.calculate_interest()}")
    elif isinstance(account, CheckingAccount):
        print(f"Overdraft Limit: {account.overdraft_limit}")

def apply_interest_savings(accounts: dict):
    """
    Applies interest to a SavingsAccount by account number.
    """
    print("\n--- Apply Interest (Savings Only) ---")
    acct_number = input("Enter the savings account number: ").strip()
    account = accounts.get(acct_number)

    if not account:
        print("Account not found.")
        return

    if not isinstance(account, SavingsAccount):
        print("This is not a SavingsAccount.")
        return

    # Apply interest
    interest_before = account.calculate_interest()
    account.apply_interest()
    print(f"Interest of {interest_before} has been added.")
    print(f"New balance: {account.get_balance()}")


# ============================================
#               PROGRAM ENTRY
# ============================================
if __name__ == "__main__":
    main()