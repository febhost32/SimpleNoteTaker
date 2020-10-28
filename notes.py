# This is a simple program python that takes user input into a file,
# and then prints the saved input
# By Febhost32

print("========== NOTE TAKER ========== \n \n")
file = open("words.txt", "r+")

words = []
selection = "r"

for line in file:
    words.append(line.strip())

selection = input("Selection (r/a/s)? ")
print("\n")

while selection != "s":
    if selection == "r":
        file = open("words.txt", "r+")
        for line in file:
            words.append(line.strip())
        print('\n'.join(words))
        print("\n")
        selection = input("Selection (r/a/s)? ")
        print("\n")
    elif selection == "a":
        print("Insert your words here : ")
        file = open("words.txt", "r+")
        file.seek(0)
        file.truncate(0)
        add = input()
        file.write(add)
        file.close()
        print("Words added! \n")
        selection = input("Selection (r/a/s)? ")
        print("\n")
    else :
        break

file = open("words.txt", "r+")
file.seek(0)
file.truncate(0)
file.close()
