def getlines(filename):
    try:
        file = open(filename, "r") 
        lines = []
        for i in file:
            lines.append(i.strip()) 
        return lines
        
    except FileNotFoundError: 
        input("File name not found! Enter anything to exit: ")
        exit()

    

name = input("Enter file name: ")
lines = getlines(name)

num = 1
while num != 0:
    print("There are {} lines in {}".format(len(lines) - 1, name))
    num = int(input("Enter line number (or 0 to exit): "))
    if num == 0:
        break # end the while loop
    elif num < 0:
        print("Number cannot be negative!") 
    elif num >= len(lines):
        print("Number is greater than the amount of lines!") 
    else:
        print("Line {}: {}".format(num, lines[num - 1])) 

