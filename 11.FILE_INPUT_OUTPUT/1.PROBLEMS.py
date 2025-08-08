# 1. Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

with open("poems.txt","r") as f:
    content = f.read()
    if("twinkle".lower() in content.lower()):
        print("Given word is in the text")
    else:
        print("given word is not in the text")



# 2. The game() function in a program lets a user play a game and retums the score as an integer. You need to read a file "Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
    print("You are playing the game...")
    score = random.randint(1,100)
    # fetch the hiscore
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score : {score}")
    if(score > hiscore):
        # write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13-year old.

def table(n):
    table = ""
    for i in range(1,11):
        table += f" {n} x {i} = {n*i}\n"

    with open(f"M_TABLE/Table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    table(i)

# 4. A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ###### by updating the same file.

with open("donkey.txt","r") as f:
    content = f.read()

NewContent = content.replace("donkey","######")

with open("donkey.txt","w") as f:
    f.write(NewContent)

# 5. Repeat program 4 for a list of such words to be censored.

words = ["bastard", "bullshit", "rascal", "idiot"]

with open("words.txt","r") as f:
    content = f.read()
    
for word in words:  
    content = content.replace(word, "#" * len(word))

with open("words.txt","w") as f:
    f.write(content)


# 6. Write a program to mine a log file and find out whether it contains 'python".

with open("logfile.txt","r") as f:
    content = f.read()
    if("python".lower() in content.lower()):
        print("It contains python")
    else:
        print("It doesnot contain python")

# 7. Write a program to find out the line number where python is present from ques 6.

with open("logfile.txt","r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    content = f.readline
    if("python".lower() in line.lower()):
        print(f"It contains python in line no : {lineno}")
        break
    lineno += 1    
else:
    print("It doesnot contain python")

# 8. Write a program to make a copy of a text file "this. txt"

with open("this. txt","r") as f:
    content = f.read()

with open("this_copy.txt","w") as f:
    f.write(content)

# 9. Write a program to find out whether a file is identical & matches the content of another file.

with open("this. txt","r") as f:
    content1 = f.read()
with open("this_copy.txt","r") as f:
    content2 = f.read()
if(content1 == content2):
    print("files are identical")
else:
    print("files are not identical")

# 10. Write a program to wipe out the content of a file using python.

with open("wipeout.txt","r") as f:
    content = f.read()
with open("wipeout.txt","w") as f:
    f.write(" ")

# 11. Write a python program to rename a file to "renamed_by_python.txt.

with open("rename.txt","r") as f:
    content = f.read()
with open("renamed_by_python.txt","w") as f:
    f.write(content)