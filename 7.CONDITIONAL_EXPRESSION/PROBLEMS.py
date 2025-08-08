#1. Write a program to find the greatest of four numbers entered by the user. 
n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
n3=int(input("enter number 3: "))
n4=int(input("enter number 4: "))
if(n1>n2 and n1>n3 and n1>n4):
    print("n1 is greater than n2 , n3 and n4",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("n2 is greater than n1 , n3 and n4",n2)
elif(n3>n1 and n3>n2 and n3>n4):
    print("n3 is greater than n2 , n1 and n4",n3)
elif(n4>n1 and n4>n2 and n4>n3):
    print("n4 is greater than n2 , n3 and n1",n4)
else:
    print("invalid")

#2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 
marks1=int(input("enter marks 1: "))
marks2=int(input("enter marks 2: "))
marks3=int(input("enter marks 3: "))
percentage=((marks1+marks2+marks3)*100)/300
if(percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("pass",percentage)
else:
    print("fail",percentage)


#3. A spam comment is defined as a text containing following keywords: 
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams. 
a="Make a lot of money"
b="buy now"
c="subscribe this"
d= "click this"
message=input("Enter your comment")
if((a in message) or (b in message) or (c in message) or (d in message)):
    print("spam comments")
else:
    print("comments")


#4. Write a program to find whether a given username contains less than 10 characters or not.
username=input("Enter your username")
if(len(username)<10):
    print("username is of less than 10 charcters")
else:
    print("username is of more than or equal to 1 0 charcters")

#5. Write a program which finds out whether a given name is present in a list or not. 
list=["omm","pratyush","sangram","harsh","sinu","ashutosh","saroj"]
name=input("enter your name")
if(name in list):
    print("present")
else:
    print("absent")


#6. Write a program to calculate the grade of a student from his marks from the following scheme: 
# 90-100 =>Ex 
# 80-90 =>A 
# 70-80 =>B 
# 60-70 =>C 
# 50-60 =>D 
# <50 =>F 
marks=int(input("enter marks"))
if(90 <= marks <= 100):
    print("EX")
elif(80 <= marks < 90):
    print("A")
elif(70 <= marks < 80):
    print("B")
elif(60 <= marks < 70):
    print("C")
elif(50 <= marks < 60):
    print("D")
elif(marks < 50):
    print("F")
else:
    print("invalid grade")


#7. Write a program to find out whether a given post is talking about "Harry" or not. 
post=input("enter something : ")
if("harry".lower() in post.lower()):
    print("talking about harry")
else:
    print("not talking about harry")