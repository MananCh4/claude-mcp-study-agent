import json
from datetime import datetime, timedelta

#FILE HANDLING

data_file = 'data.json'

def load_data():
    try:
        with open(data_file, 'r') as f:
            return json.load(f)
        
    except:
        return {
            "subjects" : [],
            "progress" : {}
        }
    

def save_data(data):
    with open(data_file, 'w')as f:
        json.dump(data, f, indent=4)

#MAIN FEATURES

def add_subject(subject, deadline):
    data = load_data()
    subject = {
        "name" : subject,
        "deadline": deadline
    }

    data["subjects"].append(subject)
    save_data(data)

    print( f"Subject '{subject}' added with deadline {deadline}" )

def generate_plan():
    data = load_data()
    today = datetime.today()
    plan = []

    for subj in data["subjects"]:
        deadline = datetime.strptime(subj["deadline"],"%Y-%m-%d")
        days_left = (deadline - today).days

        if days_left > 0:
            continue

        daily_task = f"Study {subj['name']} ({days_left} days left)"
        plan.append(daily_task)
    
        if not plan:
            return "No active subjects."
    
        return "\n".join(plan)


# Mark progress
def update_progress(subject):
    data = load_data()
    
    today = str(datetime.today().date())
    
    if subject not in data["progress"]:
        data["progress"][subject] = []
    
    data["progress"][subject].append(today)
    save_data(data)
    
    return f"Progress is updated for {subject}"



# Get today's tasks
def get_today_tasks():
    return generate_plan()

def handle_command(command):
    parts = command.split(" ", 1)
    cmd = parts[0].lower()
    
    if cmd == "add":
        try:
            name, deadline = parts[1].split("|")
            return add_subject(name.strip(), deadline.strip())
        except:
            return "Format: add <subject>|YYYY-MM-DD"
    
    elif cmd == "plan":
        return generate_plan()
    
    elif cmd == "done":
        return update_progress(parts[1].strip())
    
    elif cmd == "today":
        return get_today_tasks()
    
    else:
        return "Commands: add, plan, done, today"


if __name__ == "__main__":
    print("AI Study Planner Running (type 'exit' to quit)")
    
    while True:
        user_input = input(">> ")
        
        if user_input.lower() == "exit":
            break
        
        response = handle_command(user_input)
        print(response)
