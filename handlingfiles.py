# Using fh for file handler to ope a file for reading
fh = open('./samples/testreading.txt', 'r')

# print the contents of the file
for line in fh:
    # show special characters like newline, \n, using: repr()
    print(repr(line))    

# reset the file handler to the start of the file
fh.seek(0)

# add some space in the CLI
print("\n\n")

for line in fh:
    # remove the newline added by print by using: end = ''
    print(repr(line), end = '')

# close the file
fh.close()

# add some space in the CLI
print("\n\n")

# you can also use: with ... as ..., which will automatically close the file handler
with open('./samples/testreading.txt', 'r') as fh:
    for line in fh:
        # remove newlines at the end of the line
        print(line.rstrip())

# add some space in the CLI
print("\n\n")

# Ask for user input for file name to open
filename = input('Enter the file name to open: ')

try:
    contents = ''
    with open(filename, 'r') as fh:
        count = 0
        for line in fh:
            count += 1
            contents += line

    print('There are', count, 'lines in', filename)
    print('=============================================')
    print(contents)
except FileNotFoundError:
    # provide specific message that the file was not found
    print('This file was not found:', filename)
except PermissionError:
    # provide permission based error message
    print('You do not have permission to access the file:', filename)
except OSError as e:
    # display OSError/IOError message
    print('An I/O Error occurred:', str(e))
except Exception as e:
    #display any other type of error
    print('An unexpected error occurred:', repr(e))

# add some space in the CLI
print("\n\n")

# Now, I am going to show writing to files
# First, I'll create a file and write to it.
try :
    filename = 'samples/newfile.txt' 
    fh = open(filename, 'x')
    fh.write("This is a new file.\nThe second line in the file has this sentence.\n\nThis is good.")
    fh.close()
except FileExistsError as e:
    # The file already exists
    print(repr(e))
    print("The file, ", filename, ", already exists!")
    print("So, let's edit the existing file...\n")
except Exception as e:
    #display any other type of error
    print('An unexpected error occurred:', repr(e))

# Append some text to the existing file
# Open file with mode 'a'
writingfile = 'samples/testwriting.txt'
fh = open(writingfile, 'a')
fh.write("\n\nThis is an additional line I am adding to an existing file")
fh.close()

# Display the contents of the file
print("=====================================\n")
with open(writingfile, 'r') as fh:
    for line in fh:
        print(line)

# Replace the content of the file
# Open file with mode 'w'
with open(filename, 'w') as fh:
    fh.write("The previous contents are erased\n\nThis is a new second line.")

# Display the contents of the file
print("=====================================\n")
with open(filename, 'r') as fh:
    for line in fh:
        print(line)

