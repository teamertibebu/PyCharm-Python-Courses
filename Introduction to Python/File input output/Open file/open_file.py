with open('input.txt', 'r') as my_file:
    # Some action performed with the file, the read() method explained later.
    print(my_file.read(), '\n')


with open('input1.txt', 'r') as file:
    outfile_name = file.readline()


outfile = open('outfile.txt', 'w')  # Opening the file in write mode (using the `w` argument)
outfile.write('Hello World')  # Writing to the file, the write() method is explained later.
# Close the output file!
outfile.close()