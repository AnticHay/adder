
import random
x = random.random()
print (x)
y = random.randint(0,10)
print (y)

moves = ["rock","paper","scissors"]

for i in range (5):
  player = int(input ("rock (0), paper (1), scissors (2)? ") )
  ai =random.randint (0,3) 
  if  ai == player: 
    print ("draw you both did ",moves[ai])
  elif player == 0 and ai == 2: #player is rock and ai is scissors
    print ("you win, ai did ", moves[ai])
  elif player ==1 and ai == 0:
    print("you win , ai did", moves[ai])
  elif player == 2 and ai ==1: 
    print ("you win , ai did ", moves[ai])
  else:
    print ("you lost", moves [ai])
