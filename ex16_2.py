from sys import argv

script, filename = argv

print("Press Enter to read the file that was created in exercise 16")
print("Press CTRL-C to exit")

input("?")

target = open(filename, 'r')

#READING =/= PRINTING
print(target.read())
