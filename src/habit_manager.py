# habit_manager.py

import json
import os
from datetime import date

# File to store habits
HABIT_FILE = "habits.json"

# Load habits from file if exists
if os.path.exists(HABIT_FILE):
    with open(HABIT_FILE, "r") as f:
        habits = json.load(f)
else:
    habits = []

def save_habits():
    """Save habits to file."""
    with open(HABIT_FILE, "w") as f:
        json.dump(habits, f, indent=4)

def add_habit(name):
    habit = {
        "name": name,
        "completed": False,
        "created_date": date.today().isoformat(),
        "last_completed_date": None,
        "current_streak": 0
    }
    habits.append(habit)
    save_habits()
    print("Habit added successfully!")



def list_habits():
    if not habits:
        print("No habits found.")
        return

    for i, habit in enumerate(habits, start=1):
        status = "✔ Completed" if habit["completed"] else "❌ Pending"
        created = habit.get("created_date", "N/A")
        last_done = habit.get("last_completed_date", "N/A")
        streak = habit.get("current_streak", 0)

        print(f"{i}. {habit['name']} - {status} | Created: {created} | Last Done: {last_done} | Current Streak: {streak}")

from datetime import date, timedelta

def complete_habit():
    if not habits:
        print("No habits to complete.")
        return

    list_habits()

    try:
        choice = int(input("Enter the habit number to mark as completed: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= choice <= len(habits):
        habit = habits[choice - 1]
        today = date.today()
        today_str = today.isoformat()

        if habit.get("last_completed_date") == today_str:
            print(f"Habit '{habit['name']}' is already completed today! ✔")
            return

        # Calculate streak
        last_date_str = habit.get("last_completed_date")
        if last_date_str:
            last_date = date.fromisoformat(last_date_str)
            if last_date == today - timedelta(days=1):
                habit["current_streak"] += 1  # consecutive day
            else:
                habit["current_streak"] = 1  # broken streak
        else:
            habit["current_streak"] = 1  # first completion ever

        # Mark completed
        habit["completed"] = True
        habit["last_completed_date"] = today_str
        save_habits()
        print(f"Habit '{habit['name']}' completed today! Current streak: {habit['current_streak']} ✔")
    else:
        print("Invalid habit number.")
