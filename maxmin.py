numbers = [2, 4, 1, 0, 2, -1]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print([smallest, largest])