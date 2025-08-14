from random import randint
from time import sleep

print("Welcome to rock, paper, scissors! 👋\n")
sleep(2)
username = input("Enter a cool name 😎:\n")
game_round = 1
required_wins = 1
full_round = 1
user_wins = 0
computer_wins = 0
tie = 0
done = None
replay = None
print(f"\nHey {username}! Glad you're here! ☺️")
sleep(2)
understand = str(input("\nDo you know how to play?\n")).replace(" ", "").lower()

while True:
  if understand == 'yes' or understand == 'y' or understand == '1':
    break
  elif understand == 'no' or understand == 'n' or understand == '2':
    print("\nNo worries! Let's go over the rules:\n")
    sleep(2)
    print("\nThis is a guessing game 🤔\nYou're goal is to out-smart your opponent using pure luck! 🍀")
    sleep(5)
    print("\nYou have 3 tools you can pick from:\n 🪨  Rock\n 📃 Paper\n ✂️  Scissors")
    sleep(5)
    print("\nTo pick Rock, enter '1', 'r', or 'rock'")
    sleep(3)
    print("To pick Paper, enter '2', 'p', or 'paper'")
    sleep(3)
    print("To pick Scissors, enter '3', 's', or 'scissors'")
    sleep(3)
    print("\n⚠️  Be sure to pick wisely because:\n 1. Rock breaks Scissors\n 2. Scissors cut Paper\n 3. Paper covers Rock\n\nSee the pattern?")
    sleep(8)
    print("\nIf you and your opponent pick the same tool, a tie is called and another round must be performed.")
    sleep(5)
    print("The game continues until a winner is declared.\n")
    sleep(3)
    move_on = input("Enter any key to continue.")
    break
  else:
    print(f"{understand} is not a valid input.")
    understand = input("Try 'yes', 'y', '1' or 'no', 'n', '2'\n").replace(" ", "").lower()

while replay != False:
  print("\nLet's see how lucky you are.")
  sleep(2)

  while True:
    computer_choice = randint(1, 3)
    print("The computer has made a decision...\n")
    sleep(2)

    # Game Logic
    while True:
      tie_flag = False

      print("🪨  Rock")
      sleep(1)
      print("📃 Paper")
      sleep(1)
      print("✂️  Scissors")
      sleep(1)
      user_choice = input("SHOOT!\n").replace(" ", "").lower()

      if user_choice == '1' or user_choice == 'r' or user_choice == 'rock':
        if computer_choice == 1:
          tie += 1
          tie_flag = True
          print("\nYou both threw rock 🪨\n Go again!\n")
          computer_choice = randint(1, 3)
        elif computer_choice == 2:
          computer_wins += 1
          print("\nThe computer's paper covered your rock!\n You lost 😔\n")        
        else:
          user_wins += 1
          print("\nYour rock crushed the computer's scissors!\n You won! 🥳\n")
        
        if game_round == full_round and tie_flag == False:
          done = True
          break
        elif (required_wins == user_wins or required_wins == computer_wins) and tie_flag == False:
          done = True
          break
        elif tie_flag == True:
          done = False
          continue
        else:
          done = False
          game_round += 1
          print("Again!")
      
      elif user_choice == '2' or user_choice == 'p' or user_choice == 'paper':
        if computer_choice == 2:
          tie += 1
          tie_flag = True
          print("\nYou both threw paper 📃\n Go again!\n")
          computer_choice = randint(1, 3)        
        elif computer_choice == 3:
          computer_wins += 1
          print("\nThe computer's scissors cut your paper!\n You lost 😔\n")
        else:
          user_wins += 1
          print("\nYour paper covered the computer's rock!\n You won! 🥳\n")
        
        if game_round == full_round and tie_flag == False:
          done = True
          break
        elif (required_wins == user_wins or required_wins == computer_wins) and tie_flag == False:
          done = True
          break
        elif tie_flag == True:
          done = False
          continue
        else:
          done = False
          game_round += 1
          print("Again!")
      
      elif user_choice == '3' or user_choice == 's' or user_choice == 'scissors':
        if computer_choice == 3:
          tie += 1
          tie_flag = True
          print("\nYou both threw scissors ✂️\n Go again!\n")
          computer_choice = randint(1, 3)   
        elif computer_choice == 1:
          computer_wins += 1
          print("\nThe computer's rock crushed your scissors!\n You lost 😔\n")
        else:
          user_wins += 1
          print("\nYour scissors cut the computer's paper!\n You won! 🥳\n")
      
        if game_round == full_round and tie_flag == False:
          done = True
          break
        elif (required_wins == user_wins or required_wins == computer_wins) and tie_flag == False:
          done = True
          break
        elif tie_flag == True:
          done = False
          continue
        else:
          done = False
          game_round += 1
          print("Again!")
      
      else:
        print(f"\n\nWhat on earth is {user_choice}? 🤨")
        sleep(1)
        print("\nHere's a list of acceptable inputs:")
        print("For Rock: '1', 'r', 'rock'")
        print("For Paper:'2', 'p', 'paper'")
        print("For Scissors:'3', 's', 'scissors'\n")
        sleep(5)
        print("Let's try again.\n")
        sleep(2)
        done = False

    # Break Outer Loop
    if done == True:
      break

  # Play Again Logic
  if user_wins == required_wins:
    print(f"\nYou won best {required_wins} out of {full_round} 🎉\n")
  else:
    print(f"\nYou lost best {required_wins} out of {full_round} 😢\n")
  sleep(3)

  required_wins += 1
  full_round = required_wins * 2 - 1
  while True:
    play_again = input(f"\nBest {required_wins} out of {full_round}? 😈\n").replace("", "").lower()
    if play_again == 'yes' or play_again == 'y' or play_again == '1':
      replay = True
      game_round += 1
      break
    elif play_again == 'no' or play_again == 'n' or play_again == '2':
      replay = False
      print("\nThanks for playing! 😄")
      break
    else:
      print(f"{play_again} is not a valid input.")

# Show Stats
win_rate = (user_wins / game_round) * 100
print(f"\n\n{username}'s Report Card:\n 🔄 Rounds Played: {game_round}\n 👑 Rounds Won: {user_wins}\n 🎯 Win Rate: {win_rate}\n 👀 Ties: {tie}\n")
sleep(5)
if win_rate == 100 and game_round >= 3:
  print(f"{username} IS THE UNDEFEATED CHAMP! 🔥\n You earned a rare S++ 🤯")
elif win_rate >= 85:
  print(f"The odds are in {username}'s favor! You earned an A 🤩")
elif win_rate < 85 and win_rate >= 70:
  print("Well look at you go! You earned a B 🤓")
elif win_rate < 70 and win_rate >= 55:
  print("You earned a C 🤨...")
  sleep(2)
  print("But C's get degrees so it's okay! 🙂")
elif win_rate < 55 and win_rate >= 40:
  print("You are clearly a novice. You earned a D 😑")
else:
  print("You earned an F...")
  sleep(2)
  print("You are banned from playing rock, paper, scissors ever again...")
  sleep(3)
  print(f"You have been sentenced to {game_round - user_wins} years in PyPrison.")
  sleep(4)
  print(f"\n{username}, YOU HAVE OFFICIALLY BEEN BANNISHED! ❌")
