import random
a=int(input("Enter the lower bound"))
b=int(input("enter the upper bound"))
c=int(input('enter the number of guess'))
r=random.randint(a,b)
count=0
while count<c:
    count=count+1
    i=int(input("Guess the number"))
    if(i==r):
        print("congratulations,You guessed it correctly.")
        break
    elif(i>r):
        print("You guessed higher number.")
    elif(i<r):
       print("you guessed small number.")    
if(c==count):
       print("Your chances are over.")
      