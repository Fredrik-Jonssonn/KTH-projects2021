import hemligasprak


def main():
    menu = {"1": (lambda text: hemligasprak.visk(text), "Viskspråket"),
                "2": (lambda text: hemligasprak.rovar(text), "Rövarspråket"),
                "3": (lambda text: hemligasprak.bebis(text), "Bebisspråket",),
                "4": (lambda text: hemligasprak.all(text), "Allspråket"),
                "5": (lambda text: hemligasprak.fikon(text), "Viskspråket")}
    while True:
        print("Vilket språk önskas? \n"
              "1. Viskspråket  2. Rövarspråket \n"
              "3. Bebisspråket  4. Allspråket \n"
              "5. Fikonspråket  6. Avsluta programmet")
        choice = input()
        if choice in menu.keys():
            text = input("Din mening: ")
            print(menu[choice][1] + ": " + menu[choice][0](text))
            input("Tryck på enter för att fortsätta.")
        elif choice == "6":
            print("Hej då")
            break
        else:
            print("Felaktig inmatning, försök igen")


if __name__ == '__main__':
    main()
