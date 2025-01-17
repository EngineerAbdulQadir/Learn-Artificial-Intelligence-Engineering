import time
from functools import wraps

# =============================================================================
#                          IN-MEMORY 'DATABASE'
# =============================================================================

"""
USER_DB structure:
{
  "admin": {
    "pin": "0000",
    "name": "System Administrator",
    "role": "admin",
    "accounts": {},
    "transactions": [],
    "daily_withdrawn": 0.0,
  },
  "u1001": {
    "pin": "1234",
    "name": "Alice Johnson",
    "role": "user",
    "accounts": {
        "Checking": 500.0,
        "Savings": 1000.0
    },
    "transactions": [
        "timestamped messages"
    ],
    "daily_withdrawn": 0.0
  },
  ...
}
"""

USER_DB = {
    "admin": {
        "pin": "0000",
        "name": "System Administrator",
        "role": "admin",
        "accounts": {},  # Admin might not have typical accounts, but let's keep structure
        "transactions": [],
        "daily_withdrawn": 0.0,  # For demonstration
    },
    "u1001": {
        "pin": "1234",
        "name": "Alice Johnson",
        "role": "user",
        "accounts": {
            "Checking": 500.0,
            "Savings": 1000.0
        },
        "transactions": [],
        "daily_withdrawn": 0.0
    },
    "u1002": {
        "pin": "4321",
        "name": "Bob Smith",
        "role": "user",
        "accounts": {
            "Checking": 750.0,
            "Savings": 2000.0
        },
        "transactions": [],
        "daily_withdrawn": 0.0
    },
}

# A simple daily withdrawal limit for demonstration
DAILY_WITHDRAWAL_LIMIT = 1000.0

# Track who is currently logged in
current_user_id = None


# =============================================================================
#                           HELPER / DECORATORS
# =============================================================================

def login_required(func):
    """Decorator to ensure that a user is logged in before accessing a feature."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        global current_user_id
        if not current_user_id:
            print("You must be logged in to use this feature.")
            login()
            if not current_user_id:
                return  # If still no login, stop
        return func(*args, **kwargs)
    return wrapper

def admin_required(func):
    """Decorator to ensure that the current user has admin privileges."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        global current_user_id
        if not current_user_id:
            print("You must be logged in to use this feature.")
            login()
            if not current_user_id:
                return
        if USER_DB[current_user_id]["role"] != "admin":
            print("Admin privileges are required to use this feature.")
            return
        return func(*args, **kwargs)
    return wrapper

def timestamp():
    """Returns a formatted timestamp string."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")


# =============================================================================
#                      AUTHENTICATION: LOGIN / LOGOUT
# =============================================================================

def login():
    """Allows a user (admin or user) to log in with an ID and PIN."""
    global current_user_id

    user_id = input("Enter your User ID (e.g., 'admin' or 'u1001'): ").strip()
    if user_id not in USER_DB:
        print("Invalid User ID.")
        return

    pin = input("Enter PIN: ").strip()
    if USER_DB[user_id]["pin"] == pin:
        current_user_id = user_id
        print(f"\nWelcome {USER_DB[user_id]['name']}! You are now logged in.")
    else:
        print("Incorrect PIN.")

def logout():
    """Logs out the current user."""
    global current_user_id
    if not current_user_id:
        print("No user is currently logged in.")
        return
    print(f"User {USER_DB[current_user_id]['name']} (ID: {current_user_id}) has been logged out.")
    current_user_id = None


# =============================================================================
#                      ADMIN FUNCTIONS
# =============================================================================

@admin_required
def create_user():
    """Create a new user (with user ID, name, and initial PIN)."""
    new_user_id = input("Enter new user ID (e.g., 'u1003'): ").strip()
    if new_user_id in USER_DB:
        print("That user ID already exists.")
        return
    name = input("Enter user full name: ").strip()
    pin = input("Set initial PIN: ").strip()

    # Create a basic user entry
    USER_DB[new_user_id] = {
        "pin": pin,
        "name": name,
        "role": "user",  # by default
        "accounts": {},
        "transactions": [],
        "daily_withdrawn": 0.0
    }
    print(f"User '{name}' created with ID '{new_user_id}'.")

@admin_required
def delete_user():
    """Delete an existing user (cannot delete admin)."""
    user_id = input("Enter user ID to delete: ").strip()
    if user_id not in USER_DB:
        print("User not found.")
        return
    if user_id == "admin":
        print("Cannot delete admin account.")
        return
    confirm = input(f"Are you sure you want to delete user '{user_id}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        del USER_DB[user_id]
        print(f"User '{user_id}' deleted.")
    else:
        print("Deletion cancelled.")

@admin_required
def view_all_users():
    """List all users in the system."""
    print("\n=== All Users ===")
    for uid, info in USER_DB.items():
        print(f"User ID: {uid}, Name: {info['name']}, Role: {info['role']}")


# =============================================================================
#                      USER / ATM FEATURES
# =============================================================================

@login_required
def change_pin():
    """Change the current user's PIN, verifying old PIN first."""
    global current_user_id
    old_pin = input("Enter your current PIN: ").strip()
    if USER_DB[current_user_id]["pin"] != old_pin:
        print("Current PIN is incorrect.")
        return
    new_pin = input("Enter new PIN: ").strip()
    confirm_pin = input("Confirm new PIN: ").strip()
    if new_pin != confirm_pin:
        print("PIN confirmation doesn't match.")
        return
    USER_DB[current_user_id]["pin"] = new_pin
    # Record transaction
    USER_DB[current_user_id]["transactions"].append(f"{timestamp()} PIN changed.")
    print("PIN successfully changed.")

@login_required
def show_balance():
    """Shows all sub-accounts and their balances."""
    user_info = USER_DB[current_user_id]
    print(f"\nAccount Holder: {user_info['name']}")
    if not user_info["accounts"]:
        print("No sub-accounts found. You can create some from the menu.")
        return
    for acc_type, bal in user_info["accounts"].items():
        print(f" - {acc_type} Balance: ${bal:.2f}")

@login_required
def create_sub_account():
    """User can create a new sub-account (e.g., 'Vacation Savings')."""
    user_info = USER_DB[current_user_id]
    acc_name = input("Enter a new sub-account name (e.g. 'Vacation Savings'): ").strip()
    if acc_name in user_info["accounts"]:
        print("That sub-account already exists.")
        return
    initial_deposit_str = input("Enter initial deposit amount (0 if none): ").strip()
    try:
        initial_deposit = float(initial_deposit_str)
        if initial_deposit < 0:
            print("Cannot have negative initial deposit.")
            return
        user_info["accounts"][acc_name] = initial_deposit
        user_info["transactions"].append(f"{timestamp()} Created sub-account '{acc_name}' with ${initial_deposit:.2f}.")
        print(f"Sub-account '{acc_name}' created successfully with balance ${initial_deposit:.2f}.")
    except ValueError:
        print("Invalid amount entered.")

@login_required
def deposit():
    """Deposits an amount into a chosen sub-account."""
    user_info = USER_DB[current_user_id]
    if not user_info["accounts"]:
        print("No sub-accounts found. Create one first.")
        return
    print("Available sub-accounts:")
    account_list = list(user_info["accounts"].keys())
    for i, acc_name in enumerate(account_list, start=1):
        print(f"{i}. {acc_name}")
    choice_str = input("Select an account by number: ").strip()
    try:
        choice = int(choice_str)
        if choice < 1 or choice > len(account_list):
            print("Invalid choice.")
            return
        selected_account = account_list[choice - 1]
        amount_str = input(f"Enter amount to deposit into {selected_account}: ").strip()
        amount = float(amount_str)
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        user_info["accounts"][selected_account] += amount
        message = f"{timestamp()} Deposited ${amount:.2f} to '{selected_account}'."
        user_info["transactions"].append(message)
        print(message)
    except ValueError:
        print("Invalid input.")

@login_required
def withdraw():
    """Withdraws an amount from a chosen sub-account, respecting daily limits."""
    user_info = USER_DB[current_user_id]
    if not user_info["accounts"]:
        print("No sub-accounts found. Create one first.")
        return
    print("Available sub-accounts:")
    account_list = list(user_info["accounts"].keys())
    for i, acc_name in enumerate(account_list, start=1):
        print(f"{i}. {acc_name}")
    choice_str = input("Select an account by number: ").strip()
    try:
        choice = int(choice_str)
        if choice < 1 or choice > len(account_list):
            print("Invalid choice.")
            return
        selected_account = account_list[choice - 1]
        amount_str = input(f"Enter amount to withdraw from {selected_account}: ").strip()
        amount = float(amount_str)
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        # Check daily limit
        daily_used = user_info["daily_withdrawn"]
        if daily_used + amount > DAILY_WITHDRAWAL_LIMIT:
            remaining = DAILY_WITHDRAWAL_LIMIT - daily_used
            print(f"You have ${remaining:.2f} remaining of your daily withdrawal limit (${DAILY_WITHDRAWAL_LIMIT}).")
            return

        # Check account balance
        if user_info["accounts"][selected_account] < amount:
            print(f"Insufficient funds in '{selected_account}'.")
            return

        user_info["accounts"][selected_account] -= amount
        user_info["daily_withdrawn"] += amount
        message = f"{timestamp()} Withdrew ${amount:.2f} from '{selected_account}'."
        user_info["transactions"].append(message)
        print(message)
    except ValueError:
        print("Invalid input.")

@login_required
def transfer():
    """Transfer funds between sub-accounts or even different users if desired."""
    # For simplicity, let’s do same-user sub-account transfer.
    # If you want cross-user, just adapt the code.
    user_info = USER_DB[current_user_id]
    if len(user_info["accounts"]) < 2:
        print("You need at least two sub-accounts to transfer within your profile.")
        return
    print("Your sub-accounts:")
    account_list = list(user_info["accounts"].keys())
    for i, acc_name in enumerate(account_list, start=1):
        print(f"{i}. {acc_name}")
    from_choice_str = input("Select FROM account (by number): ").strip()
    to_choice_str = input("Select TO account (by number): ").strip()
    try:
        from_choice = int(from_choice_str)
        to_choice = int(to_choice_str)
        if (from_choice < 1 or from_choice > len(account_list)
                or to_choice < 1 or to_choice > len(account_list)):
            print("Invalid choice.")
            return
        if from_choice == to_choice:
            print("Cannot transfer to the same account.")
            return
        from_acc = account_list[from_choice - 1]
        to_acc = account_list[to_choice - 1]

        amount_str = input(f"Enter amount to transfer from '{from_acc}' to '{to_acc}': ").strip()
        amount = float(amount_str)
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if user_info["accounts"][from_acc] < amount:
            print(f"Insufficient funds in '{from_acc}'.")
            return

        user_info["accounts"][from_acc] -= amount
        user_info["accounts"][to_acc] += amount
        message = f"{timestamp()} Transferred ${amount:.2f} from '{from_acc}' to '{to_acc}'."
        user_info["transactions"].append(message)
        print(message)
    except ValueError:
        print("Invalid input.")

@login_required
def reset_daily_withdrawal():
    """Resets the daily withdrawal usage for the current user (for demonstration)."""
    user_info = USER_DB[current_user_id]
    user_info["daily_withdrawn"] = 0.0
    print("Daily withdrawal usage reset to 0.0 for demonstration.")


@login_required
def view_transactions():
    """Views transaction history for the current user."""
    user_info = USER_DB[current_user_id]
    if not user_info["transactions"]:
        print("No transactions found.")
        return
    print(f"\n=== Transaction History for {user_info['name']} ===")
    for txn in user_info["transactions"]:
        print(txn)


# =============================================================================
#                     MAIN MENU / CLI LOOP (Enhanced)
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Digital ATM Machine Simulation")
        print("------------------------------------------------------------")
        print(f"Current User: {current_user_id if current_user_id else 'None'}")
        print("------------------------------------------------------------")

        if current_user_id:  # Show options based on login status and role
            if USER_DB[current_user_id]["role"] == "admin":
                print("1.  Logout")
                print("2.  Create New User")
                print("3.  Delete User")
                print("4.  View All Users")
                print("5.  Show Balances")
                print("6.  Create a Sub-Account")
                print("7.  Deposit")
                print("8.  Withdraw")
                print("9.  Transfer (within your sub-accounts)")
                print("10. Change PIN")
                print("11. Transaction History")
                print("12. Reset Daily Withdrawal (demo)")
                print("13. Exit")
            else:  # User menu
                print("1.  Logout")
                print("2.  Show Balances")
                print("3.  Create a Sub-Account")
                print("4.  Deposit")
                print("5.  Withdraw")
                print("6.  Transfer (within your sub-accounts)")
                print("7.  Change PIN")
                print("8.  Transaction History")
                print("9.  Exit")
        else:  # Not logged in
            print("1.  Login")
            print("2.  Exit")

        choice = input("Enter your choice: ").strip()

        if current_user_id:
            if USER_DB[current_user_id]["role"] == "admin":
                if choice == "1":
                    logout()
                elif choice == "2":
                    create_user()
                elif choice == "3":
                    delete_user()
                elif choice == "4":
                    view_all_users()
                elif choice == "5":
                    show_balance()
                elif choice == "6":
                  create_sub_account()
                elif choice == "7":
                    deposit()
                elif choice == "8":
                    withdraw()
                elif choice == "9":
                    transfer()
                elif choice == "10":
                    change_pin()
                elif choice == "11":
                    view_transactions()
                elif choice == "12":
                    reset_daily_withdrawal()
                elif choice == "13":
                    print("\nThank you for using the Education Trust Nasra School - Digital ATM Machine Simulation.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else: #user
                if choice == "1":
                    logout()
                elif choice == "2":
                    show_balance()
                elif choice == "3":
                  create_sub_account()
                elif choice == "4":
                    deposit()
                elif choice == "5":
                    withdraw()
                elif choice == "6":
                    transfer()
                elif choice == "7":
                    change_pin()
                elif choice == "8":
                    view_transactions()
                elif choice == "9":
                    print("\nThank you for using the Education Trust Nasra School - Digital ATM Machine Simulation.")
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:  # Not logged in
            if choice == "1":
                login()
            elif choice == "2":
                print("\nThank you for using the Education Trust Nasra School - Digital ATM Machine Simulation.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()