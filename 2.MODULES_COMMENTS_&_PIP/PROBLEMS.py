#1 write a program to print a poem in python.
print('''twinkle twinkle little star
how i wonder what you are
up above the world so high 
like a diamond in the sky''')


#2 Use REPL and print the table of 5 using it.
'''
=>using command prompt :

python
>>> 5*1
5
>>> 5*2
10
>>> 5*3
15
>>> 5*4
20
>>> 5*5
25
>>> 5*6
30
>>> 5*7
35
>>> 5*8
40
>>> 5*9
45
>>> 5*10
50
>>>
'''

#3 Install an external module and use it to perform an operation of your intrest.
# pip install pyttsx3 
import pyttsx3
engine = pyttsx3.init()
engine.say("I love you Rashi...i cant move on....")
engine.runAndWait()


#4 Write a python program to print the contents of directory using the os module.
# search online for the function which does that.
import os
directory_path = "/"  # Current directory
contents = os.listdir(directory_path)
for item in contents:
    print(item)

# OR

import os

def list_directory_contents(directory_path):
    try:
        # Get the list of all entries in the directory
        entries = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# => Example usage
#   directory_path = '/'
#   list_directory_contents(directory_path)
 

#5 Label the program with comments in problem 4.
import os

#specify the directory you want to list
directory_path = "/"  # Current directory

#list all files and directories in the specified path
contents = os.listdir(directory_path)

#print the contents of the directory
print(contents)

#print each file and directry name
# **  for item in contents:
#       print(item)