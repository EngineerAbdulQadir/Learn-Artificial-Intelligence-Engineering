import time
import hashlib
from functools import wraps
from datetime import datetime

# =============================================================================
#                            HELPER FUNCTIONS
# =============================================================================

def timestamp():
    """Returns a standard string timestamp."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")

def hash_password(plain_text: str) -> str:
    """
    Returns a SHA256 hash of the plain_text.
    In a real system, use salt + bcrypt or passlib.
    """
    return hashlib.sha256(plain_text.encode('utf-8')).hexdigest()

def generate_employee_id() -> str:
    """
    Generates a unique ID for new employees, e.g., 'E1003'.
    We'll keep a simple incremental system in memory.
    """
    global EMPLOYEE_ID_COUNTER
    EMPLOYEE_ID_COUNTER += 1
    return f"E{EMPLOYEE_ID_COUNTER}"


# =============================================================================
#                         IN-MEMORY 'DATABASE'
# =============================================================================

"""
EMPLOYEES_DB:
{
  "<username>": {
    "name": str,
    "employee_id": str,   # e.g. "E1001"
    "role": str,          # "admin", "manager", or "user"
    "password": str,      # hashed password
    "department": str or None,
    "location": str or None,    # optional for department-based location
    "salary": float,
    "history": [list of strings with timestamps],
    "is_active": bool,
    "shifts": [
       {"date": "YYYY-MM-DD", "start": "HH:MM", "end": "HH:MM"}
    ],
    "performance_notes": [
       {"timestamp": "...", "note": "...", "added_by": "..."}
    ],
    "projects": set() or list,
    "time_logs": [ {"clock_in": "...", "clock_out": "..."} ],
    ...
  },
  ...
}

DEPARTMENTS_DB:
{
  "<department_name>": {
    "manager": "<username>",    # must have 'role' in ["manager","admin"]
    "employees": list of usernames,
    "location": str (optional)
  },
  ...
}

We also track an auto-increment:
EMPLOYEE_ID_COUNTER: for generating new employee IDs
"""

EMPLOYEE_ID_COUNTER = 1002  # We'll start from E1003 for new employees
EMPLOYEES_DB = {
    "admin": {
        "name": "System Admin",
        "employee_id": "E1000",
        "role": "admin",
        "password": hash_password("admin123"),
        "department": None,
        "location": None,
        "salary": 0.0,
        "history": [f"{timestamp()} Created admin account."],
        "is_active": True,
        "shifts": [],
        "performance_notes": [],
        "projects": set(),
        "time_logs": []
    },
    "manager_anna": {
        "name": "Anna Manager",
        "employee_id": "E1001",
        "role": "manager",
        "password": hash_password("manager123"),
        "department": "HR",
        "location": "HQ Building, 3rd Floor",
        "salary": 60000.0,
        "history": [f"{timestamp()} Created manager account for Anna."],
        "is_active": True,
        "shifts": [],
        "performance_notes": [],
        "projects": set(),
        "time_logs": []
    },
    "john_smith": {
        "name": "John Smith",
        "employee_id": "E1002",
        "role": "user",
        "password": hash_password("john123"),
        "department": "HR",
        "location": "HQ Building, 3rd Floor",
        "salary": 45000.0,
        "history": [],
        "is_active": True,
        "shifts": [],
        "performance_notes": [],
        "projects": set(),
        "time_logs": []
    },
}

DEPARTMENTS_DB = {
    "HR": {
        "manager": "manager_anna",
        "employees": ["manager_anna", "john_smith"],
        "location": "HQ Building, 3rd Floor"
    },
    "Engineering": {
        "manager": None,
        "employees": [],
        "location": "Tech Park, 2nd Floor"
    }
}

current_user = None


# =============================================================================
#                     DECORATORS: LOGIN & ROLE CHECK
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
        if EMPLOYEES_DB[current_user]["role"] != "admin":
            print("Admin privileges required.")
            return
        return func(*args, **kwargs)
    return wrapper

def manager_or_admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global current_user
        if not current_user:
            print("You must be logged in to use this feature.")
            login()
            if not current_user:
                return
        user_role = EMPLOYEES_DB[current_user]["role"]
        if user_role not in ["manager", "admin"]:
            print("Manager or Admin privileges required.")
            return
        return func(*args, **kwargs)
    return wrapper


# =============================================================================
#                  AUTHENTICATION & SESSION
# =============================================================================

def login():
    global current_user
    username = input("Enter username: ").strip()
    if username not in EMPLOYEES_DB:
        print("Username not found.")
        return
    if not EMPLOYEES_DB[username]["is_active"]:
        print("This account is inactive. Contact Admin.")
        return

    password = input("Enter password: ").strip()
    hashed = hash_password(password)
    if EMPLOYEES_DB[username]["password"] == hashed:
        current_user = username
        print(f"\nWelcome {EMPLOYEES_DB[username]['name']}! You are now logged in.")
    else:
        print("Incorrect password.")

def logout():
    global current_user
    if not current_user:
        print("No user is logged in.")
        return
    print(f"User {EMPLOYEES_DB[current_user]['name']} has been logged out.")
    current_user = None


# =============================================================================
#                  ADMIN FEATURES
# =============================================================================

@admin_required
def create_employee():
    """
    Creates a new employee record. Assign a role (admin/manager/user).
    Salary can be set. Department optional.
    Generates an employee_id automatically.
    """
    uname = input("Enter new username: ").strip()
    if uname in EMPLOYEES_DB:
        print("That username already exists.")
        return
    fullname = input("Enter employee's full name: ").strip()
    role = input("Enter role (admin/manager/user) [default=user]: ").strip() or "user"
    password = input("Set initial password: ").strip()
    hashed_pw = hash_password(password)

    # Department
    dept = input("Enter department name (or blank): ").strip()
    if not dept:
        dept = None
    else:
        if dept not in DEPARTMENTS_DB:
            create_it = input(f"Department '{dept}' not found. Create it? [yes/no]: ").strip().lower()
            if create_it == "yes":
                DEPARTMENTS_DB[dept] = {
                    "manager": None,
                    "employees": [],
                    "location": None
                }
            else:
                dept = None  # If not created, ignore

    salary_str = input("Enter salary (default=0): ").strip()
    try:
        salary = float(salary_str) if salary_str else 0.0
    except ValueError:
        salary = 0.0

    new_eid = generate_employee_id()

    EMPLOYEES_DB[uname] = {
        "name": fullname,
        "employee_id": new_eid,
        "role": role.lower(),
        "password": hashed_pw,
        "department": dept,
        "location": None,
        "salary": salary,
        "history": [f"{timestamp()} Created employee record."],
        "is_active": True,
        "shifts": [],
        "performance_notes": [],
        "projects": set(),
        "time_logs": []
    }
    # If dept was set, add to that dept
    if dept and dept in DEPARTMENTS_DB:
        DEPARTMENTS_DB[dept]["employees"].append(uname)

    print(f"Employee '{fullname}' created (username='{uname}'), ID={new_eid}.")


@admin_required
def delete_employee():
    """
    Delete an employee record permanently, except for 'admin' itself.
    """
    uname = input("Enter username to delete: ").strip()
    if uname not in EMPLOYEES_DB:
        print("No such username.")
        return
    if uname == "admin":
        print("Cannot delete main admin.")
        return
    confirm = input(f"Are you sure you want to delete '{uname}'? [yes/no]: ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return

    dept = EMPLOYEES_DB[uname]["department"]
    if dept and dept in DEPARTMENTS_DB:
        if uname in DEPARTMENTS_DB[dept]["employees"]:
            DEPARTMENTS_DB[dept]["employees"].remove(uname)
    del EMPLOYEES_DB[uname]
    print(f"Employee '{uname}' deleted.")


@admin_required
def toggle_employee_active():
    """Activate or deactivate an employee account."""
    uname = input("Enter username to toggle: ").strip()
    if uname not in EMPLOYEES_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot deactivate main admin.")
        return
    current_status = EMPLOYEES_DB[uname]["is_active"]
    EMPLOYEES_DB[uname]["is_active"] = not current_status
    new_status = "Active" if EMPLOYEES_DB[uname]["is_active"] else "Inactive"
    EMPLOYEES_DB[uname]["history"].append(f"{timestamp()} Status changed to {new_status}.")
    print(f"Employee '{uname}' is now {new_status}.")


@admin_required
def view_all_employees():
    """Displays a detailed list of all employees."""
    print("\n=== ALL EMPLOYEES ===")
    for uname, data in EMPLOYEES_DB.items():
        print(f"Username: {uname}, EmployeeID: {data['employee_id']}, Name: {data['name']}, "
              f"Role: {data['role']}, Dept: {data['department']}, Salary: {data['salary']}, "
              f"Active: {data['is_active']}")


@admin_required
def create_department():
    """Create a new department with optional location info."""
    dname = input("Enter department name: ").strip()
    if dname in DEPARTMENTS_DB:
        print("Department already exists.")
        return
    location = input("Enter department location (optional): ").strip() or None
    DEPARTMENTS_DB[dname] = {
        "manager": None,
        "employees": [],
        "location": location
    }
    print(f"Department '{dname}' created with location '{location}'.")


@admin_required
def delete_department():
    """Delete an existing department. Reassign employees to no department."""
    dname = input("Enter department name to delete: ").strip()
    if dname not in DEPARTMENTS_DB:
        print("No such department.")
        return
    confirm = input(f"Are you sure to delete '{dname}'? [yes/no]: ").strip().lower()
    if confirm != "yes":
        print("Cancelled.")
        return
    employees_in_dept = DEPARTMENTS_DB[dname]["employees"]
    for euname in employees_in_dept:
        if euname in EMPLOYEES_DB:
            EMPLOYEES_DB[euname]["department"] = None
    del DEPARTMENTS_DB[dname]
    print(f"Department '{dname}' deleted.")


# =============================================================================
#             MANAGER & ADMIN FEATURES (DEPARTMENT SCOPED)
# =============================================================================

@manager_or_admin_required
def assign_manager_to_dept():
    """
    Let admin/manager assign a manager to a department.
    If a manager is assigned, remove manager role from previous if needed.
    """
    dname = input("Enter department name: ").strip()
    if dname not in DEPARTMENTS_DB:
        print("No such department.")
        return
    uname = input("Enter the new manager username: ").strip()
    if uname not in EMPLOYEES_DB:
        print("No such user.")
        return
    # Might also check if user's role is manager or admin
    # For now, we can auto-upgrade them to manager:
    EMPLOYEES_DB[uname]["role"] = "manager"
    # Remove from old dept if needed
    old_mgr = DEPARTMENTS_DB[dname]["manager"]
    DEPARTMENTS_DB[dname]["manager"] = uname
    if uname not in DEPARTMENTS_DB[dname]["employees"]:
        DEPARTMENTS_DB[dname]["employees"].append(uname)
    EMPLOYEES_DB[uname]["department"] = dname

    print(f"User '{uname}' is now manager of dept '{dname}'. Previous manager was '{old_mgr}'.")


@manager_or_admin_required
def assign_employee_to_dept():
    """Moves an employee to manager’s department (or any, if admin)."""
    global current_user
    dname = input("Enter department name to place employee in: ").strip()
    if dname not in DEPARTMENTS_DB:
        print("No such department.")
        return

    user_role = EMPLOYEES_DB[current_user]["role"]
    # If current user is manager, only let them assign to their dept
    if user_role == "manager" and DEPARTMENTS_DB[dname]["manager"] != current_user:
        print("You can only assign employees to the department you manage.")
        return

    uname = input("Enter employee username to assign: ").strip()
    if uname not in EMPLOYEES_DB:
        print("No such user.")
        return

    # Remove from old dept if any
    old_dept = EMPLOYEES_DB[uname]["department"]
    if old_dept and old_dept in DEPARTMENTS_DB:
        if uname in DEPARTMENTS_DB[old_dept]["employees"]:
            DEPARTMENTS_DB[old_dept]["employees"].remove(uname)

    # Add to new dept
    DEPARTMENTS_DB[dname]["employees"].append(uname)
    EMPLOYEES_DB[uname]["department"] = dname
    print(f"User '{uname}' assigned to dept '{dname}' successfully.")


@manager_or_admin_required
def schedule_shift():
    """Assign a shift to an employee in your department."""
    global current_user
    uname = input("Enter employee username for shift: ").strip()
    if uname not in EMPLOYEES_DB:
        print("No such user.")
        return
    # Check dept scope if manager
    user_role = EMPLOYEES_DB[current_user]["role"]
    if user_role == "manager":
        my_dept = EMPLOYEES_DB[current_user]["department"]
        if EMPLOYEES_DB[uname]["department"] != my_dept:
            print("Cannot schedule an employee outside your department.")
            return

    shift_date = input("Enter shift date (YYYY-MM-DD): ").strip()
    start_time = input("Start time (HH:MM): ").strip()
    end_time = input("End time (HH:MM): ").strip()
    # Basic validations omitted for brevity
    shift_record = {
        "date": shift_date,
        "start": start_time,
        "end": end_time
    }
    EMPLOYEES_DB[uname]["shifts"].append(shift_record)
    print(f"Shift assigned to {uname} on {shift_date}, {start_time}-{end_time}.")


@manager_or_admin_required
def add_performance_note():
    """Add a performance note to an employee in manager’s department or for any if admin."""
    global current_user
    uname = input("Enter employee username: ").strip()
    if uname not in EMPLOYEES_DB:
        print("No such user.")
        return
    # If manager, must be in same dept
    if EMPLOYEES_DB[current_user]["role"] == "manager":
        my_dept = EMPLOYEES_DB[current_user]["department"]
        if EMPLOYEES_DB[uname]["department"] != my_dept:
            print("That employee is outside your department.")
            return
    note = input("Enter performance note: ").strip()
    record = {
        "timestamp": timestamp(),
        "note": note,
        "added_by": current_user
    }
    EMPLOYEES_DB[uname]["performance_notes"].append(record)
    print(f"Performance note added to {uname}.")


@manager_or_admin_required
def assign_project():
    """Assign an employee to a project."""
    global current_user
    uname = input("Enter employee username: ").strip()
    if uname not in EMPLOYEES_DB:
        print("No such user.")
        return
    # Department scope check for managers
    if EMPLOYEES_DB[current_user]["role"] == "manager":
        my_dept = EMPLOYEES_DB[current_user]["department"]
        if EMPLOYEES_DB[uname]["department"] != my_dept:
            print("Employee is outside your department.")
            return
    project_name = input("Enter project name: ").strip()
    EMPLOYEES_DB[uname]["projects"].add(project_name)
    print(f"Employee '{uname}' assigned to project '{project_name}'.")


@manager_or_admin_required
def view_time_logs_dept():
    """Manager or admin can view clock in/out logs for employees in a department (manager sees their dept)."""
    global current_user
    user_role = EMPLOYEES_DB[current_user]["role"]
    if user_role == "manager":
        # Show logs only for manager’s dept
        my_dept = EMPLOYEES_DB[current_user]["department"]
        print(f"\nTime logs for department '{my_dept}':")
        for uname in DEPARTMENTS_DB[my_dept]["employees"]:
            logs = EMPLOYEES_DB[uname]["time_logs"]
            if not logs:
                continue
            print(f"\nUser {uname} ({EMPLOYEES_DB[uname]['name']}):")
            for rec in logs:
                print(f"  Clock in: {rec['clock_in']}, Clock out: {rec.get('clock_out','--still in--')}")
    else:
        # Admin can pick a dept
        dname = input("Enter department name: ").strip()
        if dname not in DEPARTMENTS_DB:
            print("No such department.")
            return
        print(f"\nTime logs for department '{dname}':")
        for uname in DEPARTMENTS_DB[dname]["employees"]:
            logs = EMPLOYEES_DB[uname]["time_logs"]
            if not logs:
                continue
            print(f"\nUser {uname} ({EMPLOYEES_DB[uname]['name']}):")
            for rec in logs:
                print(f"  Clock in: {rec['clock_in']}, Clock out: {rec.get('clock_out','--still in--')}")


@manager_or_admin_required
def generate_monthly_payroll():
    """
    Very basic payroll generation.
    Could consider hours from time_logs or just use salary (ex. monthly = salary/12).
    """
    # For simplicity, we do “monthly pay = salary / 12”.
    # Optionally factor in hours from time_logs if you want an hourly approach.
    dname = None
    if EMPLOYEES_DB[current_user]["role"] == "manager":
        dname = EMPLOYEES_DB[current_user]["department"]
    else:
        # admin can pick any dept or "ALL"
        dname = input("Enter department name or 'ALL' to see all: ").strip()

    print("\n=== Monthly Payroll ===")
    if dname == "ALL" and EMPLOYEES_DB[current_user]["role"] == "admin":
        # All employees
        for uname, data in EMPLOYEES_DB.items():
            if data["role"] == "admin":
                continue
            monthly_pay = data["salary"] / 12
            print(f"Employee: {uname} ({data['name']}), Monthly Pay: ${monthly_pay:.2f}")
    elif dname and dname in DEPARTMENTS_DB:
        # List employees in that dept
        for uname in DEPARTMENTS_DB[dname]["employees"]:
            data = EMPLOYEES_DB[uname]
            monthly_pay = data["salary"] / 12
            print(f"Employee: {uname} ({data['name']}), Monthly Pay: ${monthly_pay:.2f}")
    else:
        # Manager approach (their dept)
        if not dname:
            # manager
            dname = EMPLOYEES_DB[current_user]["department"]
        if dname not in DEPARTMENTS_DB:
            print("No such dept. Cancelling.")
            return
        for uname in DEPARTMENTS_DB[dname]["employees"]:
            data = EMPLOYEES_DB[uname]
            monthly_pay = data["salary"] / 12
            print(f"Employee: {uname} ({data['name']}), Monthly Pay: ${monthly_pay:.2f}")


# =============================================================================
#                 NORMAL USER FEATURES
# =============================================================================

@login_required
def clock_in():
    """User clocks in - records timestamp. If already clocked in, do nothing."""
    logs = EMPLOYEES_DB[current_user]["time_logs"]
    if logs and not logs[-1].get("clock_out"):
        print("You are already clocked in. Clock out first.")
        return
    logs.append({"clock_in": str(datetime.now()), "clock_out": None})
    print(f"Clock-in recorded at {logs[-1]['clock_in']}.")


@login_required
def clock_out():
    """User clocks out - must have a prior clock_in without clock_out."""
    logs = EMPLOYEES_DB[current_user]["time_logs"]
    if not logs or logs[-1].get("clock_out"):
        print("You are not currently clocked in.")
        return
    logs[-1]["clock_out"] = str(datetime.now())
    print(f"Clock-out recorded at {logs[-1]['clock_out']}.")


@login_required
def view_my_shifts():
    """User sees their assigned shifts."""
    shifts = EMPLOYEES_DB[current_user]["shifts"]
    if not shifts:
        print("No shifts assigned.")
        return
    print("\n=== Your Upcoming Shifts ===")
    for s in shifts:
        print(f"Date: {s['date']}, {s['start']}-{s['end']}")

@login_required
def view_my_projects():
    """User sees which projects they are assigned to."""
    projects = EMPLOYEES_DB[current_user]["projects"]
    if not projects:
        print("No projects assigned yet.")
    else:
        print("\n=== Your Projects ===")
        for p in projects:
            print("-", p)

@login_required
def view_my_performance_notes():
    """User sees their performance notes."""
    notes = EMPLOYEES_DB[current_user]["performance_notes"]
    if not notes:
        print("No performance notes found.")
        return
    print("\n=== Your Performance Notes ===")
    for n in notes:
        print(f"{n['timestamp']} by {n['added_by']}: {n['note']}")


@login_required
def view_my_profile():
    data = EMPLOYEES_DB[current_user]
    print(f"\n=== Profile of {data['name']} (User: {current_user}, ID: {data['employee_id']}) ===")
    print(f"Role: {data['role']}, Dept: {data['department']}, Salary: ${data['salary']:.2f}, Active: {data['is_active']}")
    print(f"Location: {data['location'] or '--None--'}")
    print("")

@login_required
def change_my_password():
    """User changes their own password with old password check."""
    old_pw = input("Enter old password: ").strip()
    old_hashed = hash_password(old_pw)
    if EMPLOYEES_DB[current_user]["password"] != old_hashed:
        print("Incorrect old password.")
        return
    new_pw = input("Enter new password: ").strip()
    confirm = input("Confirm new password: ").strip()
    if new_pw != confirm:
        print("New password mismatch.")
        return
    EMPLOYEES_DB[current_user]["password"] = hash_password(new_pw)
    print("Password changed successfully.")

@login_required
def search_employees():
    """
    Basic search by name or department.
    Manager sees only employees in their dept. Admin sees all, normal user sees partial results.
    """
    term = input("Enter name or department to search: ").strip().lower()
    user_role = EMPLOYEES_DB[current_user]["role"]
    my_dept = EMPLOYEES_DB[current_user]["department"]

    results = []
    for uname, data in EMPLOYEES_DB.items():
        # If not active, skip or show anyway? We'll show them for admin or manager
        # but skip for normal user. Let's skip only if user is role= user
        if data["is_active"] is False and user_role == "user":
            continue

        # Basic match
        name_dept_string = f"{data['name'].lower()} {data['department'].lower() if data['department'] else ''}"
        if term in name_dept_string:
            # If manager, show only employees in manager’s dept
            if user_role == "manager":
                if data["department"] == my_dept:
                    results.append((uname, data['name'], data['department']))
            elif user_role == "admin":
                results.append((uname, data['name'], data['department']))
            else:
                # Normal user sees only partial data
                # but let's just add them
                results.append((uname, data['name'], data['department']))

    if not results:
        print("No matching employees found.")
    else:
        print("\n=== Search Results ===")
        for r in results:
            print(f"Username: {r[0]}, Name: {r[1]}, Dept: {r[2]}")


# =============================================================================
#                      MAIN MENU
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Employee Management System")
        print(f"Current User: {current_user if current_user else 'None'}")
        print("-----------------------------------------------------")
        print("1.  Login")
        print("2.  Logout")
        print("\n--- Admin-Only Features ---")
        print("3.  Create Employee")
        print("4.  Delete Employee")
        print("5.  Toggle Employee Active/Inactive")
        print("6.  View All Employees")
        print("7.  Create Department")
        print("8.  Delete Department")

        print("\n--- Manager & Admin Features ---")
        print("9.   Assign Manager to Department")
        print("10.  Assign Employee to Department")
        print("11.  Schedule Shift for Employee")
        print("12.  Add Performance Note")
        print("13.  Assign Project to Employee")
        print("14.  View Dept Time Logs")
        print("15.  Generate Monthly Payroll")

        print("\n--- Normal User Features ---")
        print("16.  Clock In")
        print("17.  Clock Out")
        print("18.  View My Shifts")
        print("19.  View My Projects")
        print("20.  View My Performance Notes")
        print("21.  View My Profile")
        print("22.  Change My Password")
        print("23.  Search Employees (Name or Dept)")
        print("\n24. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            login()
        elif choice == "2":
            logout()
        elif choice == "3":
            create_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            toggle_employee_active()
        elif choice == "6":
            view_all_employees()
        elif choice == "7":
            create_department()
        elif choice == "8":
            delete_department()
        elif choice == "9":
            assign_manager_to_dept()
        elif choice == "10":
            assign_employee_to_dept()
        elif choice == "11":
            schedule_shift()
        elif choice == "12":
            add_performance_note()
        elif choice == "13":
            assign_project()
        elif choice == "14":
            view_time_logs_dept()
        elif choice == "15":
            generate_monthly_payroll()
        elif choice == "16":
            clock_in()
        elif choice == "17":
            clock_out()
        elif choice == "18":
            view_my_shifts()
        elif choice == "19":
            view_my_projects()
        elif choice == "20":
            view_my_performance_notes()
        elif choice == "21":
            view_my_profile()
        elif choice == "22":
            change_my_password()
        elif choice == "23":
            search_employees()
        elif choice == "24":
            print("\nExiting Education Trust Nasra School - Employee Management System")
            break
        else:
            print("Invalid choice. Please try again.")


# =============================================================================
#                      ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main_menu()