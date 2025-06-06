import json, random

fileread = "data/catalog.json"
filewrite = "workouts/generated_workout.txt"

def load_catalog():
    with open(fileread, "r") as file:
        catalog = json.load(file)
    return catalog

def save_catalog(catalog):
    with open(fileread, "w") as file:
        json.dump(catalog, file, indent=4)

def input_groups():
    groups = []
    group = input("add group ['/' to finish]: ")
    while not group or group == "/":
        print("[x] No groups provided. Please enter at least one group.")
        group = input("add group ['/' to finish]: ")
    while group != "/":
        groups.append(group)
        group = input("add group ['/' to finish]: ")
    print("")
    return groups
    
def get_exercises(groups):
    switch = False
    try:
        filtered_exercises = {}
        cache = load_catalog()
        for type in groups:
            try:
                filtered_exercises[type] = cache[type]
            except(KeyError):
                print(f" -> Unable to get data for '{type}': invalid group")
                switch = True
        if switch == True:
            print("")
        return filtered_exercises
    except(FileNotFoundError, json.JSONDecodeError):
        return None
    
def pick_exercises(groups=None):
    if groups is None:
        groups = input_groups()
    if not groups:
        print("[x] No groups provided. Cancelling operation.")
        return {}
    filtered_exercises = get_exercises(groups)
    picked_exercises = {}
    for group, exercises in filtered_exercises.items():
        if not isinstance(exercises, list) or len(exercises) == 0:
            print(f"\n[x] No exercises in group '{group}'")
            continue
        picked_exercises[group] = random.choice(exercises)
    return picked_exercises

def create_workout(groups=None):
    picked_exercises = pick_exercises(groups)
    if not picked_exercises:
        print("[x] No exercises picked. Cancelling operation.")
        return
    with open(filewrite, 'w') as file:
        for exercise in picked_exercises:
            file.write(f"{picked_exercises[exercise]}\n".title())
    print(f"[i] Workout generated in '{filewrite}'!")


def send_to_creator(picked_exercises):
    from creator import receive_from_generator
    receive_from_generator(picked_exercises)
    
def print_groups():
    print("\nAvailable groups:")
    with open(fileread) as file:
        cache = json.load(file)
    for group in cache:
        print(f"> {group.title()}")

def add_to_catalog():
    catalog = load_catalog()

    while True:
        print("\nWhat do you want to add?")
        print("1. Muscle group")
        print("2. New exercise")
        print("3. Exit")
        switch = input("> ").strip()

        if switch == "1":
            group = input("Enter new muscle group name: ").strip().lower()
            if group in catalog:
                print(f"[!] The group '{group}' already exists.")
            else:
                catalog[group] = []
                save_catalog(catalog)
                print(f"[i] Added new group '{group}' and saved.")

        elif switch == "2":
            group = input("Enter muscle group to add exercise to: ").strip().lower()
            if group not in catalog:
                print(f"[!] Group '{group}' doesn't exist. Please add it first.")
                continue
            exercise = input("Enter exercise name to add: ").strip().lower()
            if exercise in catalog[group]:
                print(f"[!] Exercise '{exercise}' already exists in group '{group}'.")
            else:
                catalog[group].append(exercise)
                save_catalog(catalog)
                print(f"[i] Added exercise '{exercise}' to group '{group}' and saved.")

        elif switch == "3":
            print("[i] Exiting catalog editor.")
            break

        else:
            print("[!] Invalid input. Please select 1, 2, or 3.")

def receive_from_creator(exercise):
    catalog = load_catalog()
    if not any(exercise in group for group in catalog.values()):
        switch = input(f"\n[!] Exercise '{exercise}' not found in catalog. Add it? [y/n]: ").lower()
        if switch == "y":
            group = input("\nEnter muscle group to add exercise to: ").strip().lower()
            if group not in catalog:
                catalog[group] = []

            if exercise in catalog[group]:
                print(f"\n[!] Exercise '{exercise}' already exists in group '{group}'.")
            else:
                catalog[group].append(exercise)
                save_catalog(catalog)
                print(f"\n[i] Added exercise '{exercise}' to group '{group}' and saved.")

def group_presets():
    presets = {
        "upper body": ["chest", "back", "shoulders", "triceps", "biceps"],
        "lower body": ["quads", "hamstrings", "calves", "glutes", "core"],
        "full body": ["chest", "back", "shoulders", "triceps", "biceps", "quads", "hamstrings", "calves", "glutes", "core"],
        "push": ["chest", "shoulders", "triceps", "quads", "calves"],
        "pull": ["back", "biceps", "hamstrings", "glutes", "core"],
        "core glutes": ["core", "glutes", "hamstrings", "quads"],
        "arms shoulders": ["biceps", "triceps", "shoulders"],
        "legs": ["quads", "hamstrings", "calves", "glutes"],
        "chest back": ["chest", "back"]
    }
    return presets

def show_presets():
    presets = group_presets()
    print("\nAvailable presets:\n")
    for preset in presets:
        print(f"> {preset.title()}:\n {', '.join(presets[preset])}\n")

def pick_preset():
    show_presets()
    preset = input("Enter preset name: ").strip().lower()
    presets = group_presets()
    if preset in presets:
        return presets[preset]
    else:
        print(f"\n[!] Preset '{preset}' not found.")
        return []
    
def get_generated_workout():
    try:
        with open(filewrite, 'r') as file:
            workout = file.readlines()
        return [exercise.strip().lower() for exercise in workout]
    except FileNotFoundError:
        print(f"\n[!] No generated workout found at '{filewrite}'.")
        return []

def menu():
    print("\nGenerate Workout...")
    print(f"-"*7)
    print("   [R] Run\n   [P] Presets\n   [O] Options\n\n[.] Menu")

def options():
    switch = input("\nOptions:\n    1. Add to catalog\n    2. View groups\n    3. Create plan\n    4. Exit\n> ").strip()    
    if switch == "1":
        add_to_catalog()
    elif switch == "2":
        print_groups()
    elif switch == "3":
        generated_workout = get_generated_workout()
        if not generated_workout:
            print("\n[x] No generated workout found. Please run the generator first.")
            return
        send_to_creator(generated_workout)
        pass
    elif switch == "4":
        print("\n[i] Exiting options.")
        return
    else:
        print("\n[!] Invalid input!")
        
def generate():
    while True:
        menu()
        inp = input("> ").lower()
        if inp == "r":
            create_workout()
        elif inp == "p":
            preset = pick_preset()
            create_workout(preset)
        elif inp == "o":
            options()
        elif inp == ".":
            print("\n[i] Data saved! Returning to menu...")
            return
        else:
            print("  ^ Invalid input!")

# Script coded by Jimi Hamilton in Morocco, May/Jun 2025