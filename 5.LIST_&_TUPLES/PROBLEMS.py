#1 Wap to store seven fruits in a list entered by the user.
list=[]
f1=input("enter a fruit : ")
list.append(f1)
f2=input("enter a fruit : ")
list.append(f2)
f3=input("enter a fruit : ")
list.append(f3)
f4=input("enter a fruit : ")
list.append(f4)
f5=input("enter a fruit : ")
list.append(f5)
f6=input("enter a fruit : ")
list.append(f6)
f7=input("enter a fruit : ")
list.append(f7)
print(list)


#2 Wap to accept marks of 6 students and display them in a sorted order.
list=[]
s1=int(input("enter marks: "))
list.append(s1)
s2=int(input("enter marks: "))
list.append(s2)
s3=int(input("enter marks: "))
list.append(s3)
s4=int(input("enter marks: "))
list.append(s4)
s5=int(input("enter marks: "))
list.append(s5)
s6=int(input("enter marks: "))
list.append(s6)
list.sort()
print(list)


#3 Check that a tuple type cannot be changed in python.
a=(7,0,8,0,0,9)
a[1]=3

#4 Wap to sum a list with 4 numbers.
list=[1,2,3,4]
sum=list[0]+list[1]+list[2]+list[3]
print(sum)
#or
print(sum(list))

#5 Wap to count the number of zeroes in the following tuple. a=(7,0,8,0,0,9)
a=(7,0,8,0,0,9)
print(a.count(0))