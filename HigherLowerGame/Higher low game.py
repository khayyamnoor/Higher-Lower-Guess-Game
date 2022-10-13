

#WEAK SPOTS PROBLEMS + NEW TRICKS AND TIPS LEARNED IN THIS PROJECT:
#--------------------------------------------------------


# USUALLY FACE PROBLEMS DURING SETTING UP A FLAG WITH A LOOP, DURING REPITITION 
# AFTER WRITING FUNCTIONS MOVE THEM UPWARD AND CALL THEM WITHIN THE WHILE LOOP
# LEARNED A NEW TRIP TO RE-ASSIGN OPTION B TO OPTION-A
# ITS BETTER TO RETURN TRUE FALSE AND RE-ASSIGN IT TO A VARIABLE RATHER THEN RETURN A STRING BASED OUTPUT

#----------------------------------------------------------
from art import logo
from art import vs
from game_data import data
import random
import os 

print(logo)

def check(account):
  account_name=account['name']
  account_des=account['description']
  account_country=account['country']
  return (f"{account_name}, {account_des}, {account_country}. ")

def great(guess,accounta,accountb):
  count_a=accounta['follower_count']
  count_b=accountb['follower_count']
  # print((f"{count_a} Million, {count_b} Million"))
  if guess=="a" and count_a > count_b:
    return True
  elif guess=="a" and count_b > count_a:
    return False
  elif guess=="b" and count_a > count_b:
    return False
  elif guess=="b" and count_b > count_a:
    return True
  
score=0
game_continue=True
account_b=random.choice(data)

while game_continue: 
  account_a=account_b
  account_b=random.choice(data)

  
  while account_a==account_b:
    account_b=random.choice(data)
    
  print("Compare A: ",check(account_a))
  print(vs)
  print("Compare B: ",check(account_b))
      
    
  guess1=input("Who hass more followers? Type 'A' or 'B' : ").lower()
  
  is_correct=great(guess1,account_a,account_b)
  #clear and print logo
  os.system('cls||clear')
  print(logo)
    #make a score count
  if is_correct:
    score+=1
    print(f"Your Right! Current Score: {score}")
      
  else:
    game_continue=False
    os.system('cls||clear')
    print(f"Your Wrong! Final Score: {score}")
