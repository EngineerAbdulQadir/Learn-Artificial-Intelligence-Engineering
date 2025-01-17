# -*- coding: utf-8 -*-
import time
from functools import wraps
from datetime import datetime

# =============================================================================
#                        HELPER FUNCTIONS
# =============================================================================

def timestamp() -> str:
    """Return a formatted timestamp with date and time."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")

def parse_date(datestr: str) -> datetime:
    """
    Parse a date/time in 'YYYY-MM-DD HH:MM' format or 'YYYY-MM-DD'.
    If invalid or blank, default to now.
    """
    if not datestr:
        return datetime.now()
    fmts = ["%Y-%m-%d %H:%M", "%Y-%m-%d"]
    for f in fmts:
        try:
            return datetime.strptime(datestr, f)
        except ValueError:
            pass
    return datetime.now()

# =============================================================================
#                      IN-MEMORY 'DATABASE'
# =============================================================================

"""
USER_DB structure:
{
  "<username>": {
    "password": str,
    "role": "admin"/"user",
    "name": str,            # Full name
    "is_active": bool,
    "history": [ list of logs ],
    "reservations": [ booking_id, ... ]   # list of booking IDs for user
  }, ...
}

FLIGHTS_DB structure:
{
  "<flight_id>": {
    "flight_number": str (e.g. "ABC123"),
    "origin": str,
    "destination": str,
    "departure_time": datetime,
    "arrival_time": datetime,
    "total_seats": int,
    "booked_seats": int,
    "price": float,           # base price
    "history": [strings of event logs],
  },
  ...
}

BOOKINGS_DB structure:
{
  "<booking_id>": {
    "user": <username>,
    "flight_id": <flight_id>,
    "seats": int (number of seats booked),
    "status": "confirmed"/"cancelled",
    "price_paid": float,
    "timestamp": str (when created),
  }, ...
}
"""

USER_DB = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "name": "System Admin",
        "is_active": True,
        "history": ["Admin account created."],
        "reservations": []
    },
    "alice": {
        "password": "alice123",
        "role": "user",
        "name": "Alice Example",
        "is_active": True,
        "history": ["Joined as normal user."],
        "reservations": []
    }
}

FLIGHTS_DB = {}
BOOKINGS_DB = {}

FLIGHT_COUNTER = 1000
BOOKING_COUNTER = 2000

current_user = None

# =============================================================================
#                           DECORATORS
# =============================================================================

def login_required(func):
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
    def wrapper(*args, **kwargs):
        global current_user
        if not current_user:
            print("You must be logged in to use this feature.")
            login()
            if not current_user:
                return
        if USER_DB[current_user]["role"] != "admin":
            print("Admin privileges are required for this action.")
            return
        return func(*args, **kwargs)
    return wraps(func)(wrapper)

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
        print("No user is logged in.")
        return
    print(f"User {USER_DB[current_user]['name']} has been logged out.")
    current_user = None

# =============================================================================
#                       ADMIN FEATURES
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
        "reservations": []
    }
    print(f"User '{uname}' created with role '{role}'.")

@admin_required
def toggle_user_status():
    """Activate or deactivate a user account."""
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
    """Remove a user from the system."""
    uname = input("Enter username to remove: ").strip()
    if uname not in USER_DB:
        print("No such user.")
        return
    if uname == "admin":
        print("Cannot remove the main admin.")
        return
    confirm = input(f"Are you sure to remove '{uname}'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return
    del USER_DB[uname]
    print(f"User '{uname}' removed from system.")

@admin_required
def view_all_users():
    """List all users with roles and statuses."""
    print("\n=== All Users ===")
    for uname, data in USER_DB.items():
        print(f"Username: {uname}, Role: {data['role']}, Active: {data['is_active']}, Name: {data['name']}")
    print("")

# =============================================================================
#                        FLIGHT MANAGEMENT (ADMIN)
# =============================================================================

@admin_required
def create_flight():
    """Add a new flight to the system."""
    global FLIGHT_COUNTER
    fl_num = input("Enter flight number (e.g. 'ABC123'): ").strip()
    origin = input("Enter origin airport/city: ").strip()
    destination = input("Enter destination airport/city: ").strip()

    dep_str = input("Enter departure datetime (YYYY-MM-DD HH:MM): ").strip()
    arr_str = input("Enter arrival datetime (YYYY-MM-DD HH:MM): ").strip()
    dep_dt = parse_date(dep_str)
    arr_dt = parse_date(arr_str)

    seat_str = input("Enter total seats available: ").strip()
    try:
        total_seats = int(seat_str)
    except ValueError:
        total_seats = 100  # default
    price_str = input("Enter base ticket price: ").strip()
    try:
        price_val = float(price_str)
    except ValueError:
        price_val = 100.0

    FLIGHT_COUNTER += 1
    flight_id = f"F{FLIGHT_COUNTER}"

    FLIGHTS_DB[flight_id] = {
        "flight_number": fl_num,
        "origin": origin,
        "destination": destination,
        "departure_time": dep_dt,
        "arrival_time": arr_dt,
        "total_seats": total_seats,
        "booked_seats": 0,
        "price": price_val,
        "history": [f"{timestamp()} Flight created by admin."]
    }
    print(f"Flight '{fl_num}' added with ID={flight_id}.")

@admin_required
def edit_flight():
    """Edit details of an existing flight."""
    fid = input("Enter Flight ID to edit: ").strip()
    if fid not in FLIGHTS_DB:
        print("No such flight.")
        return
    fdata = FLIGHTS_DB[fid]
    print(f"Current flight info: FlightNum={fdata['flight_number']}, Origin={fdata['origin']}, Dest={fdata['destination']}")

    new_fl_num = input(f"New flight number [old={fdata['flight_number']}] (blank=no change): ").strip()
    if new_fl_num:
        fdata["flight_number"] = new_fl_num
    new_origin = input(f"New origin [old={fdata['origin']}] (blank=no change): ").strip()
    if new_origin:
        fdata["origin"] = new_origin
    new_dest = input(f"New destination [old={fdata['destination']}] (blank=no change): ").strip()
    if new_dest:
        fdata["destination"] = new_dest

    dep_str = input(f"New departure (YYYY-MM-DD HH:MM) [old={fdata['departure_time'].strftime('%Y-%m-%d %H:%M')}]: ").strip()
    if dep_str:
        fdata["departure_time"] = parse_date(dep_str)
    arr_str = input(f"New arrival (YYYY-MM-DD HH:MM) [old={fdata['arrival_time'].strftime('%Y-%m-%d %H:%M')}]: ").strip()
    if arr_str:
        fdata["arrival_time"] = parse_date(arr_str)

    seat_str = input(f"New total seats [old={fdata['total_seats']}] (blank=no change): ").strip()
    if seat_str:
        try:
            fdata["total_seats"] = int(seat_str)
        except ValueError:
            pass
    price_str = input(f"New ticket price [old={fdata['price']}] (blank=no change): ").strip()
    if price_str:
        try:
            fdata["price"] = float(price_str)
        except ValueError:
            pass

    fdata["history"].append(f"{timestamp()} Flight edited by admin.")
    print("Flight updated successfully.")

@admin_required
def remove_flight():
    """Remove a flight from the system."""
    fid = input("Enter Flight ID to remove: ").strip()
    if fid not in FLIGHTS_DB:
        print("No such flight.")
        return
    confirm = input("Are you sure? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return
    del FLIGHTS_DB[fid]
    print(f"Flight {fid} removed from system.")

@admin_required
def view_all_flights():
    """Admin sees all flights, basic info."""
    if not FLIGHTS_DB:
        print("No flights in the system.")
        return
    print("\n=== All Flights ===")
    for fid, fdata in FLIGHTS_DB.items():
        dep_str = fdata["departure_time"].strftime("%Y-%m-%d %H:%M")
        arr_str = fdata["arrival_time"].strftime("%Y-%m-%d %H:%M")
        print(f"ID={fid}, FlightNum={fdata['flight_number']}, {fdata['origin']} -> {fdata['destination']}, "
              f"Dep={dep_str}, Arr={arr_str}, Seats={fdata['booked_seats']}/{fdata['total_seats']}, Price={fdata['price']}")

# =============================================================================
#                USER FEATURES - SEARCH & BOOK
# =============================================================================

@login_required
def search_flights():
    """Search flights by origin, destination, date range, etc."""
    orig = input("Origin (blank=any): ").strip()
    dest = input("Destination (blank=any): ").strip()
    date_str = input("Filter by departure date (YYYY-MM-DD, blank=none): ").strip()
    date_dt = parse_date(date_str) if date_str else None

    results = []
    for fid, fdata in FLIGHTS_DB.items():
        if orig and fdata["origin"].lower() != orig.lower():
            continue
        if dest and fdata["destination"].lower() != dest.lower():
            continue
        if date_str:
            # Compare only the date portion of departure_time
            flight_date = fdata["departure_time"].date()
            if flight_date != date_dt.date():
                continue
        # If we get here, it matches
        results.append((fid, fdata))

    if not results:
        print("No matching flights.")
        return

    print("\n=== Matching Flights ===")
    for fid, fdata in results:
        dep_str = fdata["departure_time"].strftime("%Y-%m-%d %H:%M")
        arr_str = fdata["arrival_time"].strftime("%Y-%m-%d %H:%M")
        seats_left = fdata["total_seats"] - fdata["booked_seats"]
        print(f"ID={fid}, {fdata['flight_number']}, {fdata['origin']}-> {fdata['destination']} "
              f"Dep={dep_str}, Arr={arr_str}, SeatsLeft={seats_left}, Price={fdata['price']}")
    print("")

@login_required
def book_flight():
    """Book seats on a flight if available."""
    fid = input("Enter Flight ID to book: ").strip()
    if fid not in FLIGHTS_DB:
        print("No such flight.")
        return
    fdata = FLIGHTS_DB[fid]
    seats_left = fdata["total_seats"] - fdata["booked_seats"]
    if seats_left <= 0:
        print("No seats left on this flight.")
        return
    seat_str = input(f"How many seats do you want to book? (Available={seats_left}): ").strip()
    try:
        seat_count = int(seat_str)
    except ValueError:
        print("Invalid seat number.")
        return
    if seat_count <= 0 or seat_count > seats_left:
        print("Not enough seats or invalid seat request.")
        return

    global BOOKING_COUNTER
    BOOKING_COUNTER += 1
    booking_id = f"B{BOOKING_COUNTER}"
    total_price = seat_count * fdata["price"]
    # Create booking
    BOOKINGS_DB[booking_id] = {
        "user": current_user,
        "flight_id": fid,
        "seats": seat_count,
        "status": "confirmed",
        "price_paid": total_price,
        "timestamp": timestamp()
    }
    # update flight seats
    FLIGHTS_DB[fid]["booked_seats"] += seat_count
    # Add to user reservations
    USER_DB[current_user]["reservations"].append(booking_id)
    print(f"Booking created (ID={booking_id}), total price=${total_price:.2f}. Seats confirmed.")

@login_required
def view_my_bookings():
    """View the current user's flight bookings."""
    booking_ids = USER_DB[current_user]["reservations"]
    if not booking_ids:
        print("No bookings found.")
        return
    print("\n=== Your Bookings ===")
    for bid in booking_ids:
        bdata = BOOKINGS_DB[bid]
        if bdata["status"] == "cancelled":
            status_str = "CANCELLED"
        else:
            status_str = "CONFIRMED"
        fid = bdata["flight_id"]
        flight_info = FLIGHTS_DB[fid]
        flight_num = flight_info["flight_number"]
        dep_str = flight_info["departure_time"].strftime("%Y-%m-%d %H:%M")
        arr_str = flight_info["arrival_time"].strftime("%Y-%m-%d %H:%M")
        print(f"BookingID={bid}, FlightNum={flight_num}, Seats={bdata['seats']}, "
              f"PricePaid={bdata['price_paid']:.2f}, Status={status_str}")
        print(f"  {flight_info['origin']} -> {flight_info['destination']}, Dep={dep_str}, Arr={arr_str}\n")

@login_required
def cancel_booking():
    """Cancel an existing booking (if status is confirmed). Refund logic is not modeled here."""
    bid = input("Enter Booking ID to cancel: ").strip()
    if bid not in BOOKINGS_DB:
        print("No such booking.")
        return
    bdata = BOOKINGS_DB[bid]
    if bdata["user"] != current_user and USER_DB[current_user]["role"] != "admin":
        print("You can only cancel your own bookings (unless you're admin).")
        return
    if bdata["status"] == "cancelled":
        print("This booking is already cancelled.")
        return
    # Confirm
    confirm = input("Are you sure to cancel this booking? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Cancellation aborted.")
        return
    # cancel
    bdata["status"] = "cancelled"
    # Return seats to flight
    fid = bdata["flight_id"]
    seat_count = bdata["seats"]
    FLIGHTS_DB[fid]["booked_seats"] -= seat_count
    print(f"Booking {bid} cancelled successfully.")

# =============================================================================
#                        MAIN MENU
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Flight Reservation System")
        print(f"Current User: {current_user if current_user else 'None'}")
        print("-----------------------------------------------")
        print("1.  Login")
        print("2.  Logout")

        print("\n-- Admin Features --")
        print("3.  Create User")
        print("4.  Toggle User Status")
        print("5.  Remove User")
        print("6.  View All Users")
        print("7.  Create Flight")
        print("8.  Edit Flight")
        print("9.  Remove Flight")
        print("10. View All Flights")

        print("\n-- User Features --")
        print("11. Search Flights")
        print("12. Book Flight")
        print("13. View My Bookings")
        print("14. Cancel Booking")

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
            view_all_users()
        elif choice == "7":
            create_flight()
        elif choice == "8":
            edit_flight()
        elif choice == "9":
            remove_flight()
        elif choice == "10":
            view_all_flights()
        elif choice == "11":
            search_flights()
        elif choice == "12":
            book_flight()
        elif choice == "13":
            view_my_bookings()
        elif choice == "14":
            cancel_booking()
        elif choice == "15":
            print("\nExiting Education Trust Nasra School - Flight Reservation System")
            break
        else:
            print("Invalid choice. Please try again.")

# =============================================================================
#                   SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main_menu()