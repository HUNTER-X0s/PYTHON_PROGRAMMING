# 1. Write a program using functions to find greatest of three numbers. 
def greatest(a,b,c):
    if(a>b and a>c):
       print("a is greater")
    elif(b>c and b>a):
       print("b is greater")
    elif(c>a and c>b):
       print("c is greater")

greatest(1,256,38)




# 2. Write a python program using function to convert Celsius to Fahrenheit. 
def cel_to_far(c):
    return (9/5)*c+32

f = cel_to_far(37)
print(round(f,2))


# 3. How do you prevent a python print() function to print a new line at the end. 
print("*",end="")
print("*",end="")


# 4. Write a recursive function to calculate the sum of first n natural numbers. 
def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return sum(n-1)+n

print(sum(4))


# 5. Write a python function to print first n lines of the following pattern: 
# for n=3 
# ***
# **
# *
def pattern(n):
    if(n==0):
        return
    else:
        print("*"*n)
        pattern(n-1)
pattern(5)


# 6. Write a python function which converts inches to cms. 
def inch_to_cm(n):
    return n*(2.54)
inch_to_cm(6)


#7.Write a python function to remove a given word from a list and strip it at the same time. 
def remove(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["harry","rohan","shubham","an"]
print(remove(l,"an"))

# 8. Write a python function to print multiplication table of a given number. 
def table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
table(5)
