#1 Wap to create a dictionary of hindi words with values as their english translation.provide user with an option to look it up !
dictionary = { 
     "pyaar":"love",
     "paani":"water",
     "tamatar":"tomato"
    }
meanings = input("enter a word[key] from the above to get the meaning[value]")
print(dictionary["meanings"])


#2 Wap to input 8 numbers from the user and display all the unique numbers (once).
set = set()
n1=int(input("enter number :"))
set.add(n1)
n2=int(input("enter number :"))
set.add(n2)
n3=int(input("enter number :"))
set.add(n3)
n4=int(input("enter number :"))
set.add(n4)
n5=int(input("enter number :"))
set.add(n5)
n6=int(input("enter number :"))
set.add(n6)
n7=int(input("enter number :"))
set.add(n7)
n8=int(input("enter number :"))
set.add(n8)
print(set)


#3 can we have a set with 8(int) and "8"(str) as a value in it?
set={8,"8"}
print(set)  #yes


#4 What will be the length of the following set s :
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20') ...length of these after these operations?
s=set() 
s.add(20) 
s.add(20.0)
s.add('20')
print(s)
print(len(s))   #-->2

#5 s={}.... what is the type of 's'?
s={}
print(type(s))  # ->dictionary


#6 Create an empty dictionary.Allow 4 friends to enter their favourite language as value and use keys as their names.Assume that their names are unique.
dictionary={}
name=input("enter name : ")
language=input("enter language : ")
dictionary.update({name:language})
name=input("enter name : ")
language=input("enter language : ")
dictionary.update({name:language})
name=input("enter name : ")
language=input("enter language : ")
dictionary.update({name:language})
name=input("enter name : ")
language=input("enter language : ")
dictionary.update({name:language})
print(dictionary)  


#7 If the names of two friends are same;what will happen to the program in problem 6?
'''--> As dictionary can't have same keys...it will update the previous value to new value of the same key
'''

#8 If languages of two friends are same;what will happen to the program in problem 6?
'''--> ok...dictionary can have same values
'''

#9 Can you change the values inside the list which is contained in set s?{8,7,2,"harry",[1,2]}
s={8,7,2,"harry",[1,2]}
'''--> No, because  sets are unordered and unindexed

and 1st of all we cants include lists as an element in sets'''