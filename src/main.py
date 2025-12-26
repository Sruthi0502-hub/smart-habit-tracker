from habit_manager import add_habit, list_habits


def main():
    print("Smart Habit Tracker")
    print("1. Add Habit")
    print("2. View Habits")

    choice = input("Choose option: ")

    if choice == "1":
        habit = input("Enter habit name: ")
        add_habit(habit)
        print("Habit added successfully!")

    elif choice == "2":
        habits = list_habits()
        for idx, habit in enumerate(habits, start=1):
            print(f"{idx}. {habit['name']} - Completed: {habit['completed']}")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
