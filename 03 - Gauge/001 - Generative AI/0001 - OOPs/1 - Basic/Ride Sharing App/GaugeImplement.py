import time
import random
from functools import wraps

# =============================================================================
#                           HELPER FUNCTIONS
# =============================================================================

def timestamp():
    """Returns a nicely formatted timestamp string."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")

def generate_ride_id() -> str:
    """Generate a simple unique ride ID."""
    global RIDE_ID_COUNTER
    RIDE_ID_COUNTER += 1
    return f"R{RIDE_ID_COUNTER}"

def approximate_fare(distance_km: float, base_fare=5.0, per_km_rate=2.0) -> float:
    """
    A simple fare approximation:
      total_fare = base_fare + (distance_km * per_km_rate)
    """
    return base_fare + (distance_km * per_km_rate)


# =============================================================================
#                        IN-MEMORY 'DATABASE'
# =============================================================================

"""
USER_DB structure (dict):
{
  "<username>": {
    "password": "pass123",
    "role": "rider"/"driver"/"admin",
    "name": "Full Name",
    "is_active": True/False,
    "rating": float (average rating),
    "num_ratings": int (to compute average),
    "history": [strings of event logs],
    "driver_info": {
      "vehicle": "Car Model/Plate",
      "online": bool,       # True if driver is accepting rides
      "location": (lat, lon) or None,  # in a real app, stored or updated
    },
    "rider_info": {
      "payment_method": "Cash/Wallet/Card",  # demonstration
      "location": (lat, lon) or None,
    },
  }, ...
}

RIDES_DB structure (dict):
{
  "<ride_id>": {
    "rider": <username>,
    "driver": <username> or None,
    "pickup": "Location string or (lat,lon)",
    "dropoff": "Location string or (lat,lon)",
    "distance_km": float,
    "fare": float,
    "status": "requested"/"accepted"/"ongoing"/"completed"/"cancelled",
    "timestamp": "time string",
    "rider_rating": None or float,
    "driver_rating": None or float,
    "paid": bool
  }, ...
}
"""

RIDE_ID_COUNTER = 1000

USER_DB = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "name": "System Admin",
        "is_active": True,
        "rating": 0.0,
        "num_ratings": 0,
        "history": [],
        "driver_info": None,
        "rider_info": None
    },
    "driver_alex": {
        "password": "driver123",
        "role": "driver",
        "name": "Alex Driver",
        "is_active": True,
        "rating": 4.5,
        "num_ratings": 2,
        "history": ["[2023-01-01 12:00] Joined as driver."],
        "driver_info": {
            "vehicle": "Toyota Corolla AB-1234",
            "online": False,
            "location": None,
        },
        "rider_info": None
    },
    "rider_jane": {
        "password": "rider123",
        "role": "rider",
        "name": "Jane Rider",
        "is_active": True,
        "rating": 4.9,
        "num_ratings": 3,
        "history": ["[2023-01-02 09:00] Joined as rider."],
        "driver_info": None,
        "rider_info": {
            "payment_method": "Cash",
            "location": None,
        }
    }
}

RIDES_DB = {}

current_user = None


# =============================================================================
#                        DECORATORS
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
#                       AUTH & SESSION
# =============================================================================

def login():
    global current_user
    uname = input("Enter username: ").strip()
    if uname not in USER_DB:
        print("No such username.")
        return
    if not USER_DB[uname]["is_active"]:
        print("This account is inactive. Contact admin.")
        return
    pw = input("Enter password: ").strip()
    if pw == USER_DB[uname]["password"]:
        current_user = uname
        print(f"\nWelcome {USER_DB[uname]['name']} ({uname})! You are logged in as {USER_DB[uname]['role']}.")
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
#                        ADMIN FEATURES
# =============================================================================

@admin_required
def create_user():
    """Create a new user (driver, rider, or admin)."""
    uname = input("Enter new username: ").strip()
    if uname in USER_DB:
        print("That username already exists.")
        return
    role = input("Enter role (admin/driver/rider) [default=rider]: ").strip() or "rider"
    name = input("Enter full name: ").strip()
    pw = input("Set password: ").strip()

    USER_DB[uname] = {
        "password": pw,
        "role": role.lower(),
        "name": name,
        "is_active": True,
        "rating": 0.0,
        "num_ratings": 0,
        "history": [f"{timestamp()} Account created as {role}."],
        "driver_info": None,
        "rider_info": None
    }
    if role.lower() == "driver":
        vehicle = input("Enter vehicle info (e.g. 'Honda Civic XY-9999'): ").strip()
        USER_DB[uname]["driver_info"] = {
            "vehicle": vehicle,
            "online": False,
            "location": None,
        }
    elif role.lower() == "rider":
        payment = input("Enter payment method (Cash/Wallet/Card): ").strip() or "Cash"
        USER_DB[uname]["rider_info"] = {
            "payment_method": payment,
            "location": None,
        }

    print(f"User '{uname}' created with role '{role}'.")

@admin_required
def toggle_user_status():
    """Activate/deactivate an existing user."""
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
    """Remove user from the system entirely."""
    uname = input("Enter username to remove: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot remove the main admin.")
        return
    confirm = input(f"Are you sure? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return
    del USER_DB[uname]
    print(f"User '{uname}' removed from the system.")

@admin_required
def view_all_rides():
    """Admin can view all rides in the system."""
    if not RIDES_DB:
        print("No rides in the system yet.")
        return
    print("\n=== All Rides ===")
    for rid, data in RIDES_DB.items():
        print(f"Ride ID: {rid}, Rider: {data['rider']}, Driver: {data['driver']}, "
              f"Status: {data['status']}, Fare: ${data['fare']:.2f}, Paid: {data['paid']}")

@admin_required
def view_all_users():
    """Admin sees all users with their roles and status."""
    print("\n=== All Users ===")
    for uname, uinfo in USER_DB.items():
        print(f"Username: {uname}, Role: {uinfo['role']}, Active: {uinfo['is_active']}, "
              f"Rating: {uinfo['rating']:.1f}")


# =============================================================================
#                   DRIVER FEATURES
# =============================================================================

@login_required
def set_driver_online():
    """Driver sets themselves online to accept rides."""
    global current_user
    if USER_DB[current_user]["role"] != "driver":
        print("You are not a driver.")
        return
    USER_DB[current_user]["driver_info"]["online"] = True
    print("You are now ONLINE and available for rides.")

@login_required
def set_driver_offline():
    """Driver sets themselves offline."""
    global current_user
    if USER_DB[current_user]["role"] != "driver":
        print("You are not a driver.")
        return
    USER_DB[current_user]["driver_info"]["online"] = False
    print("You are now OFFLINE.")

@login_required
def view_ride_requests():
    """Driver sees all rides with 'requested' status (for demonstration, real matching is more complex)."""
    global current_user
    if USER_DB[current_user]["role"] != "driver":
        print("You are not a driver.")
        return
    open_rides = [ (rid, data) for rid, data in RIDES_DB.items() if data["status"] == "requested" ]
    if not open_rides:
        print("No open ride requests.")
        return

    print("\n=== Open Ride Requests ===")
    for rid, data in open_rides:
        print(f"Ride ID: {rid}, Rider: {data['rider']}, Pickup: {data['pickup']}, Dropoff: {data['dropoff']}, "
              f"Estimated Fare: ${data['fare']:.2f}")

    # Optionally: the driver can choose to accept one
    choice = input("Enter Ride ID to accept or press Enter to skip: ").strip()
    if not choice:
        print("No ride accepted.")
        return
    if choice not in RIDES_DB or RIDES_DB[choice]["status"] != "requested":
        print("Invalid or non-requested ride ID.")
        return
    # Accept
    RIDES_DB[choice]["driver"] = current_user
    RIDES_DB[choice]["status"] = "accepted"
    print(f"You accepted ride {choice}.")

@login_required
def view_my_assigned_rides():
    """Driver sees rides assigned to them that are not completed or cancelled."""
    global current_user
    if USER_DB[current_user]["role"] != "driver":
        print("You are not a driver.")
        return
    assigned_rides = [(rid, data) for rid, data in RIDES_DB.items()
                      if data["driver"] == current_user and data["status"] in ("accepted", "ongoing")]
    if not assigned_rides:
        print("No active rides assigned.")
        return
    print("\n=== Your Active Rides ===")
    for rid, data in assigned_rides:
        print(f"Ride ID: {rid}, Rider: {data['rider']}, Status: {data['status']}, "
              f"Fare: ${data['fare']:.2f}, Paid: {data['paid']}")

    # Optionally move a ride from 'accepted' to 'ongoing' or complete it
    choice = input("Enter Ride ID to start or complete. Leave blank to skip: ").strip()
    if not choice:
        return
    if choice not in RIDES_DB:
        print("Invalid ride ID.")
        return
    rdata = RIDES_DB[choice]
    if rdata["driver"] != current_user:
        print("That ride isn't assigned to you.")
        return
    if rdata["status"] == "accepted":
        # Start ride
        rdata["status"] = "ongoing"
        print(f"Ride {choice} is now ONGOING.")
    elif rdata["status"] == "ongoing":
        # Complete ride
        rdata["status"] = "completed"
        print(f"Ride {choice} is now COMPLETED.")
    else:
        print("That ride is not in a state you can change.")


# =============================================================================
#                   RIDER FEATURES
# =============================================================================

@login_required
def request_ride():
    """Rider requests a new ride by entering pickup and dropoff location. Driver assignment is simplistic here."""
    global current_user
    if USER_DB[current_user]["role"] != "rider":
        print("You are not a rider.")
        return
    pickup = input("Enter pickup location: ").strip()
    dropoff = input("Enter dropoff location: ").strip()
    # Fake distance
    distance_km = random.uniform(1.0, 15.0)
    fare_est = approximate_fare(distance_km)
    ride_id = generate_ride_id()
    RIDES_DB[ride_id] = {
        "rider": current_user,
        "driver": None,
        "pickup": pickup,
        "dropoff": dropoff,
        "distance_km": distance_km,
        "fare": fare_est,
        "status": "requested",
        "timestamp": timestamp(),
        "rider_rating": None,
        "driver_rating": None,
        "paid": False
    }
    print(f"Ride requested successfully with ID {ride_id}, estimated fare ${fare_est:.2f}. Waiting for driver acceptance.")

@login_required
def view_my_rides():
    """Rider sees their rides."""
    global current_user
    if USER_DB[current_user]["role"] != "rider":
        print("You are not a rider.")
        return
    my_rides = [(rid, data) for rid, data in RIDES_DB.items() if data["rider"] == current_user]
    if not my_rides:
        print("No rides found.")
        return

    print("\n=== My Rides ===")
    for rid, data in my_rides:
        print(f"RideID: {rid}, Driver: {data['driver']}, Status: {data['status']}, "
              f"Fare: ${data['fare']:.2f}, Paid: {data['paid']}")

    # Optionally, pay for a completed ride or rate
    choice = input("Enter Ride ID to pay or rate, or blank to skip: ").strip()
    if not choice:
        return
    if choice not in RIDES_DB:
        print("Invalid ride ID.")
        return
    rdata = RIDES_DB[choice]
    if rdata["rider"] != current_user:
        print("That’s not your ride.")
        return
    if rdata["status"] == "completed":
        # Payment or rating
        if not rdata["paid"]:
            do_pay = input("Pay for this ride now? (yes/no): ").strip().lower()
            if do_pay == "yes":
                rdata["paid"] = True
                print("Payment successful. Thank you!")
        # Rate driver
        if rdata["driver"]:
            rating_str = input("Rate your driver (1.0 - 5.0) or blank to skip: ").strip()
            if rating_str:
                try:
                    rating_val = float(rating_str)
                    if 1.0 <= rating_val <= 5.0:
                        rdata["driver_rating"] = rating_val
                        # Update driver’s rating in DB
                        duser = rdata["driver"]
                        old_sum = USER_DB[duser]["rating"] * USER_DB[duser]["num_ratings"]
                        new_sum = old_sum + rating_val
                        USER_DB[duser]["num_ratings"] += 1
                        USER_DB[duser]["rating"] = new_sum / USER_DB[duser]["num_ratings"]
                        print("Driver rated successfully.")
                    else:
                        print("Invalid rating range.")
                except ValueError:
                    print("Invalid rating input.")
    else:
        print("Ride is not completed. You cannot pay or rate yet.")


# =============================================================================
#                     RATING DRIVERS -> RATING RIDERS
# =============================================================================
@login_required
def rate_rider():
    """
    For a driver to rate a rider after a completed ride.
    """
    global current_user
    if USER_DB[current_user]["role"] != "driver":
        print("You are not a driver.")
        return
    # Show completed rides assigned to this driver
    completed_rides = [(rid, data) for rid, data in RIDES_DB.items()
                       if data["driver"] == current_user and data["status"] == "completed"]
    if not completed_rides:
        print("No completed rides to rate riders from.")
        return
    print("\n=== Completed Rides ===")
    for rid, rdata in completed_rides:
        print(f"RideID: {rid}, Rider: {rdata['rider']}, Rider Rating: {rdata['rider_rating']}")

    choice = input("Enter Ride ID to rate rider or blank to skip: ").strip()
    if not choice:
        return
    if choice not in RIDES_DB:
        print("Invalid ride ID.")
        return
    ride_info = RIDES_DB[choice]
    if ride_info["driver"] != current_user or ride_info["status"] != "completed":
        print("You can only rate from your own completed rides.")
        return
    # Rate rider
    rating_str = input("Rate the rider (1.0 - 5.0): ").strip()
    try:
        rating_val = float(rating_str)
        if 1.0 <= rating_val <= 5.0:
            ride_info["rider_rating"] = rating_val
            ruser = ride_info["rider"]
            old_sum = USER_DB[ruser]["rating"] * USER_DB[ruser]["num_ratings"]
            new_sum = old_sum + rating_val
            USER_DB[ruser]["num_ratings"] += 1
            USER_DB[ruser]["rating"] = new_sum / USER_DB[ruser]["num_ratings"]
            print("Rider rated successfully.")
        else:
            print("Invalid rating range.")
    except ValueError:
        print("Invalid rating input.")


# =============================================================================
#                      MAIN MENU
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Ride Sharing App")
        print(f"Current User: {current_user if current_user else 'None'}")
        print("--------------------------------------------")
        print("1.  Login")
        print("2.  Logout\n")

        print("-- Admin Features --")
        print("3.  Create User")
        print("4.  Toggle User Status")
        print("5.  Remove User")
        print("6.  View All Rides")
        print("7.  View All Users")

        print("\n-- Driver Features --")
        print("8.  Go Online")
        print("9.  Go Offline")
        print("10. View Ride Requests (Accept)")
        print("11. View My Assigned Rides (Start/Complete)")
        print("12. Rate Rider")

        print("\n-- Rider Features --")
        print("13. Request Ride")
        print("14. View My Rides (Pay/Rate)")

        print("\n15. Exit")

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
            view_all_rides()
        elif choice == "7":
            view_all_users()
        elif choice == "8":
            set_driver_online()
        elif choice == "9":
            set_driver_offline()
        elif choice == "10":
            view_ride_requests()
        elif choice == "11":
            view_my_assigned_rides()
        elif choice == "12":
            rate_rider()
        elif choice == "13":
            request_ride()
        elif choice == "14":
            view_my_rides()
        elif choice == "15":
            print("\nExiting the Education Trust Nasra School - Ride Sharing App")
            break
        else:
            print("Invalid choice. Please try again.")


# =============================================================================
#                   ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main_menu()