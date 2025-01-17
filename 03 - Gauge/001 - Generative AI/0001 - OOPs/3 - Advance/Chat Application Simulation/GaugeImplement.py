import time
from functools import wraps

# =============================================================================
#                           HELPER FUNCTIONS
# =============================================================================

def timestamp() -> str:
    """Returns a nicely formatted timestamp string."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")

# =============================================================================
#                       IN-MEMORY 'DATABASE'
# =============================================================================

"""
USER_DB structure:
{
  "<username>": {
    "password": str,
    "role": "admin"/"user",
    "name": str,              # Full display name
    "is_active": bool,
    "history": [list of event logs],
    "rooms_joined": set([room_name, ...])  # list of chat rooms the user joined
  }, ...
}

ROOMS_DB structure:
{
  "<room_name>": {
    "owner": <username> or None,    # user that created the room (or admin)
    "members": set([username, ...]),
    "messages": [
       {
         "timestamp": str,
         "sender": <username>,
         "text": str
       }, ...
    ]
  }, ...
}

DIRECT_MESSAGES structure:
{
  (userA, userB) (sorted tuple of user names): [
    {
      "timestamp": "...",
      "sender": <username>,
      "text": str
    },
    ...
  ],
  ...
}
"""

USER_DB = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "name": "System Admin",
        "is_active": True,
        "history": ["Admin account created."],
        "rooms_joined": set()
    },
    "alice": {
        "password": "alice123",
        "role": "user",
        "name": "Alice Example",
        "is_active": True,
        "history": ["User account created."],
        "rooms_joined": set()
    }
}

ROOMS_DB = {}
DIRECT_MESSAGES = {}

current_user = None

# =============================================================================
#                        DECORATORS
# =============================================================================

def login_required(func):
    """Ensures a user is logged in (and active) before accessing a feature."""
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
    return wraps(func)(wrapper)

def admin_required(func):
    """Ensures only admin can access certain features."""
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
    return wraps(func)(wrapper)

# =============================================================================
#                  AUTH & SESSION
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
        "history": [f"{timestamp()} Created user with role {role}."],
        "rooms_joined": set()
    }
    print(f"User '{uname}' created with role '{role}'.")

@admin_required
def toggle_user_status():
    """Activate or deactivate a user's account."""
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
    """Remove a user from the system entirely."""
    uname = input("Enter username to remove: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot remove the main admin.")
        return
    confirm = input(f"Are you sure you want to remove '{uname}'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return
    # Optionally handle direct messages or rooms
    del USER_DB[uname]
    print(f"User '{uname}' removed from system.")

@admin_required
def view_all_users():
    """Admin sees all users, their roles, and statuses."""
    print("\n=== All Users ===")
    for uname, data in USER_DB.items():
        print(f"Username: {uname}, Role: {data['role']}, Active: {data['is_active']}, Name: {data['name']}")
    print("")

@admin_required
def view_all_rooms():
    """Admin can see all rooms, owners, and members."""
    if not ROOMS_DB:
        print("No rooms created yet.")
        return
    print("\n=== All Chat Rooms ===")
    for rname, rdata in ROOMS_DB.items():
        print(f"Room: {rname}, Owner: {rdata['owner']}, Members: {', '.join(rdata['members'])}")

# =============================================================================
#                    ROOM & GROUP CHAT FEATURES
# =============================================================================

@login_required
def create_room():
    """Create a new chat room. The current user becomes the owner."""
    rname = input("Enter room name: ").strip()
    if not rname:
        print("Invalid room name.")
        return
    if rname in ROOMS_DB:
        print("That room name already exists.")
        return

    ROOMS_DB[rname] = {
        "owner": current_user,
        "members": set([current_user]),
        "messages": []
    }
    USER_DB[current_user]["rooms_joined"].add(rname)
    print(f"Room '{rname}' created. You are the owner and first member.")

@login_required
def join_room():
    """User joins an existing room."""
    rname = input("Enter room name to join: ").strip()
    if rname not in ROOMS_DB:
        print("No such room.")
        return
    ROOMS_DB[rname]["members"].add(current_user)
    USER_DB[current_user]["rooms_joined"].add(rname)
    print(f"You have joined room '{rname}'.")

@login_required
def leave_room():
    """User leaves a room they're a member of."""
    rname = input("Enter room name to leave: ").strip()
    if rname not in ROOMS_DB:
        print("No such room.")
        return
    if current_user not in ROOMS_DB[rname]["members"]:
        print("You are not a member of this room.")
        return
    ROOMS_DB[rname]["members"].remove(current_user)
    if rname in USER_DB[current_user]["rooms_joined"]:
        USER_DB[current_user]["rooms_joined"].remove(rname)
    print(f"You have left room '{rname}'.")

@login_required
def post_message_room():
    """Post a message to a room if user is a member."""
    rname = input("Enter room name to post in: ").strip()
    if rname not in ROOMS_DB:
        print("No such room.")
        return
    if current_user not in ROOMS_DB[rname]["members"]:
        print("You are not a member of this room.")
        return
    msg = input("Enter your message: ").strip()
    if not msg:
        print("Empty message. Cancelled.")
        return
    ROOMS_DB[rname]["messages"].append({
        "timestamp": timestamp(),
        "sender": current_user,
        "text": msg
    })
    print("Message posted.")

@login_required
def view_room_messages():
    """View the messages in a specific room (if user is a member)."""
    rname = input("Enter room name to view messages: ").strip()
    if rname not in ROOMS_DB:
        print("No such room.")
        return
    if current_user not in ROOMS_DB[rname]["members"]:
        print("You are not a member of this room.")
        return
    msgs = ROOMS_DB[rname]["messages"]
    if not msgs:
        print("No messages yet in this room.")
        return
    print(f"\n=== Messages in Room '{rname}' ===")
    for m in msgs:
        print(f"{m['timestamp']} - {m['sender']}: {m['text']}")
    print("")

@login_required
def kick_user_from_room():
    """
    Room owner (or admin) can remove a user from their room.
    """
    rname = input("Enter room name: ").strip()
    if rname not in ROOMS_DB:
        print("No such room.")
        return
    # check if current user is room owner or admin
    if USER_DB[current_user]["role"] != "admin" and ROOMS_DB[rname]["owner"] != current_user:
        print("Only the room owner or an admin can kick users from this room.")
        return
    target_user = input("Enter username to kick out: ").strip()
    if target_user not in USER_DB:
        print("No such user in system.")
        return
    if target_user not in ROOMS_DB[rname]["members"]:
        print("That user is not in this room.")
        return
    ROOMS_DB[rname]["members"].remove(target_user)
    if rname in USER_DB[target_user]["rooms_joined"]:
        USER_DB[target_user]["rooms_joined"].remove(rname)
    print(f"User '{target_user}' has been removed from room '{rname}'.")

# =============================================================================
#                  DIRECT MESSAGE FEATURES
# =============================================================================

@login_required
def send_direct_message():
    """Send a direct (private) message to another user."""
    target_user = input("Enter username to send DM: ").strip()
    if target_user not in USER_DB:
        print("No such user in system.")
        return
    if not USER_DB[target_user]["is_active"]:
        print("That user is inactive.")
        return
    msg = input("Enter message: ").strip()
    if not msg:
        print("Empty message. Cancelled.")
        return

    # Store in DIRECT_MESSAGES with a sorted tuple key
    key = tuple(sorted([current_user, target_user]))
    if key not in DIRECT_MESSAGES:
        DIRECT_MESSAGES[key] = []
    DIRECT_MESSAGES[key].append({
        "timestamp": timestamp(),
        "sender": current_user,
        "text": msg
    })
    print(f"Message sent to user '{target_user}'.")

@login_required
def view_direct_messages():
    """View direct messages between the current user and another user."""
    other_user = input("Enter username to view DM with: ").strip()
    if other_user not in USER_DB:
        print("No such user in system.")
        return
    key = tuple(sorted([current_user, other_user]))
    if key not in DIRECT_MESSAGES or not DIRECT_MESSAGES[key]:
        print("No direct messages found between you and that user.")
        return
    print(f"\n=== Direct Messages with {other_user} ===")
    for m in DIRECT_MESSAGES[key]:
        print(f"{m['timestamp']} - {m['sender']}: {m['text']}")
    print("")

# =============================================================================
#                       MAIN MENU
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Chat Application Simulation")
        print(f"Current User: {current_user if current_user else 'None'}")
        print("-----------------------------------------")
        print("1.  Login")
        print("2.  Logout")

        print("\n-- Admin Features --")
        print("3.  Create User")
        print("4.  Toggle User Status")
        print("5.  Remove User")
        print("6.  View All Users")
        print("7.  View All Rooms (Admin)")

        print("\n-- Room / Group Chat Features --")
        print("8.  Create Room")
        print("9.  Join Room")
        print("10. Leave Room")
        print("11. Post Message to Room")
        print("12. View Room Messages")
        print("13. Kick User from Room (owner/admin)")

        print("\n-- Direct Messaging --")
        print("14. Send Direct Message")
        print("15. View Direct Messages")

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
            view_all_rooms()
        elif choice == "8":
            create_room()
        elif choice == "9":
            join_room()
        elif choice == "10":
            leave_room()
        elif choice == "11":
            post_message_room()
        elif choice == "12":
            view_room_messages()
        elif choice == "13":
            kick_user_from_room()
        elif choice == "14":
            send_direct_message()
        elif choice == "15":
            view_direct_messages()
        elif choice == "16":
            print("\nExiting Education Trust Nasra School - Chat Application Simulation")
            break
        else:
            print("Invalid choice. Please try again.")

# =============================================================================
#                      SCRIPT ENTRY
# =============================================================================

if __name__ == "__main__":
    main_menu()