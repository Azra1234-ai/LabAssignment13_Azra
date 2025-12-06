def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: You do not have permission to open this file.")
    except Exception as e:
        print("An unexpected error occurred:", e)

print(read_file("sample.txt"))

