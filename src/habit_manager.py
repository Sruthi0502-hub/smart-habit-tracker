# habit_manager.py

import json
import os

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
    habit = {"name": name, "completed": False}
    habits.append(habit)
    save_habits()
    print("Habit added successfully!")

def list_habits():
    if not habits:
        print("No habits found.")
        return
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit['name']} - Completed: {habit['completed']}")

def complete_habit(index):
    if 0 <= index < len(habits):
        habits[index]["completed"] = True
        save_habits()
        print(f"Habit '{habits[index]['name']}' marked as completed!")
    else:
        print("Invalid habit number.")
