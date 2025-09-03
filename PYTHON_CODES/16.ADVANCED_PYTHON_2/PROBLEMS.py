# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

# RUN THIS SCRIPT IN YOUR TERMINAL

# -> pip install virtualenv
# -> virtualenv env1
# -> virtualenv env2
# -> ./env1/scripts/activate.ps1
# -> pip install pyjokes
# -> pip install pyttsx3
# -> pip install pandas
# -> pip freeze > requirements.txt
# -> deactivate
# -> ./env2/scripts/activate.ps1
# -> pip install -r requirements.txt

# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below: "The name of the student is Harry, his marks are 72 and phone number is 99999888"

name = input("Enter your name :- ")
marks = int(input("Enter your marks :- "))
phoneNo = int(input("Enter your phoneNo :- "))

FORMAT = "The name of the student is {0}, his marks are {1} and phone number is {2}".format(name,marks,phoneNo)
print(FORMAT)

# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

list = [f"{7}x{i}={7*i}" for i in range(1,11)]

result = "\n".join(list)
# print(result)

# 4. Write a program to filter a list of numbers which are divisible by 5.

f = lambda x:x%5 == 0
l = [4*i for i in range(1,61)]

# print(l)
print(list(filter(f,l)))


# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

f = lambda a,b:a if a>b else b
l = [i for i in range(0,11)]
print((reduce(f,l)))

# OR

def greater(a,b):
    if(a>b):
        return a
    return b
l = [111,567,67,34]
print((reduce(greater,l)))

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

# RUN THIS SCRIPT IN YOUR TERMINAL

# -> pip install virtualenv
# -> virtualenv env1
# -> ./env1/scripts/activate.ps1
#  -> deactivate
# -> virtualenv env6
# -> ./env6/scripts/activate.ps1
# -> pip install -r .\requirements.txt

# 7. Explore the 'Flask' module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()
