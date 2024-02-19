def write_name_to_file():
    try:
        user_name = input("Ievadiet savu vārdu: ")

        with open("lietotajs.txt", "w") as file:
            file.write(user_name)

        print("Vārds veiksmīgi ierakstīts failā 'lietotajs.txt'.")

    except IOError:
        print("Kļūda: Neizdevās ierakstīt failā.")
    except Exception as e:
        print("Radās neparedzēta kļūda:", e)