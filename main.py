from random import randint
from art import logo

easy_level = 10
hard_level = 5
#Function to check user guess against actual answer

def check_answer(guess,answer,turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess< answer:
    print("Too low")
    return turns - 1
#Choose a random number between 1 and 100

def game():
  print(logo)
  print("Welcome to the guessing game")
  answer = randint(1,100)
  print(f"Pssst, the correct answer is {answer}")
  
  
  #Make a function to make difficulty
  def set_difficulty():
    level = input("Choose a diffculty. Type 'easy' or 'hard': ")
    if level == "easy":
      return easy_level
    elif level == "hard":
      return hard_level
  
  #Let the user guess a number
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    
    #Repeat the guessing if they get it wrong
    guess = int(input("Make a guess: "))
    print(f"You have {turns} attempts remaining to guess the number ")
    
    turns = check_answer(guess,answer,turns)

    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess!= answer:
      rpint("Guess again")
  #Function to check user guess against actual answer
  
  #Track the number of turns
game()