import random
'''1 for s
-1 for r
0 for p
'''
computer=random.choice(['s','p','r'])
l=['s','p','r']
user_choice=input("choose among(rock,paper, or scissors?)(r/p/s)").lower()
#if user_choice!='r' and user_choice!='s' and user_choice!='p':
    #print("invalid error")
if user_choice in l:
    print(f'you choose:{user_choice} and computer choose:{computer}')

    if(computer==user_choice):
        print("its a draw")
    elif(computer=='s' and user_choice=='r') :
        print("you win")  
    elif(computer=='s' and user_choice=='p') :
        print("you loose")   
    elif(computer=='r' and user_choice=='p') :
        print("you loose")  
    elif(computer=='r' and user_choice=='s') :
        print("you loose")  
    elif(computer=='p' and user_choice=='s') :
        print("you win") 
    elif(computer=='p' and user_choice=='r') :
        print("you win")   
                   

else:
    print("invalid choice!")    


  
