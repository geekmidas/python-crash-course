# 1. Assuming you will be given a file (Empty or not),
# write a program that will read the file and print the
# contents of the file to the screen
data = open('data.txt')
contents = data.read()
size = len(contents)
print(contents)

# 2. If the file from 1 is Empty print out “FILE IS EMPTY”
# to the screen. Otherwise print the contents of the file
if size == 0:
    print('FILE IS EMPTY')
else:
    print(contents)
# 3. Using the same file from 1, if the contents of
# 1 has an even length and the file is not empty
# print out “THE FILE IS OF EVEN LENGTH {}”
# otherwise print “THE FILE HAS LENGTH {}”
if size % 2 == 0 and size != 0:
    print(F"THE FILE IS OF EVEN LENGTH {size}")
elif size == 0:
    print('FILE IS EMPTY')
else:
    print(F"THE FILE HAS LENGTH {size}")

# 4. Create a separate program from the question above.
# 4.1 Taking a file name as input, use the
# input to open the file and print the contents to the screen.