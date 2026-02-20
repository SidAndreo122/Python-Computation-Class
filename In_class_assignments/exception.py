try:
    filename = input("Enter filename: ")
    infile = open(filename, "r")
    line = infile.readline()
    value = int(line)
except IOError:
    print("Error: file not found.")
except ValueError as exception:
    print("Error:", str(exception))