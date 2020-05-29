# 4. Create a separate program from the question above.
# 4.1 Taking a file name as input, use the
# input to open the file and print the contents to the screen.
name = input("Enter the file name: ")
data = open(name)
print(data.read())