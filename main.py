from Factory.tec import Tec

def display_menu():
    print("---------------------------")
    print("[1] Opret lærer")
    print("[2] Opdater lærer")
    print("[3] Opret elev")
    print("[4] Vis list af alle lærer")
    print("[5] SAVE and EXIT")


def main():
    tec_system = Tec()

    while True:
        display_menu()
        choice = input("Vælg 1, 2, 3, 4, eller 5: ")
    
        if choice == '1':
            tec_system.add_teacher()
        elif choice == '2':
            tec_system.update_teacher()
        elif choice == '3':
            tec_system.add_student()
        elif choice == '4':
            tec_system.show_all_teachers()
        elif choice == '5':
            tec_system.save_and_exit()
        else:
            print("Du skal vælge et tal mellem 1 og 5.")


if __name__ == "__main__":
    main()