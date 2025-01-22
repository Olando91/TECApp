from Factory.tec import Tec

def display_menu():
    print("---------------------------")
    print("[1] Opret lærer")
    print("[2] Opdater lærer")
    print("[3] Opret elev")
    print("[4] Opdater elev")
    print("[5] Vis list af alle lærer")
    print("[6] SAVE and EXIT")


def main():
    tec_system = Tec()

    while True:
        display_menu()
        choice = input("Vælg 1, 2, 3, 4, 5 eller 6: ")
    
        if choice == "1":
            tec_system.add_teacher()
        elif choice == "6":
            tec_system.save_and_exit()

if __name__ == "__main__":
    main()