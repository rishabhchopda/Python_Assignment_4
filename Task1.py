try:
    with open("sample.txt","rt") as fh:
        line1 = fh.readline().strip()
        line2 = fh.readline().strip()

    print("Reading file contents: ")
    print("Line 1: ",line1)
    print("Line 2: ",line2)

except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found")