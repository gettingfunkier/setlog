import csv, os
from datetime import datetime

filename = "data/log.csv"
filewrite = "workouts/logbook.txt"

def load_data():
    if not os.path.exists(filename):
        return[["Date", "Exercise", "Sets", "Reps", "Weight"]]
    
    with open(filename, 'r', newline="") as file:
        data = list(csv.reader(file))
        
    if not data:
        return [["Date", "Exercise", "Sets", "Reps", "Weight"]]

    return data


def save_data(data):
    if data[0] != ["Date", "Exercise", "Sets", "Reps", "Weight"]:
        data.insert(0, ["Date", "Exercise", "Sets", "Reps", "Weight"])

    with open(filename, 'w', newline="") as file:
        write = csv.writer(file)
        write.writerows(data)

    return data


def get_valid_date(prompt="date [YYYY-MM-DD]: "):
    while True:
        date_input = input(prompt).strip()
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("[!] Invalid date format! Please use YYYY-MM-DD.")

def add_data(data):
    try:
        date = get_valid_date()
        name = input("name: ").lower().strip()
        while not name:
            print("\n[!] Must have a name!")
            name = input("name: ").lower().strip()
        sets = input("sets: ").strip()
        reps = input("reps: ").strip()
        weight = input("weight: ").strip()

        try:
            sets = int(sets)
        except(ValueError):
            sets = 0

        try:
            reps = int(reps)
        except(ValueError):
            reps = 0

        try:
            weight = float(weight)
        except(ValueError):
            weight = 0

        log = [date, name, sets, reps, weight]
        data.append(log)

        return save_data(data)
    except Exception:
        print(f"\n[!] Error: {Exception}")


def filter_logs(data):
    switch = True
    if not data:
        print("\n[x] No data available.")
        return
    
    inp = input("\nFilter by?\n1. date\n2. exercise\n\n> ").strip()

    if inp == "1":
        switch = True
        date = get_valid_date()
        vessel = date
        sortby = [row for row in data if row[0] == date]

    elif inp == "2":
        switch = False
        exercise = input("Exercise name: ").lower().strip()
        vessel = exercise
        sortby = [row for row in data if row[1].lower() == exercise]

    else:
        print("  ^ Invalid input!")
        return
    
    if sortby:
        print(f"\nWORKOUT LOGS '{vessel}':")
        print(f"-" * 42)

        for row in sortby:
            try:
                if int(row[2]) != 0:
                    sets = int(row[2])
                else:
                    sets = ''
                if int(row[3]) != 0:
                    reps = int(row[3])
                else:
                    reps = ''
                if float(row[4]) != 0.0:
                    weight = float(row[4])
                else:
                    weight = ''
                    
                if switch == True:
                    print(f"{row[1]:<25} {sets:<5} {reps:<5} {weight:<12}")
                else:
                    print(f"{row[0]:<25} {sets:<5} {reps:<5} {weight:<12}")
            except:
                print("\n[?] Unknown error occured!")
                pass

    else:
        print("\n[x] No results found!")
        return
    

def delete_entry(data):
    by = input("\nDelete by?\n1. date\n2. exercise\n3. entry\n4. clear file\n\n> ").strip()
    
    def remove_by_date(data):
        date = get_valid_date()
        sortby = [row for row in data if row[0] != date]

        if len(sortby) == len(data):
            print("\n[x] No entries found!")
            return data
        else:
            return sortby

    def remove_by_exercise(data):
        exercise = input("Exercise name: ").lower().strip()
        sortby = [row for row in data if row[1].lower() != exercise]

        if len(sortby) == len(data):
            print("\n[x] No entries found!")
            return data
        else:
            return sortby

    def remove_by_entry(data):
        date = get_valid_date()
        exercise = input("Exercise name: ").lower().strip()
        sortby = [row for row in data if not (row[0] == date and row[1].lower() == exercise)]

        if len(sortby) == len(data):
            print("\n[x] No matching entry found!")
            return data
        else:
            print(f"\n[i] Removed {exercise} on {date}.")
            return sortby
        
    def remove_all(data):
        confirm = input("\nAre you sure you want to delete all entries? [y/n]: ").lower().strip()
        if confirm == 'y':
            print("\n[i] All entries deleted!")
            return [["Date", "Exercise", "Sets", "Reps", "Weight"]]
        else:
            print("\n[i] No entries deleted.")
            return data

    if by == "1":
        data = remove_by_date(data)

    elif by == "2":
        data = remove_by_exercise(data)

    elif by == "3":
        data = remove_by_entry(data)

    elif by == "4":
        data = remove_all(data)

    else:
        print("\n[!] Invalid input!")
        return data

    save_data(data)
    data = load_data()
    return data


def view_logs(data):
    if len(data) <= 1:
        print("\n[x] No workouts recorded yet.")
        return
    
    print("\nWORKOUT LOGS:")
    print(f"{'Date':<12} {'Exercise':<25} {'Sets':<5} {'Reps':<5} {'Weight (kg)':<12}")
    print(f"-" * 57)

    for row in data[1:]:
        if int(row[2]) != 0:
            sets = int(row[2])
        else:
            sets = ''
        if int(row[3]) != 0:
            reps = int(row[3])
        else:
            reps = ''
        if float(row[4]) != 0.0:
            weight = float(row[4])
        else:
            weight = ''
            
        print(f"{row[0]:<12} {row[1]:<25} {sets:<5} {reps:<5} {weight:<12}")


def progress_track(data):
    data = load_data()
    counter = 0
    vessel_list = []

    for row in data[1:]:
        vessel_list.append(row[1].lower())
        counter = counter + 1

    if vessel_list:
        print(f"\nTotal workouts logged: {counter}")
        print(f"Most performed exercise: {max(set(vessel_list), key=vessel_list.count)}")
    else:
        print("\n[x] No exercises logs yet!")

def export_data(data):
    data = load_data()

    vessel_data = []
    for row in data[1:]:
        if row[0] not in vessel_data:
            vessel_data.append(row[0])

    with open(filewrite, "w") as file:
        for date in vessel_data:
            file.write(f"{date}:\n")

            for row in data[1:]:
                if row[0] == date:
                    exercise = row[1].lower()

                    try:
                        sets = int(row[2])
                    except:
                        sets = 0
                    try:
                        reps = int(row[3])
                    except:
                        reps = 0
                    try:
                        weight = float(row[4])
                    except:
                        weight = 0.0

                    desc = ""
                    if sets:
                        desc += f"{sets} set{'s' if sets > 1 else ''}"
                        if reps:
                            desc += f" of {reps} rep{'s' if reps > 1 else ''}"
                    elif reps:
                        desc += f"{reps} rep{'s' if reps > 1 else ''}"
                    
                    if weight:
                        if desc:
                            desc += f", at {weight}kg"
                        else:
                            desc += f"at {weight}kg"

                    if desc:
                        file.write(f"{exercise}: {desc}\n")
                    else:
                        file.write(f"{exercise}\n")

            file.write("\n")
    print(f"\n[i] Exported successfully to '{filewrite}'!")

def menu():
    print("\nLog Session...")
    print(f"-"*7)
    print("   [V] View\n   [A] Add\n   [F] Filter\n   [S] Stats\n   [E] Export\n   [D] Delete\n\n[.] Menu")

def log():
    data = load_data()
    while True:
        menu()
        inp = input("> ").lower().strip()
        if inp == "a":
            add_data(data)
        elif inp == "f":
            filter_logs(data)
        elif inp == "s":
            progress_track(data)
        elif inp == "v":
            view_logs(data)
        elif inp == "e":
            export_data(data)
        elif inp == "d":
            data = delete_entry(data)
        elif inp == ".":
            print("\n[i] Data saved! Returning to menu...")
            save_data(data)
            return

        else:
            print("  ^ Invalid input!")
            return