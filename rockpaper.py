import random
more="y"
result=0
computer=""
while more=="y":
  print("enter: rock/ paper/ scissors")
  user=(input())
  result=random.randint(1,3)
  if result==1:
    computer="rock"
  elif result==2:
    computer="paper"
  else:
    computer="scissors"

  print("you= "+user+" and me= "+computer)
  if user==computer:
    print("its a draw")
  #Rock wins against scissors.
  elif user=="rock" and computer=="scissors":
    print("You win!")
  elif user=="scissors" and computer=="rock":
    print("you loss")

  #Scissors win against paper
  elif user=="scissors" and computer=="paper":
    print("You win!")
  elif user=="paper" and computer=="scissors":
    print("you loss")
   
  #Paper wins against rock.
  elif user=="Paper" and computer=="rock":
    print("You win!")
  elif user=="rock" and computer=="paper":
    print("you loss")

  print("again? (y)")
  more=input()
print("end")