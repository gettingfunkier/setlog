import json, os

filename = "data/cache.json"
filewrite = "workouts/my_workout.txt"

def importData(): # gets information from JSON file
    workout = {}
    with open(filename, "r") as file:
        return json.load(file)

def saveFile(workout): # saves information to JSON file
    with open(filename, "w") as file:
        json.dump(workout, file, indent = 4)

def addEx(workout): # writes a new exercise
    name = input("name: ")
    while not name:
        print("\n[!] Must have a name!")
        name = input("name: ")
    sets = input("sets: ")
    reps = input("reps: ")
    weight = input("weight: ")

    checkCatalog(name)

    if name in workout:
        confirm = input(f"[!] '{name}' already exists. Overwrite? [y/n]: ").lower()
        if confirm != 'y':
            return
    workout[name] = {'sets': sets, 'reps': reps, 'weight': weight}
    print(f"\n[i] '{name}' logged!")
    saveFile(workout)

def checkCatalog(name):
    from generator import receive_from_creator
    receive_from_creator(name)

def viewWorkout(workout): # prints current workout
    if not workout:
        print("\n[x] No exercises logged yet!")
        return

    for exercise in workout:
        exercise = exercise.lower()

        try:
            sets = int(workout[exercise]["sets"])
        except:
            sets = 0
        try:
            reps = int(workout[exercise]["reps"])
        except:
            reps = 0
        try:
            weight = float(workout[exercise]["weight"])
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
            print(f"{exercise.title()}: {desc}")
        else:
            print(f"{exercise.title()}")

def exportFile(workout):  # exports current workout to txt, always in sync with JSON
    with open(filewrite, "w") as file:
        heading = input("\n[>] Add title? (opt.) ")
        if heading:
            file.write(f"{heading}\n")
            weekdays = input(f"[>] Weekdays for {heading}? (opt.) ")
            if weekdays:
                file.write(f"For {weekdays}:\n")
        else:
            weekdays = input(f"[>] Weekdays? (opt.) ")
            if weekdays:
                file.write(f"For {weekdays}:\n")

        for exercise in workout:
            exercise_lower = exercise.lower()

            try:
                sets = int(workout[exercise_lower]["sets"])
            except:
                sets = 0
            try:
                reps = int(workout[exercise_lower]["reps"])
            except:
                reps = 0
            try:
                weight = float(workout[exercise_lower]["weight"])
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
                file.write(f"{exercise.title()}: {desc}\n")
            else:
                file.write(f"{exercise.title()}\n")

    print(f"\n[i] Exported successfully to '{filewrite}'!")

def resetData(workout, check): # erases all data
    if check == True:
        confirm = input("\n[!] will erase all data, proceed? y/n\n> ")

        if confirm == "y":
            workout.clear()
            with open(filename, "w") as file:
                json.dump(workout, file,)
            
            open(filewrite, "w").close()
                    
            print("\n[i] All workout data erased.")

        elif confirm == "n":
            print("\n[i] Reset cancelled. Data preserved.")

        else:
            print("\n[!] Invalid input, reset cancelled by default.")

    elif check == False:
        workout.clear()
        with open(filename, "w") as file:
            json.dump(workout, file,)
        
        open(filewrite, "w").close()

def menu():
    print("\nCreate Workout...")
    print(f"-"*7)
    print("   [V] View workout\n   [A] Add exercise\n   [E] Export\n   [R] Reset\n\n[.] Menu")

def create():
    while True:
        menu()
        act = input("> ")
        workout = importData()
        if act == "a":
            addEx(workout)
        elif act == "v":
            viewWorkout(workout)
        elif act == "e":
            exportFile(workout)
        elif act == "r":
            resetData(workout, True)
        elif act == ".":
            print("\n[i] Data saved! Returning to menu...")
            return
        else:
            print("  ^ Invalid input!")

def receive_from_generator(exercise_list):
    workout = importData()
    resetData(workout, False)

    for exercise in exercise_list:
        print(f"\n> editing '{exercise}'")
        sets = input("sets: ")
        reps = input("reps: ")
        weight = input("weight: ")

        workout[exercise] = {'sets': sets, 'reps': reps, 'weight': weight}
        print(f"\n[i] '{exercise}' logged!")

    saveFile(workout)
    exportFile(workout)
    return