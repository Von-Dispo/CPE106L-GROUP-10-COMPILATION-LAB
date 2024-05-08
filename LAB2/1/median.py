def main(numbers):
    if not numbers:
        print("The list is empty.")
        return 0
    else:
        midpoint = len(numbers) // 2
        print("The median is", end=" ")
        if len(numbers) % 2 == 1:
            print(numbers[midpoint])
        else:
            print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
