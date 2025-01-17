import time
from functools import wraps
from datetime import datetime

# =============================================================================
#                           HELPER FUNCTIONS
# =============================================================================

def timestamp() -> str:
    """Return a nicely formatted timestamp."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")

def parse_date(datestr: str) -> datetime:
    """
    Attempt to parse a date from a 'YYYY-MM-DD' format.
    If invalid or empty, default to today's date.
    """
    if not datestr:
        return datetime.now()
    try:
        return datetime.strptime(datestr, "%Y-%m-%d")
    except ValueError:
        return datetime.now()

# =============================================================================
#                       IN-MEMORY 'DATABASE'
# =============================================================================

"""
USER_DB structure:
{
  "<username>": {
    "password": str,
    "role": "admin"/"user",
    "name": str,               # Full name
    "is_active": bool,
    "history": [ list of event logs ],
    "categories": set or list of categories,
    "expenses": [
      {
        "amount": float,
        "category": str,
        "date": datetime or stored as "YYYY-MM-DD",
        "description": str,
        "payment_method": str,
        "timestamp": str
      }, ...
    ]
  }, ...
}
"""

USER_DB = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "name": "System Admin",
        "is_active": True,
        "history": ["System admin account created."],
        "categories": {"General", "Food", "Bills"},
        "expenses": []
    },
    "alice": {
        "password": "alice123",
        "role": "user",
        "name": "Alice Example",
        "is_active": True,
        "history": ["Joined as a normal user."],
        "categories": {"Groceries", "Rent", "Entertainment"},
        "expenses": []
    }
}

current_user = None  # track logged in user

# =============================================================================
#                          DECORATORS
# =============================================================================

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global current_user
        if not current_user:
            print("You must be logged in to use this feature.")
            login()
            if not current_user:
                return
        if not USER_DB[current_user]["is_active"]:
            print("Your account is inactive. Contact admin.")
            return
        return func(*args, **kwargs)
    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global current_user
        if not current_user:
            print("You must be logged in to use this feature.")
            login()
            if not current_user:
                return
        if USER_DB[current_user]["role"] != "admin":
            print("Admin privileges required.")
            return
        return func(*args, **kwargs)
    return wrapper

# =============================================================================
#                        AUTH & SESSION
# =============================================================================

def login():
    global current_user
    uname = input("Enter username: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if not USER_DB[uname]["is_active"]:
        print("User is inactive. Contact admin.")
        return
    pw = input("Enter password: ").strip()
    if pw == USER_DB[uname]["password"]:
        current_user = uname
        print(f"\nWelcome {USER_DB[uname]['name']}! You are logged in as {USER_DB[uname]['role']}.")
    else:
        print("Incorrect password.")

def logout():
    global current_user
    if not current_user:
        print("No user is currently logged in.")
        return
    print(f"User {USER_DB[current_user]['name']} has been logged out.")
    current_user = None

# =============================================================================
#                      ADMIN FEATURES
# =============================================================================

@admin_required
def create_user():
    """Create a new user (admin/user)."""
    uname = input("Enter new username: ").strip()
    if uname in USER_DB:
        print("That username already exists.")
        return
    role = input("Enter role (admin/user) [default=user]: ").strip() or "user"
    name = input("Enter full name: ").strip()
    pw = input("Set password: ").strip()

    USER_DB[uname] = {
        "password": pw,
        "role": role.lower(),
        "name": name,
        "is_active": True,
        "history": [f"{timestamp()} Account created with role {role}."],
        "categories": set(),
        "expenses": []
    }
    print(f"User '{uname}' created as {role}.")

@admin_required
def toggle_user_status():
    """Activate/inactivate a user account."""
    uname = input("Enter username to toggle status: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot deactivate main admin.")
        return
    current_status = USER_DB[uname]["is_active"]
    USER_DB[uname]["is_active"] = not current_status
    new_status = "Active" if USER_DB[uname]["is_active"] else "Inactive"
    print(f"User '{uname}' is now {new_status}.")

@admin_required
def remove_user():
    """Remove a user from the system."""
    uname = input("Enter username to remove: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot remove main admin.")
        return
    confirm = input(f"Are you sure to remove '{uname}'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return
    del USER_DB[uname]
    print(f"User '{uname}' removed from system.")

@admin_required
def view_all_users():
    """View all users, their roles, status, and expense stats."""
    print("\n=== All Users ===")
    for uname, data in USER_DB.items():
        print(f"Username: {uname}, Role: {data['role']}, Active: {data['is_active']}, Name: {data['name']}, "
              f"NumExpenses: {len(data['expenses'])}")
    print("")

@admin_required
def view_all_expenses_admin():
    """
    Admin can see all expenses from all users.
    Summaries or the full list can be demonstrated.
    """
    print("\n=== All Expenses (All Users) ===")
    for uname, udata in USER_DB.items():
        if not udata["expenses"]:
            continue
        print(f"\n-- Expenses by {uname} ({udata['name']}) --")
        for exp in udata["expenses"]:
            date_str = exp["date"].strftime("%Y-%m-%d") if isinstance(exp["date"], datetime) else exp["date"]
            print(f"  Amount=${exp['amount']:.2f}, Cat={exp['category']}, Date={date_str}, Desc={exp['description']}, "
                  f"Method={exp['payment_method']}")

# =============================================================================
#                   USER FEATURES - CATEGORIES
# =============================================================================

@login_required
def add_category():
    """Add a new expense category to the current user's category list."""
    global current_user
    cat = input("Enter new category name: ").strip()
    if not cat:
        print("Category name cannot be empty.")
        return
    USER_DB[current_user]["categories"].add(cat)
    print(f"Category '{cat}' added.")

@login_required
def remove_category():
    """Remove an existing category from current user's list.
       Must ensure no expenses using that category or prompt to reassign.
    """
    global current_user
    user_cats = USER_DB[current_user]["categories"]
    if not user_cats:
        print("No categories to remove.")
        return
    print(f"Your Categories: {', '.join(user_cats)}")
    cat = input("Enter category name to remove: ").strip()
    if cat not in user_cats:
        print("You do not have such category.")
        return

    # Check if any expense is using this category
    user_exp = USER_DB[current_user]["expenses"]
    used_in_expenses = [e for e in user_exp if e["category"] == cat]
    if used_in_expenses:
        # Reassign or forbid removal
        choice = input(f"You have {len(used_in_expenses)} expenses in '{cat}'. "
                       f"Reassign them to a new category or 'cancel'? ").strip()
        if choice.lower() == "cancel":
            print("Removal cancelled.")
            return
        if choice not in user_cats:
            # if the user typed a new category that doesn't exist, create it
            USER_DB[current_user]["categories"].add(choice)
        # reassign
        for e in used_in_expenses:
            e["category"] = choice
        print(f"Reassigned those expenses from '{cat}' to '{choice}'.")
    # Now remove the old category
    user_cats.remove(cat)
    print(f"Category '{cat}' removed.")

@login_required
def view_categories():
    """View current user's categories."""
    global current_user
    user_cats = USER_DB[current_user]["categories"]
    if not user_cats:
        print("You have no categories. Use 'Add Category' to create some.")
    else:
        print("Your Categories:", ", ".join(user_cats))

# =============================================================================
#                USER FEATURES - EXPENSES
# =============================================================================

@login_required
def add_expense():
    """Add a new expense record for the current user."""
    global current_user
    # ask for amount, category, date, description, payment method
    amt_str = input("Enter amount: ").strip()
    try:
        amt = float(amt_str)
    except ValueError:
        print("Invalid amount. Setting to 0.")
        amt = 0.0

    user_cats = USER_DB[current_user]["categories"]
    if not user_cats:
        print("No categories found. You must add a category first.")
        return
    print(f"Categories: {', '.join(user_cats)}")
    cat = input("Enter category from above: ").strip()
    if cat not in user_cats:
        print("Invalid category. Please add it first or use an existing one.")
        return

    d_str = input("Enter date (YYYY-MM-DD) [default today]: ").strip()
    exp_date = parse_date(d_str)
    desc = input("Enter description [optional]: ").strip()
    method = input("Enter payment method (Cash/Card/Online, etc.): ").strip() or "Cash"

    new_exp = {
        "amount": amt,
        "category": cat,
        "date": exp_date,
        "description": desc,
        "payment_method": method,
        "timestamp": timestamp()
    }
    USER_DB[current_user]["expenses"].append(new_exp)
    print("Expense added successfully.")

@login_required
def view_expenses():
    """View the current user's expense records, optionally filter by date or category."""
    global current_user
    exp_list = USER_DB[current_user]["expenses"]
    if not exp_list:
        print("No expenses recorded yet.")
        return

    # Optional filters
    flt_cat = input("Filter by category (blank for none): ").strip()
    flt_start = input("Start date (YYYY-MM-DD, blank=none): ").strip()
    flt_end = input("End date (YYYY-MM-DD, blank=none): ").strip()

    start_dt = parse_date(flt_start) if flt_start else None
    end_dt = parse_date(flt_end) if flt_end else None

    # Filter
    filtered = []
    for e in exp_list:
        # Check category
        if flt_cat and e["category"] != flt_cat:
            continue
        # Check date
        e_date = e["date"]  # a datetime
        if start_dt and e_date < start_dt:
            continue
        if end_dt and e_date > end_dt:
            continue
        filtered.append(e)

    if not filtered:
        print("No expenses match your filters.")
        return

    # Sort by date?
    filtered.sort(key=lambda x: x["date"])
    total_amount = 0.0
    print("\n=== Your Filtered Expenses ===")
    for item in filtered:
        d_str = item["date"].strftime("%Y-%m-%d")
        print(f"Amount=${item['amount']:.2f}, Cat={item['category']}, Date={d_str}, "
              f"Desc='{item['description']}', Method={item['payment_method']}")
        total_amount += item['amount']
    print(f"Total of these expenses = ${total_amount:.2f}")

@login_required
def edit_expense():
    """Edit or remove an existing expense record.
       For demonstration, we’ll let the user pick from a short list or by date range.
    """
    global current_user
    exp_list = USER_DB[current_user]["expenses"]
    if not exp_list:
        print("No expenses to edit.")
        return

    # Display a short enumerated list
    print("\n=== Your Expenses (Most Recent 5) ===")
    display_list = exp_list[-5:] if len(exp_list) > 5 else exp_list
    for i, e in enumerate(display_list, start=1):
        d_str = e["date"].strftime("%Y-%m-%d")
        print(f"{i}. ${e['amount']:.2f} on {d_str}, Cat={e['category']}, Desc={e['description']}")

    choice_str = input("Choose an expense # to edit/remove or blank to skip: ").strip()
    if not choice_str:
        return
    try:
        choice = int(choice_str)
        if choice < 1 or choice > len(display_list):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    target = display_list[choice - 1]
    # Option: Edit or Remove
    action = input("(E)dit or (R)emove? ").strip().lower()
    if action == "r":
        exp_list.remove(target)
        print("Expense removed.")
    else:
        # Edit
        new_amt_str = input(f"New amount [old={target['amount']}] (blank=no change): ").strip()
        if new_amt_str:
            try:
                new_amt = float(new_amt_str)
                target["amount"] = new_amt
            except ValueError:
                pass

        # Category
        user_cats = USER_DB[current_user]["categories"]
        if user_cats:
            new_cat = input(f"New category [old={target['category']}], must be among {user_cats}: ").strip()
            if new_cat and new_cat in user_cats:
                target["category"] = new_cat

        # Date
        new_date_str = input(f"New date (YYYY-MM-DD) [old={target['date'].strftime('%Y-%m-%d')}]: ").strip()
        if new_date_str:
            ndt = parse_date(new_date_str)
            target["date"] = ndt

        # Description
        new_desc = input(f"New description [old={target['description']}]: ").strip()
        if new_desc:
            target["description"] = new_desc

        # Payment method
        new_pm = input(f"New payment method [old={target['payment_method']}]: ").strip()
        if new_pm:
            target["payment_method"] = new_pm

        print("Expense updated successfully.")

# =============================================================================
#                USER FEATURES - REPORTING
# =============================================================================

@login_required
def category_summary():
    """
    Summarize spending by category for the current user, optionally filtered by date range.
    """
    global current_user
    exp_list = USER_DB[current_user]["expenses"]
    if not exp_list:
        print("No expenses yet.")
        return

    flt_start = input("Start date (YYYY-MM-DD, blank=none): ").strip()
    flt_end = input("End date (YYYY-MM-DD, blank=none): ").strip()
    start_dt = parse_date(flt_start) if flt_start else None
    end_dt = parse_date(flt_end) if flt_end else None

    # accumulate by category
    cat_totals = {}
    for e in exp_list:
        e_date = e["date"]
        if start_dt and e_date < start_dt:
            continue
        if end_dt and e_date > end_dt:
            continue
        cat_totals[e["category"]] = cat_totals.get(e["category"], 0.0) + e["amount"]

    if not cat_totals:
        print("No expenses in that date range.")
        return

    print("\n=== Category Summary ===")
    grand_total = 0.0
    for c, amt in cat_totals.items():
        print(f"Category={c}, Amount=${amt:.2f}")
        grand_total += amt
    print(f"Grand Total = ${grand_total:.2f}")


@login_required
def monthly_summary():
    """Group expenses by year-month for the current user."""
    global current_user
    exp_list = USER_DB[current_user]["expenses"]
    if not exp_list:
        print("No expenses recorded.")
        return

    monthly_totals = {}
    for e in exp_list:
        y = e["date"].year
        m = e["date"].month
        key = f"{y}-{m:02d}"
        monthly_totals[key] = monthly_totals.get(key, 0.0) + e["amount"]

    # Display
    print("\n=== Monthly Summary ===")
    for k, amt in sorted(monthly_totals.items()):
        print(f"{k}: ${amt:.2f}")

# =============================================================================
#                        MAIN MENU
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Expense Tracker")
        print(f"Current User: {current_user if current_user else 'None'}")
        print("-------------------------------------")
        print("1.  Login")
        print("2.  Logout")

        print("\n-- Admin Features --")
        print("3.  Create User")
        print("4.  Toggle User Status")
        print("5.  Remove User")
        print("6.  View All Users")
        print("7.  View All Expenses (Admin)")

        print("\n-- User Features: Categories --")
        print("8.  Add Category")
        print("9.  Remove Category")
        print("10. View My Categories")

        print("\n-- User Features: Expenses --")
        print("11. Add Expense")
        print("12. View Expenses (Filter)")
        print("13. Edit/Remove Expense")

        print("\n-- User Features: Reporting --")
        print("14. Category Summary")
        print("15. Monthly Summary")

        print("\n16. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            login()
        elif choice == "2":
            logout()
        elif choice == "3":
            create_user()
        elif choice == "4":
            toggle_user_status()
        elif choice == "5":
            remove_user()
        elif choice == "6":
            view_all_users()
        elif choice == "7":
            view_all_expenses_admin()
        elif choice == "8":
            add_category()
        elif choice == "9":
            remove_category()
        elif choice == "10":
            view_categories()
        elif choice == "11":
            add_expense()
        elif choice == "12":
            view_expenses()
        elif choice == "13":
            edit_expense()
        elif choice == "14":
            category_summary()
        elif choice == "15":
            monthly_summary()
        elif choice == "16":
            print("\nExiting Education Trust Nasra School - Expense Tracker")
            break
        else:
            print("Invalid choice. Please try again.")


# =============================================================================
#                      SCRIPT ENTRY
# =============================================================================

if __name__ == "__main__":
    main_menu()