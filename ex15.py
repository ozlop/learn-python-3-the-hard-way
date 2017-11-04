#sets argument variable condition
from sys import argv
#dictates which argument variables to look for when executing file
script, filename = argv
#sets variable txt to command 'open' argv filename
txt = open(filename)

#basic print with variable
print(f"Here's your file {filename}:")
#sets read command to txt variable, can also add variables/argv to read command
print(txt.read())

print("Type the filename again:")
file_again = input ("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
