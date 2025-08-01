# Using fh for file handler to ope a file for reading
fh = open('./samples/testreading.txt', 'r')

# print the contents of the file
for line in fh:
    print(line)