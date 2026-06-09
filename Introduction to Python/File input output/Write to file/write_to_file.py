zoo = ["lion", "elephant", "monkey"]
number = 15

with open("output.txt", 'a') as f:
    # Write a new line symbol into a file, along with all elements from the zoo list, joined by " and "
    # Write a new line symbol and the value of the number variable into a file
    f.write('\n' + ' and '.join(zoo) + '\n')
    f.write(f'{number}')
