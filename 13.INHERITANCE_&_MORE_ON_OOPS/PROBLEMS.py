# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class vector_2D:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i+ {self.j}j")

class vector_3D(vector_2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i+ {self.j}j+ {self.k}k")
        
x = vector_2D(3,4)
x.show()
v = vector_3D(2,4,5)
v.show()

# 2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from "Pets'. Add a method 'bark' to class 'Dog'.

class Animals:
    @staticmethod
    def walk():
        print("A animal walks")
class Pets(Animals):
    @staticmethod
    def eats():
        print("A pet animal eats")
class Dogs(Pets):
    @staticmethod
    def bark():
        print("A dog barks")

A = Animals()
A.walk()
P = Pets()
P.eats()
D = Dogs()
D.bark()

# 3. Create a class 'Employee' and add salary and increment properties to it. Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 1200000
    increment = 30
    @property
    def slryAftrIncrmnt(self):
        return (self.salary + self.salary * (self.increment/100))
    @slryAftrIncrmnt.setter
    def slryAftrIncrmnt(self,salary):
        self.increment = ((salary/self.salary)-1)*100

E = Employee()
print(E.slryAftrIncrmnt)
E.slryAftrIncrmnt = 1560000
print(E.increment)

# 4. Write a class 'Complex' to represent complex numbers, along with overloaded operators "+" and "*" which adds and multiplies them.

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self,c2):
        return complex(self.r + c2.r, self.i + c2.i)
    def __mul__(self,c2):
        return Complex(self.r * c2.r - self.i * c2.i,self.r * c2.i + self.i * c2.r)
    # def __str__(self):
    #     return f"{self.r} + {self.i}i"

c1 = complex(1,2)
c2 = complex(3,4)
print(c1 + c2)
print(c1 * c2)

# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,v2):
        return Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)
    def __mul__(self,v2):
        return self.x * v2.x + self.y * v2.y + self.z * v2.z
    def __str__(self):
        return f"vector({self.x},{self.y},{self.z})"
    
V1 = Vector(1,2,3)
V2 = Vector(4,5,6)
V3 = Vector(7,8,9)

print(V1 + V2) 
print(V1 * V2)

print(V1 + V3) 
print(V1 * V3)

# 6. Write __str__() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
V = Vector(7,8,10)
print(V) 

# 7. Override the __len__() method on vector to display the dimension of the vector.

class Vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
V = Vector([1,2,3])

print(len(V))