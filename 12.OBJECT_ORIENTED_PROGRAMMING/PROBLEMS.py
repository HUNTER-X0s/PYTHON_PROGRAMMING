# 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft. 

class Programmer:
    company = "microsoft"
    language = "python"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Anurag swain","120000","751002")
print(p.name," | ",p.company," | ",p.language," | ",p.salary," | ",p.pin)
r = Programmer("rashi swain","100000","751002")
print(r.name," | ",r.company," | ",r.language," | ",r.salary," | ",r.pin)


# 2. Write a class "calculator" capable of finding square, cube and square root of a number.

class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n ** (1/2)}")

n = int(input("Enter a number :- "))
c = calculator(n)
c.square()
c.cube()
c.squareroot()

# 3. Create a class with a class attribute a; create an object from it and set "a" directly using object.a = 0. Does this change the class attribute?

class Attribute:
    a = 1
A = Attribute()
print(A.a) # prints the class attribute because the class attribute is not present.

A.a = 0 # Instance attribute is set.

print(A.a) # prints the instance attribute because the instance attribute is not present.

print(Attribute.a) #prints the class attribute
# No it doesnot change the class attribute...

# 4. Add a static method in problem 2, to greet the user with hello.

class calculator:
    @staticmethod
    def greet():
        print("Hello")

    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n * self.n}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n * self.n * self.n}")
    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n ** (1/2)}")

n = int(input("Enter a number :- "))
c = calculator(n)
c.greet()
c.square()
c.cube()
c.squareroot()


# 5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def ticketBook(self,from_P,to_P):
        print(f"Ticket is booked in train no : {self.trainNo} from {from_P} to {to_P}")

    def getStatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self,from_P,to_P):
        print(f"Ticket fare in train no : {self.trainNo} from {from_P} to {to_P} is {randint(200,8555)}")

T = Train(18025)
T.ticketBook("bombay","bhopal")
T.getStatus()
T.getFare("bombay","bhopal")


# 6. Can you change the self-parameter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects.

class parameter:
    name = "Anurag"
    def change(slf):
        print(f"My name is {slf.name}")

N = parameter()
N.change()