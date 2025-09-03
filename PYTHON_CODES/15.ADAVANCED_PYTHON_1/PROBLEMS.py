# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any of these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with open('file_1.txt') as f1:
        print(f1.read())
except Exception as e:
    print(e)

try:   
    with open('file_2.txt') as f2:
        print(f2.read())
except Exception as e:
    print(e)

try:
    with open('file_3.txt') as f3:
        print(f3.read())
except Exception as e:
    print(e)

print("Thank You")

# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1,2,3,4,5,6,7,8,9,10]

for i,item in enumerate(l):
    if (i==2 or i==4 or i==6):
        print(item)

# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered

n = int(input("Enter a number :-  "))

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [f"{n}x{i}={n*i}" for i in l1 ]
# print(l2)

# OR

table = [f"{n}x{i}={n*i}" for i in range(1,11)]
print(table)

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the 'ZeroDivisionError'.

try:
    a = int(input("Enter a :- "))
    b = int(input("Enter b :- "))
    print(f"The division of a/b is = {a/b}")
except ZeroDivisionError as Z:
    print(f"{Z} : infinite ")
except Exception as e:
    print(e)

# OR

# a = int(input("Enter a :- "))
# b = int(input("Enter b :- "))

# if (b == 0):
#     raise ZeroDivisionError ("Numbers can not b divide by zero...it will be infinite...")
# else:
#     print(f"The division of a/b is = {a/b}")

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt

n = int(input("Enter a number :-  "))

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [f"{n}x{i}={n*i}" for i in l1 ]

print(l2)

with open("Tables.txt","a") as f:
    f.write(str(l2) + "\n")
