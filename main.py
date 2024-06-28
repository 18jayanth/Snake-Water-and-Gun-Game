""" We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user."""
""" 1 for snake
    0  for water
    -1  for gun"""
import random
computer=random.choice([-1,0,1])
yourstr=input("Enter your choice::")
dict1={"s":1,"w":0,"g":-1}
you=dict1[yourstr]
revdict1={1:"snake",0:"water",-1:"gun"}
print(f"You choose {revdict1[you]}  and the  computer {revdict1[computer]}")
if(computer==you):
    print("draw")
else:
    if(computer==1 and you ==0):
        print("You lose")
    elif(computer==1 and you==-1):
        print("You win")
    elif(computer==0 and you==-1):
        print("You lose")
    elif(computer==0 and you==1):
        print("You win")
    elif(computer==1 and you==-1):
        print("You win")
    else:
        print("You lose")
    
    
    

    
    