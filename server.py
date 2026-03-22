import json
from datetime import datetime


# FILE HANDLING


DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "subjects": [],
            "progress": {}
        }

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# MAIN FEATURES


def add_subject(subject, deadline):
    data = load_data()

    new_subject = {
        "name": subject,
        "deadline": deadline
    }

    data["subjects"].append(new_subject)
    save_data(data)

    return f"✅ Subject '{subject}' added with deadline {deadline}"



def generate_plan():
    data = load_data()
    today = datetime.today()

    plan = []

    for subj in data["subjects"]:
        deadline = datetime.strptime(subj["deadline"], "%Y-%m-%d")
        days_left = (deadline - today).days

        # Skip expired subjects
        if days_left <= 0:
            continue

        daily_task = f"📖 Study {subj['name']} ({days_left} days left)"
        plan.append(daily_task)

    # After loop
    if not plan:
        return "⚠️ No active subjects."

    return "\n".join(plan)



def update_progress(subject):
    data = load_data()
    today = str(datetime.today().date())

    if subject not in data["progress"]:
        data["progress"][subject] = []

    # Prevent duplicate entry for same day
    if today not in data["progress"][subject]:
        data["progress"][subject].append(today)

    save_data(data)

    return f"✅ Progress updated for {subject}"



def get_today_tasks():
    return generate_plan()


# COMMAND HANDLER


def handle_command(command):
    parts = command.split(" ", 1)
    cmd = parts[0].lower()

    if cmd == "add":
        try:
            name, deadline = parts[1].split("|")
            return add_subject(name.strip(), deadline.strip())
        except:
            return "❌ Format: add <subject>|YYYY-MM-DD"

    elif cmd == "plan":
        return generate_plan()

    elif cmd == "done":
        try:
            return update_progress(parts[1].strip())
        except:
            return "❌ Format: done <subject>"

    elif cmd == "today":
        return get_today_tasks()

    elif cmd == "help":
        return HELP_TEXT

    else:
        return "❌ Unknown command. Type 'help' to see available commands."


# HELP / INTRO TEXT


HELP_TEXT = """
📚 AI Study Planner

Commands you can use:

1. Add a subject:
   add <subject>|YYYY-MM-DD
   Example: add Calculus|2026-04-01

2. View study plan:
   plan

3. Mark study progress:
   done <subject>
   Example: done Calculus

4. View today's tasks:
   today

5. Show help:
   help

6. Exit:
   exit

----------------------------------------
"""


# RUN PROGRAM


if __name__ == "__main__":
    print(HELP_TEXT)

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            print("👋 Exiting Study Planner. Stay consistent!")
            break

        response = handle_command(user_input)
        print(response)