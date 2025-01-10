#ask the user to roll the dice
import random
while True:
 choice = input("do you want to roll the dice?(y/n):").lower()
 if choice =='y' :
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f"{die1},{die2}")

 elif choice=='n':
    print("thankyou for playing")
    break


 else :
   print("invalid choice")


