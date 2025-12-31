text = input("Enter text to write to the file: ")

with open("Output.txt","wt") as fh :
    fh.write(text)
print("Data successfully written to Output.txt.")


append = input("\nEnter additional text to append: ")
with open("Output.txt","at") as fh:
    fh.write("\n" + append)
print("Data successfully appended.")

print("\nFinal content of Output.txt :")
with open("Output.txt","rt") as fh:
    line1 = fh.readline().strip()
    line2 = fh.readline().strip()

print(line1)
print(line2)