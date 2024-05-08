def median(numbers):
    n = len(numbers)
    sort = sorted(numbers)

    if(len(numbers)%2 == 0): #if even
        mid1 = n//2
        mid2 = mid1-1
        median = (sort[mid1] + sort[mid2])/2
    else:
        mid = n//2
        median = sort[mid]
    
    print("Median: " + str(median))

def mode(numbers):
    counter = 0
    num = numbers[0]

    for i in numbers:
        num_count = numbers.count(i)
        if(num_count > counter):
            counter = num_count
            num = i
    
    print("Mode: " + str(num))

def mean(numbers):
    i = 0
    sum = 0
    while(i != len(numbers)):
        sum = sum + numbers[i]
        i = i + 1
    
    mean = float(sum/len(numbers))
    print("Mean: " + str(mean))


numbers = []
while True:
    try:
        num = int(input("Enter a number (or '!' to finish): "))
        numbers.append(num)
    except ValueError:
        if input("Are you done entering numbers?(y/n): ").lower() == "y":
            break

median(numbers)
mode(numbers)
mean(numbers)
