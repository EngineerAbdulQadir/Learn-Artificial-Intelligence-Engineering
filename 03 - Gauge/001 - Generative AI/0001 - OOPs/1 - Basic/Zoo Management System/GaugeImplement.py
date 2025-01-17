import time
from functools import wraps

# =============================================================================
#                           HELPER FUNCTIONS
# =============================================================================

def timestamp() -> str:
    """Returns a nicely formatted timestamp."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")

def generate_animal_id() -> str:
    """Generate a simple, incremental ID for animals."""
    global ANIMAL_ID_COUNTER
    ANIMAL_ID_COUNTER += 1
    return f"A{ANIMAL_ID_COUNTER}"

# =============================================================================
#                       IN-MEMORY 'DATABASE'
# =============================================================================

"""
USER_DB structure:
{
  "<username>": {
    "password": str,
    "role": "admin"/"caretaker"/"veterinarian"/"visitor",
    "name": str,          # Full name
    "is_active": bool,
    "history": [ list of log strings ],
  }, ...
}

ANIMALS_DB structure:
{
  "<animal_id>": {
    "name": str,
    "species": str,
    "age": int,
    "enclosure": str,
    "health_records": [
      {"timestamp": "...", "notes": "Vet checkup", "vet": "username", "treatment": "..."}
    ],
    "feeding_schedule": {
      "time": "08:00, 14:00, etc." or a list,
      "caretaker": "username",
      "logs": [ {"timestamp": "...", "caretaker": "...", "notes": "..."} ]
    }
  }, ...
}

ENCLOSURES_DB structure:
{
  "<enclosure_name>": {
    "capacity": int,
    "location": str,
    "animals": [list of animal_ids]
  }, ...
}
"""

ANIMAL_ID_COUNTER = 1000

USER_DB = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "name": "System Administrator",
        "is_active": True,
        "history": ["System admin account created."]
    },
    "caretaker_carl": {
        "password": "caretaker123",
        "role": "caretaker",
        "name": "Carl the Caretaker",
        "is_active": True,
        "history": ["Joined as caretaker."]
    },
    "vet_vicky": {
        "password": "vet123",
        "role": "veterinarian",
        "name": "Vicky the Vet",
        "is_active": True,
        "history": ["Joined as veterinarian."]
    },
    "visitor_vanessa": {
        "password": "visitor123",
        "role": "visitor",
        "name": "Vanessa Visitor",
        "is_active": True,
        "history": ["Joined as visitor."]
    },
}

ANIMALS_DB = {
    "A1001": {
        "name": "Leo",
        "species": "Lion",
        "age": 5,
        "enclosure": "Savannah1",
        "health_records": [],
        "feeding_schedule": {
            "time": ["08:00", "14:00"],
            "caretaker": "caretaker_carl",
            "logs": []
        },
    },
    "A1002": {
        "name": "Ellie",
        "species": "Elephant",
        "age": 10,
        "enclosure": "ElephantArea",
        "health_records": [],
        "feeding_schedule": {
            "time": ["09:00", "15:00"],
            "caretaker": "caretaker_carl",
            "logs": []
        },
    },
}

ENCLOSURES_DB = {
    "Savannah1": {
        "capacity": 5,
        "location": "North Wing",
        "animals": ["A1001"]
    },
    "ElephantArea": {
        "capacity": 3,
        "location": "South Wing",
        "animals": ["A1002"]
    }
}

current_user = None

# =============================================================================
#                       DECORATORS
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
            print("Your account is inactive. Contact Admin.")
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

def caretaker_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global current_user
        if not current_user:
            print("You must be logged in first.")
            login()
            if not current_user:
                return
        if USER_DB[current_user]["role"] != "caretaker":
            print("Only caretakers can access this feature.")
            return
        return func(*args, **kwargs)
    return wrapper

def vet_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global current_user
        if not current_user:
            print("You must be logged in first.")
            login()
            if not current_user:
                return
        if USER_DB[current_user]["role"] != "veterinarian":
            print("Only veterinarians can access this feature.")
            return
        return func(*args, **kwargs)
    return wrapper

# =============================================================================
#                       AUTH & SESSION
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
#                       ADMIN FEATURES
# =============================================================================

@admin_required
def create_user():
    """Create a new user with a specified role."""
    uname = input("Enter new username: ").strip()
    if uname in USER_DB:
        print("That username already exists.")
        return
    role = input("Enter role (admin/caretaker/veterinarian/visitor) [default=visitor]: ").strip() or "visitor"
    name = input("Enter full name: ").strip()
    pw = input("Set password: ").strip()

    USER_DB[uname] = {
        "password": pw,
        "role": role.lower(),
        "name": name,
        "is_active": True,
        "history": [f"{timestamp()} Created user with role {role}."]
    }
    print(f"User '{uname}' created with role '{role}'.")

@admin_required
def toggle_user():
    """Toggle a user’s active/inactive status."""
    uname = input("Enter username to toggle status: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot deactivate the main admin.")
        return
    current_status = USER_DB[uname]["is_active"]
    USER_DB[uname]["is_active"] = not current_status
    new_status = "Active" if USER_DB[uname]["is_active"] else "Inactive"
    print(f"User '{uname}' is now {new_status}.")

@admin_required
def remove_user():
    """Completely remove a user from the system."""
    uname = input("Enter username to remove: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot remove the main admin.")
        return
    confirm = input("Are you sure? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return
    del USER_DB[uname]
    print(f"User '{uname}' removed from the system.")

@admin_required
def add_animal():
    """Add a new animal to the zoo."""
    a_name = input("Enter animal name: ").strip()
    a_species = input("Enter species: ").strip()
    a_age_str = input("Enter age (years): ").strip()
    try:
        a_age = int(a_age_str)
    except ValueError:
        a_age = 0
    encl = input("Enter enclosure name: ").strip()
    if encl not in ENCLOSURES_DB:
        # Possibly create a new enclosure
        create_it = input(f"Enclosure '{encl}' not found. Create it? [yes/no]: ").strip().lower()
        if create_it == "yes":
            ENCLOSURES_DB[encl] = {
                "capacity": 5,  # default capacity
                "location": "Unknown",
                "animals": []
            }
        else:
            encl = None

    new_id = generate_animal_id()
    ANIMALS_DB[new_id] = {
        "name": a_name,
        "species": a_species,
        "age": a_age,
        "enclosure": encl,
        "health_records": [],
        "feeding_schedule": {
            "time": [],
            "caretaker": None,
            "logs": []
        },
    }
    if encl and encl in ENCLOSURES_DB:
        ENCLOSURES_DB[encl]["animals"].append(new_id)

    print(f"Animal '{a_name}' (ID={new_id}) added to the zoo.")

@admin_required
def remove_animal():
    """Remove an animal from the zoo."""
    aid = input("Enter Animal ID to remove: ").strip()
    if aid not in ANIMALS_DB:
        print("No such animal.")
        return
    confirm = input(f"Are you sure you want to remove Animal {aid}? [yes/no]: ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return

    # Remove from enclosure
    old_enclosure = ANIMALS_DB[aid]["enclosure"]
    if old_enclosure and old_enclosure in ENCLOSURES_DB:
        if aid in ENCLOSURES_DB[old_enclosure]["animals"]:
            ENCLOSURES_DB[old_enclosure]["animals"].remove(aid)

    del ANIMALS_DB[aid]
    print(f"Animal {aid} removed from the zoo.")

@admin_required
def view_all_animals():
    """Admin can view all animals with details."""
    if not ANIMALS_DB:
        print("No animals in the zoo.")
        return
    print("\n=== All Zoo Animals ===")
    for aid, data in ANIMALS_DB.items():
        print(f"ID: {aid}, Name: {data['name']}, Species: {data['species']}, "
              f"Age: {data['age']}, Enclosure: {data['enclosure']}")
    print("")

@admin_required
def manage_enclosures():
    """View or create enclosures, see capacity, etc."""
    choice = input("Create new enclosure (c) or view (v)? ").strip().lower()
    if choice == "c":
        ename = input("Enter new enclosure name: ").strip()
        if ename in ENCLOSURES_DB:
            print("That enclosure already exists.")
            return
        cap_str = input("Enter capacity (default=5): ").strip()
        loc = input("Enter location (optional): ").strip() or "Unknown"
        try:
            cap = int(cap_str) if cap_str else 5
        except ValueError:
            cap = 5
        ENCLOSURES_DB[ename] = {
            "capacity": cap,
            "location": loc,
            "animals": []
        }
        print(f"Enclosure '{ename}' created, capacity={cap}, location='{loc}'.")
    else:
        # view
        if not ENCLOSURES_DB:
            print("No enclosures defined.")
            return
        print("\n=== Enclosures ===")
        for e, info in ENCLOSURES_DB.items():
            animals = info["animals"]
            print(f"Name: {e}, Capacity={info['capacity']}, Location={info['location']}, "
                  f"Animals={animals if animals else []}")

@admin_required
def view_all_users():
    """Admin sees all users and their roles/status."""
    print("\n=== All Users ===")
    for uname, data in USER_DB.items():
        print(f"Username: {uname}, Role: {data['role']}, Active: {data['is_active']}, Name: {data['name']}")

# =============================================================================
#                     CARETAKER FEATURES
# =============================================================================

@caretaker_required
def set_feeding_schedule():
    """Assign or update an animal's feeding schedule and caretaker."""
    aid = input("Enter Animal ID to set feeding schedule for: ").strip()
    if aid not in ANIMALS_DB:
        print("No such animal.")
        return
    # caretaker can only schedule if they are caretaker of that animal or if no caretaker set
    # For simplicity, let's allow caretaker to set caretaker to themselves
    times_str = input("Enter feeding times (comma separated, e.g. '08:00,14:00'): ").strip()
    times_list = [t.strip() for t in times_str.split(",")] if times_str else []
    ANIMALS_DB[aid]["feeding_schedule"]["time"] = times_list
    ANIMALS_DB[aid]["feeding_schedule"]["caretaker"] = current_user
    print(f"Feeding schedule updated for Animal {aid}. Times: {times_list}")

@caretaker_required
def record_feeding():
    """Caretaker records a feeding event for an animal."""
    aid = input("Enter Animal ID you fed: ").strip()
    if aid not in ANIMALS_DB:
        print("No such animal.")
        return
    # Check caretaker
    caretaker_assigned = ANIMALS_DB[aid]["feeding_schedule"].get("caretaker", None)
    if caretaker_assigned and caretaker_assigned != current_user:
        print("You are not the assigned caretaker for this animal.")
        return

    notes = input("Enter feeding notes (optional): ").strip()
    log_entry = {
        "timestamp": timestamp(),
        "caretaker": current_user,
        "notes": notes
    }
    ANIMALS_DB[aid]["feeding_schedule"]["logs"].append(log_entry)
    print(f"Feeding recorded for Animal {aid} at {log_entry['timestamp']}.")

@caretaker_required
def view_my_assigned_animals():
    """Caretaker sees which animals they’re assigned to feed."""
    assigned = []
    for aid, data in ANIMALS_DB.items():
        fsched = data["feeding_schedule"]
        if fsched["caretaker"] == current_user:
            assigned.append(aid)
    if not assigned:
        print("You are not assigned to any animals yet.")
        return
    print("\n=== Your Assigned Animals ===")
    for aid in assigned:
        adata = ANIMALS_DB[aid]
        print(f"ID: {aid}, Name: {adata['name']}, Species: {adata['species']}, "
              f"Feeding times: {adata['feeding_schedule']['time']}")
    print("")

# =============================================================================
#                    VETERINARIAN FEATURES
# =============================================================================

@vet_required
def add_health_record():
    """Vet writes a health/treatment record for an animal."""
    aid = input("Enter Animal ID for health record: ").strip()
    if aid not in ANIMALS_DB:
        print("No such animal.")
        return
    notes = input("Enter health notes: ").strip()
    treatment = input("Enter any treatment/medication (optional): ").strip()
    rec = {
        "timestamp": timestamp(),
        "notes": notes,
        "vet": current_user,
        "treatment": treatment
    }
    ANIMALS_DB[aid]["health_records"].append(rec)
    print(f"Health record added for Animal {aid}.")

@vet_required
def view_animal_health():
    """Vet views health records of an animal."""
    aid = input("Enter Animal ID: ").strip()
    if aid not in ANIMALS_DB:
        print("No such animal.")
        return
    recs = ANIMALS_DB[aid]["health_records"]
    if not recs:
        print("No health records found for this animal.")
        return
    print(f"\n=== Health Records for Animal {aid} ({ANIMALS_DB[aid]['name']}) ===")
    for r in recs:
        print(f"{r['timestamp']} by {r['vet']}: {r['notes']}, Treatment: {r['treatment']}")

# =============================================================================
#                  VISITOR & GENERAL VIEW
# =============================================================================

@login_required
def visitor_view_animals():
    """A visitor can see a limited list of animals with basic info."""
    print("\n=== Zoo Animal List (Basic Info) ===")
    for aid, data in ANIMALS_DB.items():
        print(f"ID: {aid}, Name: {data['name']}, Species: {data['species']}")
    print("")

def visitor_animal_details():
    """Visitor can optionally see more details on a single animal, albeit limited."""
    aid = input("Enter Animal ID to view details: ").strip()
    if aid not in ANIMALS_DB:
        print("No such animal.")
        return
    data = ANIMALS_DB[aid]
    # limited info, no health records
    print(f"\n=== Animal {aid} ===")
    print(f"Name: {data['name']}, Species: {data['species']}, Age: {data['age']}, Enclosure: {data['enclosure']}")

# =============================================================================
#                     MAIN MENU
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Zoo Mangement System")
        print(f"Current User: {current_user if current_user else 'None'}")
        print("-------------------------------------------")
        print("1.  Login")
        print("2.  Logout")

        print("\n-- Admin Features --")
        print("3.  Create User")
        print("4.  Toggle User Active/Inactive")
        print("5.  Remove User")
        print("6.  Add Animal to Zoo")
        print("7.  Remove Animal from Zoo")
        print("8.  View All Animals")
        print("9.  Manage Enclosures")
        print("10. View All Users")

        print("\n-- Caretaker Features --")
        print("11. Set/Update Feeding Schedule")
        print("12. Record Feeding")
        print("13. View My Assigned Animals")

        print("\n-- Veterinarian Features --")
        print("14. Add Health Record")
        print("15. View Animal Health Records")

        print("\n-- Visitor/General --")
        print("16. View Animal List (Basic Info)")
        print("17. Animal Details (Limited)")

        print("\n18. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            login()
        elif choice == "2":
            logout()
        elif choice == "3":
            create_user()
        elif choice == "4":
            toggle_user()
        elif choice == "5":
            remove_user()
        elif choice == "6":
            add_animal()
        elif choice == "7":
            remove_animal()
        elif choice == "8":
            view_all_animals()
        elif choice == "9":
            manage_enclosures()
        elif choice == "10":
            view_all_users()
        elif choice == "11":
            set_feeding_schedule()
        elif choice == "12":
            record_feeding()
        elif choice == "13":
            view_my_assigned_animals()
        elif choice == "14":
            add_health_record()
        elif choice == "15":
            view_animal_health()
        elif choice == "16":
            visitor_view_animals()
        elif choice == "17":
            visitor_animal_details()
        elif choice == "18":
            print("\nExiting Education Trust Nasra School - Zoo Mangement System")
            break
        else:
            print("Invalid choice. Please try again.")

# =============================================================================
#                  SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main_menu()