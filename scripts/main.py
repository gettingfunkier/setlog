def menu():
        print(f"\nSETLOG")
        print(f"-"*25)
        print(f"   [1] Generator  | Random workout\n   [2] Planner    | Manual setup\n   [3] Logger     | Track progress\n\n   [Q] Quit\n")

def main():
    while True:
        menu()
        pointer = input("> ").lower().strip()
        if pointer == "1":
            from generator import generate
            generate()
        elif pointer == "2":
            from creator import create
            create()
        elif pointer == "3":
            from logger import log
            log()
        elif pointer == "q":
            print(f"\nExiting...")
            return
        else:
            print("  ^ Invalid input!")
            
main()

# Code by gettingfunkier/Jimi Hamilton, 2024/25