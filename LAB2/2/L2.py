def inputFile(userInput):
    try:
        with open(userInput, "r") as file:  
            lines = [None]
            for line in file:
                lines.append(line.strip())
    except ValueError:
        print("Enter a valid text file.")

    return lines

print("Enter the file name in the given prompt below. It must be in the same folder as the python file. \n")
userInput = input("Enter filename: ")
textLine = inputFile(userInput)

userNum = 1
while True:
    userNum = int(input("Enter a line in the text file (input '0' to quit): "))
    if userNum == 0:
        break

    if userNum < 1 or userNum >= len(textLine):
        print("Invalid input: line number must be between 1 and", len(textLine)-1)
    else:
        print("Line", userNum, ":", textLine[userNum], "\n")

