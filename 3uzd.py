def print_lines_3_4(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 3:
            print("Trešā rinda:", lines[2].strip())
        if len(lines) >= 4:
            print("Ceturtā rinda:", lines[3].strip())