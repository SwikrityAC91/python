import random
n=random.randint(1,100)#n=number_to_guess
guesses=0
try:
    a=int(input("guess the number"))
    if(a>n):
        print("lower number please")
        guesses+=1
    elif(a<n):
        print("higher number please")
        guesses+=1
    else:    
      print(f"you have guessed the correct number{n}in {guesses }attempts")       
except ValueError:
    print("please enter valid number")
