#1 Wap to display a user entered name followed by good afternoon using input() function.
Name = input("enter your name : ")
print("good afternoon"+Name +"")
# OR
print(f"good afternoon ,{Name}")


# 2 Wap to fill in a letter template with name and date.
# Letter='''Dear <|Name|>,
#           You are selected!
#           <|Date|>
#        '''
letter=''' Dear <|Name|>,
           You are selected!
           <|Date|>'''
print(letter.replace("<|Name|>","Anurag").replace("<|Date|>","24 march 2018"))


# 3 Wap to detect double space in a string.
letter = "anurag  i love  you very  much"
print(letter.find("  "))


#4 Replace the double space from problem 3 with single spaces.
letter ="anurag  i love  you very  much"
print(letter.replace("  "," "))


#5 Wap to format a letter using escape sequence characters.
letter = "Dear harry,\n \tThis python course is nice.\n Thanks !!"
print(letter)