# SNAKE, WATER, GUN *__GAME__*

import random 

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
yourChoice = input("Enter Your Choice({For 'Snake' Enter 's'}{For 'water' Enter 'w'}{For 'gun' Enter 'g'}) :- ")
youDict  = {"s":1, "w":-1, "g":0}
you = youDict[yourChoice]
reverseDict = {1:"snake", -1:"water", 0:"gun"}
print(f"You Choose {reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer == yourChoice):
    print("It's a Draw....Try Again")

else:
    if(computer == 1 and you == 0):
        print("congrats! \n You Win!")
    elif(computer == -1 and you == 1):
        print("congrats! \n You Win!") 
    elif(computer == 0 and you == -1):
        print("congrats! \n You Win!") 
    elif(computer == 1 and you == -1):
        print("Oops! \n You Lose!") 
    elif(computer == -1 and you == 0):
        print("Oops! \n You Lose!")  
    elif(computer == 0 and you == 1):
        print("Oops! \n You Lose!") 
    else:
        print("Something Went Wrong!!")

# --------------------------------------------------------------------------

# OR

# --------------------------------------------------------------------------

# SNAKE, WATER, GUN *__GAME__*

import random 

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1,0,1])
yourChoice = input("Enter Your Choice({For 'Snake' Enter 's'}{For 'water' Enter 'w'}{For 'gun' Enter 'g'}) :- ")
youDict  = {"s":1, "w":-1, "g":0}
you = youDict[yourChoice]
reverseDict = {1:"snake", -1:"water", 0:"gun"}
print(f"You Choose {reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer == yourChoice):
    print("It's a Draw....Try Again")

else:
    
# The logic is written on the basis of the value of computer - you .

    if((computer - you) == -1 or (computer - you) == 2 ):
        print("Oops! \n You Lose!")
    else:
        print("congrats! \n You Win!")


#     if(computer == 1 and you == 0):
#         print("congrats! \n You Win!") #computer - you = 1
#     elif(computer == -1 and you == 1):
#         print("congrats! \n You Win!") #computer - you = -2
#     elif(computer == 0 and you == -1):
#         print("congrats! \n You Win!") #computer - you = 1
#     elif(computer == 1 and you == -1):
#         print("Oops! \n You Lose!")    #computer - you = 2
#     elif(computer == -1 and you == 0):
#         print("Oops! \n You Lose!")    #computer - you = -1
#     elif(computer == 0 and you == 1):
#         print("Oops! \n You Lose!")    #computer - you = -1
#     else:
#         print("Something Went Wrong!!")
      
