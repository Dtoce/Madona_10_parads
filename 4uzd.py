def read_file_content():
    try:
        file_name = input("Ievadiet faila nosaukumu: ")
        file_extension = input("Ievadiet faila formātu (paplašinājumu): ")
        
        file_path = f"{file_name}.{file_extension}"

        with open(file_path, 'r') as file:
            content = file.read()
            print("Faila saturs:")
            print(content)
    
    except FileNotFoundError:
        print(f"Kļūda: Faila {file_path} nav atrasts.")
    except IOError:
        print(f"Kļūda: Neizdevās nolasīt failu {file_path}.")
    except Exception as e:
        print("Radās neparedzēta kļūda:", e)