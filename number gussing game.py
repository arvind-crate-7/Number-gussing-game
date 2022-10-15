txt="This is a Number guessing game." 
print("\033[1;32m" ,txt.center(70))
print("\n\n\nYou have only 5 chance,So be careful.")
number=18
j=1
while(j<=5):
  inpu=int(input("\033[1;37mEnter number: "))
  if inpu==number :
   print("\033[1;34mcongratulations you enter right number\n","\033[1;35mYou won.") 
   if(j==1):
    print("you are genius, you guess in only one time.\n")
   break
  elif inpu<number :
   print("\033[1;35mYou Enter (lesser) Number.\n")
  else :
   print("\033[1;35mYou Enter (greater) number.\n")
  if j!=5:
    print("you have",5-j,"chance left.")
  j=j+1
if(j>5):
  print("Game over.")