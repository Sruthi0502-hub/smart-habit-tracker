from habit_manager import add_habit, list_habits, complete_habit

def main():
    while True:
        print("\nSmart Habit Tracker")
        print("1. Add Habit")
        print("2. List Habits")
        print("3. Complete Habit")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            habit = input("Enter habit name: ")
            add_habit(habit)

        elif choice == "2":
            list_habits()

        elif choice == "3":
             complete_habit()  # ✅ no arguments needed


        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
