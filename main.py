import random
'''
1 for snake
-1 for water 
0 for gun
'''
computer=random.choice([1,0,-1])
youstr=input("enter yourchoice:" )
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}

you=youDict[youstr]

print(f"you chose {reverseDict[you]}\n computer chose{reverseDict[computer]}")
if(computer==you):
    print("its draw")
else:
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you win!")
    elif(computer==1 and you==-1):
        print("you lose!")
    elif(computer==0 and you==1):
        print("you win!")
    elif(computer==0 and you==-1):
        print("you lose!")
    elif(computer==1 and you==0):
        print("you lose!")

    else:
        print("something went wrong")
        '''
        if((computer-you)==-1 or (computer-you)==2):
        print("you lose)
        else:
        print("you win)
        '''