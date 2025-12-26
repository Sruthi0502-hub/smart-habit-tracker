from storage import load_data, save_data


def add_habit(habit_name):
    data = load_data()
    data["habits"].append({
        "name": habit_name,
        "completed": False
    })
    save_data(data)


def list_habits():
    data = load_data()
    return data["habits"]
