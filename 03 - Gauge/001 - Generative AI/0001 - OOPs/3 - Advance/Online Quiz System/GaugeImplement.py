import time
from functools import wraps

# =============================================================================
#                           HELPER FUNCTIONS
# =============================================================================

def timestamp() -> str:
    """Return a nicely formatted timestamp."""
    return time.strftime("[%Y-%m-%d %H:%M:%S]")

# =============================================================================
#                         IN-MEMORY 'DATABASE'
# =============================================================================

"""
USER_DB structure:
{
  "<username>": {
    "password": str,
    "role": "admin"/"user",
    "name": str,          # Full name
    "is_active": bool,
    "history": [list of event logs],
    "quiz_attempts": [ list of attempt IDs ],
  }, ...
}

QUIZ_DB structure:
{
  "<quiz_id>": {
    "title": str,
    "description": str,
    "questions": [
      {
        "question_id": int,
        "question_text": str,
        "options": [list of options],
        "correct_answer": int (index of correct option, e.g. 0-based),
        "points": int (points for the question)
      }, ...
    ],
    "creator": <username>,
    "is_published": bool,
    "history": [strings of event logs],
  },
  ...
}

ATTEMPTS_DB structure:
{
  "<attempt_id>": {
    "user": <username>,
    "quiz_id": <quiz_id>,
    "score": float,
    "answers": [int or None for each question, indicating user’s chosen option index],
    "timestamp": str,
  },
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
        "quiz_attempts": []
    },
    "bob": {
        "password": "bob123",
        "role": "user",
        "name": "Bob Example",
        "is_active": True,
        "history": ["Joined as user."],
        "quiz_attempts": []
    }
}

QUIZ_DB = {}
ATTEMPTS_DB = {}

QUIZ_COUNTER = 1000
ATTEMPT_COUNTER = 2000

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
            print("Admin privileges are required for this action.")
            return
        return func(*args, **kwargs)
    return wrapper

# =============================================================================
#                     AUTH & SESSION
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
        "quiz_attempts": []
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
    """List all users with role and status."""
    print("\n=== All Users ===")
    for uname, data in USER_DB.items():
        print(f"Username: {uname}, Role: {data['role']}, Active: {data['is_active']}, Name: {data['name']}")
    print("")

# =============================================================================
#                      QUIZ MANAGEMENT (ADMIN)
# =============================================================================

@admin_required
def create_quiz():
    """Create a new quiz (title, description)."""
    global QUIZ_COUNTER
    title = input("Enter quiz title: ").strip()
    desc = input("Enter quiz description: ").strip()

    QUIZ_COUNTER += 1
    quiz_id = f"Q{QUIZ_COUNTER}"

    QUIZ_DB[quiz_id] = {
        "title": title,
        "description": desc,
        "questions": [],
        "creator": current_user,
        "is_published": False,
        "history": [f"{timestamp()} Quiz created by admin."],
    }

    print(f"Quiz '{title}' created with ID={quiz_id}. Not published yet.")

@admin_required
def add_question():
    """Add a question to an existing quiz."""
    qid = input("Enter Quiz ID to add a question to: ").strip()
    if qid not in QUIZ_DB:
        print("No such quiz.")
        return
    if QUIZ_DB[qid]["is_published"]:
        print("Cannot modify questions of a published quiz. Unpublish first or create a new quiz.")
        return

    # get question details
    question_text = input("Enter question text: ").strip()
    # Collect multiple choice options
    options = []
    while True:
        opt = input(f"Enter option #{len(options)+1} (blank to finish): ").strip()
        if not opt:
            break
        options.append(opt)
    if len(options) < 2:
        print("At least 2 options required.")
        return
    print("Options:")
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    correct_str = input("Enter the correct option number: ").strip()
    try:
        correct_idx = int(correct_str) - 1
        if correct_idx < 0 or correct_idx >= len(options):
            print("Invalid correct answer index.")
            return
    except ValueError:
        print("Invalid input.")
        return

    pts_str = input("Points for this question (default=1): ").strip()
    try:
        pts = int(pts_str) if pts_str else 1
    except ValueError:
        pts = 1

    # build question data
    question_data = {
        "question_id": len(QUIZ_DB[qid]["questions"]) + 1,
        "question_text": question_text,
        "options": options,
        "correct_answer": correct_idx,
        "points": pts
    }

    QUIZ_DB[qid]["questions"].append(question_data)
    QUIZ_DB[qid]["history"].append(f"{timestamp()} Question added by admin.")
    print("Question added successfully.")

@admin_required
def publish_quiz():
    """Set a quiz as published (cannot modify questions after publishing)."""
    qid = input("Enter Quiz ID to publish: ").strip()
    if qid not in QUIZ_DB:
        print("No such quiz.")
        return
    if QUIZ_DB[qid]["is_published"]:
        print("Quiz already published.")
        return
    if not QUIZ_DB[qid]["questions"]:
        print("Cannot publish a quiz with no questions.")
        return

    QUIZ_DB[qid]["is_published"] = True
    QUIZ_DB[qid]["history"].append(f"{timestamp()} Quiz published.")
    print(f"Quiz {qid} published successfully.")

@admin_required
def unpublish_quiz():
    """Set a quiz to unpublished (allows editing again)."""
    qid = input("Enter Quiz ID to unpublish: ").strip()
    if qid not in QUIZ_DB:
        print("No such quiz.")
        return
    if not QUIZ_DB[qid]["is_published"]:
        print("Quiz is already unpublished.")
        return

    QUIZ_DB[qid]["is_published"] = False
    QUIZ_DB[qid]["history"].append(f"{timestamp()} Quiz unpublished.")
    print(f"Quiz {qid} is now unpublished.")

@admin_required
def remove_quiz():
    """Remove a quiz from the system entirely."""
    qid = input("Enter Quiz ID to remove: ").strip()
    if qid not in QUIZ_DB:
        print("No such quiz.")
        return
    confirm = input("Are you sure you want to remove this quiz? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Removal cancelled.")
        return
    del QUIZ_DB[qid]
    print(f"Quiz {qid} removed from the system.")

@admin_required
def view_all_quizzes():
    """Admin sees all quizzes, whether published or not."""
    if not QUIZ_DB:
        print("No quizzes in the system.")
        return
    print("\n=== All Quizzes ===")
    for qid, qdata in QUIZ_DB.items():
        status = "PUBLISHED" if qdata["is_published"] else "UNPUBLISHED"
        print(f"ID={qid}, Title='{qdata['title']}', Questions={len(qdata['questions'])}, Status={status}")
    print("")

# =============================================================================
#             USER FEATURES: TAKING QUIZZES
# =============================================================================

@login_required
def list_published_quizzes():
    """List all published quizzes for a user to see."""
    published = [(qid, qdata) for qid, qdata in QUIZ_DB.items() if qdata["is_published"]]
    if not published:
        print("No published quizzes available.")
        return
    print("\n=== Published Quizzes ===")
    for qid, qdata in published:
        print(f"ID={qid}, Title='{qdata['title']}', Questions={len(qdata['questions'])}")
    print("")

@login_required
def take_quiz():
    """User takes a published quiz, system calculates score, saves attempt."""
    qid = input("Enter Quiz ID to attempt: ").strip()
    if qid not in QUIZ_DB:
        print("No such quiz.")
        return
    quiz_data = QUIZ_DB[qid]
    if not quiz_data["is_published"]:
        print("That quiz is not published yet.")
        return
    if not quiz_data["questions"]:
        print("This quiz has no questions.")
        return

    print(f"Taking quiz '{quiz_data['title']}' - {quiz_data['description']}")
    total_score = 0
    total_points = sum(q["points"] for q in quiz_data["questions"])
    user_answers = []

    for q in quiz_data["questions"]:
        print(f"\nQ{q['question_id']}: {q['question_text']} (Points: {q['points']})")
        for i, opt in enumerate(q["options"], start=1):
            print(f"{i}. {opt}")

        choice_str = input("Your answer (number): ").strip()
        try:
            choice_idx = int(choice_str) - 1
        except ValueError:
            choice_idx = -1
        user_answers.append(choice_idx)

        # check correctness
        if choice_idx == q["correct_answer"]:
            total_score += q["points"]

    # Save attempt
    global ATTEMPT_COUNTER
    ATTEMPT_COUNTER += 1
    attempt_id = f"A{ATTEMPT_COUNTER}"
    ATTEMPTS_DB[attempt_id] = {
        "user": current_user,
        "quiz_id": qid,
        "score": total_score,
        "answers": user_answers,
        "timestamp": timestamp()
    }

    # link attempt to user
    USER_DB[current_user]["quiz_attempts"].append(attempt_id)

    print(f"\nQuiz completed! Your score: {total_score}/{total_points} (ID={attempt_id}).")

@login_required
def view_my_attempts():
    """User sees all their quiz attempts."""
    attempts = USER_DB[current_user]["quiz_attempts"]
    if not attempts:
        print("No attempts found.")
        return

    print("\n=== Your Quiz Attempts ===")
    for aid in attempts:
        adata = ATTEMPTS_DB[aid]
        qid = adata["quiz_id"]
        quiz_title = QUIZ_DB[qid]["title"] if qid in QUIZ_DB else "Unknown Quiz"
        score = adata["score"]
        attempt_time = adata["timestamp"]
        print(f"AttemptID={aid}, Quiz='{quiz_title}', Score={score}, Time={attempt_time}")
    print("")

# =============================================================================
#                         MAIN MENU
# =============================================================================

def main_menu():
    while True:
        print("Education Trust Nasra School - Online Quiz System")
        print(f"Current User: {current_user if current_user else 'None'}")
        print("----------------------------------------")
        print("1.  Login")
        print("2.  Logout")

        print("\n-- Admin Features --")
        print("3.  Create User")
        print("4.  Toggle User Status")
        print("5.  Remove User")
        print("6.  View All Users")
        print("7.  Create Quiz")
        print("8.  Add Question to Quiz")
        print("9.  Publish Quiz")
        print("10. Unpublish Quiz")
        print("11. Remove Quiz")
        print("12. View All Quizzes")

        print("\n-- User Features --")
        print("13. List Published Quizzes")
        print("14. Take Quiz")
        print("15. View My Attempts")

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
            create_quiz()
        elif choice == "8":
            add_question()
        elif choice == "9":
            publish_quiz()
        elif choice == "10":
            unpublish_quiz()
        elif choice == "11":
            remove_quiz()
        elif choice == "12":
            view_all_quizzes()
        elif choice == "13":
            list_published_quizzes()
        elif choice == "14":
            take_quiz()
        elif choice == "15":
            view_my_attempts()
        elif choice == "16":
            print("\nExiting Education Trust Nasra School - Online Quiz System")
            break
        else:
            print("Invalid choice. Please try again.")

# =============================================================================
#                   SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main_menu()