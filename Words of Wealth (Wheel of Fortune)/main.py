"""
Words of Wealth
Created by Milaan Shah
"""
import random

print("Welcome to the Words of Wealth!")
print("")

turn = 1
choose_action = ""

vowel_list = ["a", "e", "i", "o", "u"]

letters_called_list = []

spin_amount_list = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 2500, 5000, "Bankrupt", "Bankrupt", "Lose a Turn", "Express"]

player1_total = 0
player2_total = 0
player3_total = 0

#puzzle_list = ["having fun at the beach", "What are you doing?", "playing hide and seek", "What are you doing?", "reno nevada", "On the map", "new york, new york", "On the map", "a positive attitude", "Thing", "friends in need are friends indeed", "Phrase", "figuring it out", "Phrase"]
puzzle_list = ["playing a round of miniature golf", "What are you doing?", "beach volleyball tournament", "Fun and Games", "welcome to fabulous las vegas", "Quotation", "honolulu hawaii", "On the map", "a dog chasing his tail", "Phrase", "and then there were none", "Book title", "baseball card collection", "Thing", "playing wheel of fortune with friends", "What are you doing?", "blowing up balloons", "What are you doing?", "a gold medal", "What are you wearing?", "a broad smile", "What are you wearing?", ]

puzzle = random.choice(puzzle_list)
board = ""

solved = False

#-----------------------

while puzzle_list.index(puzzle) % 2 == 1:
  puzzle = random.choice(puzzle_list)

category = puzzle_list[puzzle_list.index(puzzle)+1]

#-----------------------

for i in range(len(puzzle)):
  board = board + "-"

sample_letter = " "
sample_letter_index_list = []
for pos, char in enumerate(puzzle):
  if char == sample_letter:
    sample_letter_index_list.append(pos)
for i in range(len(sample_letter_index_list)):
  sample_x = sample_letter_index_list[i]
  board = board[:sample_x] + sample_letter + board[sample_x+1:]

sample_letter = ","
sample_letter_index_list = []
for pos, char in enumerate(puzzle):
  if char == sample_letter:
    sample_letter_index_list.append(pos)
for i in range(len(sample_letter_index_list)):
  sample_x = sample_letter_index_list[i]
  board = board[:sample_x] + sample_letter + board[sample_x+1:]

sample_letter = "&"
sample_letter_index_list = []
for pos, char in enumerate(puzzle):
  if char == sample_letter:
    sample_letter_index_list.append(pos)
for i in range(len(sample_letter_index_list)):
  sample_x = sample_letter_index_list[i]
  board = board[:sample_x] + sample_letter + board[sample_x+1:]

sample_letter = "?"
sample_letter_index_list = []
for pos, char in enumerate(puzzle):
  if char == sample_letter:
    sample_letter_index_list.append(pos)
for i in range(len(sample_letter_index_list)):
  sample_x = sample_letter_index_list[i]
  board = board[:sample_x] + sample_letter + board[sample_x+1:]

sample_letter = "!"
sample_letter_index_list = []
for pos, char in enumerate(puzzle):
  if char == sample_letter:
    sample_letter_index_list.append(pos)
for i in range(len(sample_letter_index_list)):
  sample_x = sample_letter_index_list[i]
  board = board[:sample_x] + sample_letter + board[sample_x+1:]

sample_letter = "."
sample_letter_index_list = []
for pos, char in enumerate(puzzle):
  if char == sample_letter:
    sample_letter_index_list.append(pos)
for i in range(len(sample_letter_index_list)):
  sample_x = sample_letter_index_list[i]
  board = board[:sample_x] + sample_letter + board[sample_x+1:]

print("Here is your puzzle:")
print(board)

print("")
print("The category is:", category)

# ---------------------

while solved == False:
  if turn == 1:
    print("")
    print("Player 1's turn!")
    while turn == 1:
      print("")
      choose_action = input("Player 1, what do you want to do? ")
      if choose_action == "Spin":
        spin_amount = random.choice(spin_amount_list)
        if spin_amount == "Express":
          spin_amount = 1000
          print("You landed on Express!")
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              print("Please call a consonant!")
            else:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 2
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player1_total = player1_total + int((spin_amount * len(letter_index_list)))
                  print("You now have $", player1_total)
                  print("")
                  print(board)
                  print("")
                  express_input = input("Would you like to hop on? ")
                  if express_input == "Yes":
                    while "-" in board:
                      print("")
                      letter = input("Enter a letter or solve: ")
                      if letter == "Solve":
                        solve_puzzle = input("What is the puzzle? ")
                        if solve_puzzle == puzzle:
                          if player1_total < 1000:
                            player1_total = 1000
                          print("")
                          print("Player 1 wins with $" + str(player1_total) + "!")
                          solved = True
                          break
                        else:
                          print("")
                          print("This is incorrect!")
                          turn = 2
                          break
                      elif letter in puzzle:
                        if letter in letters_called_list:
                          print("Sorry, this letter has already been called!")
                          turn = 2
                          player1_total = 0
                          break
                        else:
                          if letter in vowel_list:
                            if player1_total >= 250:
                              letter_index_list = []
                              for pos, char in enumerate(puzzle):
                                if char == letter:
                                  letter_index_list.append(pos)
                              
                              for i in range(len(letter_index_list)):
                                x = letter_index_list[i]
                                board = board[:x] + letter + board[x+1:]
                              letters_called_list.append(letter)
                              player1_total = player1_total - 250
                              print("You now have $", player1_total)
                            else:
                              print("You do not have enough money to buy a vowel!")
                            print("")
                            print(board)
                          else:
                            spin_amount = 1000
                            letter_index_list = []
                            for pos, char in enumerate(puzzle):
                              if char == letter:
                                letter_index_list.append(pos)
                            
                            for i in range(len(letter_index_list)):
                              x = letter_index_list[i]
                              board = board[:x] + letter + board[x+1:]
                            letters_called_list.append(letter)
                            player1_total = player1_total + 1000 * len(letter_index_list)
                            print("You now have $", player1_total)
                            print("")
                            print(board)
                      else:
                        print("Sorry this letter is not in the puzzle!")
                        turn = 2
                        player1_total = 0
                        break
                else:
                  print("Sorry, this letter is not in the puzzle! ")
                  turn = 2
                  break
        
            break
        if spin_amount == "Bankrupt":
          print("You landed on a bankrupt! You lose all your money!")
          player1_total = 0
          turn = 2
          break
        elif spin_amount == "Lose a Turn":
          print("You landed on a Lose a Turn!")
          turn = 2
          break
        else:
          print("You landed on $", spin_amount)
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              print("Please call a consonant!")
            else:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 2
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player1_total = player1_total + int((spin_amount * len(letter_index_list)))
                  print("You now have $", player1_total)
                else:
                  print("Sorry, this letter is not in the puzzle! ")
                  turn = 2
                  break
        
            print("")
            print(board)
      
      elif choose_action == "Vowel":
        if player1_total >= 250:
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 2
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player1_total = player1_total - 250
                  print("You now have $", player1_total)
                else:
                  print("Sorry, this letter is not in the puzzle!")
                  turn = 2
                  break
            else:
              print("Please enter a vowel!")
        else:
          print("You do not have enough money to buy a vowel!")
        
        print("")
        print(board)
        
      elif choose_action == "Solve":
        solve_puzzle = input("What is the puzzle? ")
        if solve_puzzle == puzzle:
          if player1_total < 1000:
            player1_total = 1000
          print("")
          print("Player 1 wins with $" + str(player1_total) + "!")
          solved = True
          break
        else:
          print("")
          print("This is incorrect!")
          turn = 2
          break
#-------------------------------------------------------------------------------
  if turn == 2:
    print("")
    print("Player 2's turn!")
    while turn == 2:
      print("")
      choose_action = input("Player 2, what do you want to do? ")
      if choose_action == "Spin":
        spin_amount = random.choice(spin_amount_list)
        if spin_amount == "Express":
          spin_amount = 1000
          print("You landed on Express!")
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              print("Please call a consonant!")
            else:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 3
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player2_total = player2_total + int((spin_amount * len(letter_index_list)))
                  print("You now have $", player2_total)
                  print("")
                  print(board)
                  print("")
                  express_input = input("Would you like to hop on? ")
                  if express_input == "Yes":
                    while "-" in board:
                      print("")
                      letter = input("Enter a letter or solve: ")
                      if letter == "Solve":
                        solve_puzzle = input("What is the puzzle? ")
                        if solve_puzzle == puzzle:
                          if player2_total < 1000:
                            player2_total = 1000
                          print("")
                          print("Player 2 wins with $" + str(player2_total) + "!")
                          solved = True
                          break
                        else:
                          print("")
                          print("This is incorrect!")
                          turn = 3
                          break
                      elif letter in puzzle:
                        if letter in letters_called_list:
                          print("Sorry, this letter has already been called!")
                          turn = 3
                          player2_total = 0
                          break
                        else:
                          if letter in vowel_list:
                            if player2_total >= 250:
                              letter_index_list = []
                              for pos, char in enumerate(puzzle):
                                if char == letter:
                                  letter_index_list.append(pos)
                              
                              for i in range(len(letter_index_list)):
                                x = letter_index_list[i]
                                board = board[:x] + letter + board[x+1:]
                              letters_called_list.append(letter)
                              player2_total = player2_total - 250
                              print("You now have $", player2_total)
                            else:
                              print("You do not have enough money to buy a vowel!")
                            print("")
                            print(board)
                          else:
                            spin_amount = 1000
                            letter_index_list = []
                            for pos, char in enumerate(puzzle):
                              if char == letter:
                                letter_index_list.append(pos)
                            
                            for i in range(len(letter_index_list)):
                              x = letter_index_list[i]
                              board = board[:x] + letter + board[x+1:]
                            letters_called_list.append(letter)
                            player2_total = player2_total + 1000 * len(letter_index_list)
                            print("You now have $", player2_total)
                            print("")
                            print(board)
                      else:
                        print("Sorry this letter is not in the puzzle!")
                        turn = 3
                        player2_total = 0
                        break
                else:
                  print("Sorry, this letter is not in the puzzle! ")
                  turn = 3
                  break
        
            break
        if spin_amount == "Bankrupt":
          print("You landed on a bankrupt! You lose all your money!")
          player2_total = 0
          turn = 3
          break
        elif spin_amount == "Lose a Turn":
          print("You landed on a Lose a Turn!")
          turn = 3
          break
        else:
          print("You landed on $", spin_amount)
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              print("Please call a consonant!")
            else:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 3
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player2_total = player2_total + int((spin_amount * len(letter_index_list)))
                  print("You now have $", player2_total)
                else:
                  print("Sorry, this letter is not in the puzzle! ")
                  turn = 3
                  break
        
            print("")
            print(board)
      
      elif choose_action == "Vowel":
        if player2_total >= 250:
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 3
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player2_total = player2_total - 250
                  print("You now have $", player2_total)
                else:
                  print("Sorry, this letter is not in the puzzle!")
                  turn = 3
                  break
            else:
              print("Please enter a vowel!")
        else:
          print("You do not have enough money to buy a vowel!")
        
        print("")
        print(board)
        
      elif choose_action == "Solve":
        solve_puzzle = input("What is the puzzle? ")
        if solve_puzzle == puzzle:
          if player2_total < 1000:
            player2_total = 1000
          print("")
          print("Player 2 wins with $" + str(player2_total) + "!")
          solved = True
          break
        else:
          print("")
          print("This is incorrect!")
          turn = 3
          break
#-------------------------------------------------------------------------------
  if turn == 3:
    print("")
    print("Player 3's turn!")
    while turn == 3:
      print("")
      choose_action = input("Player 3, what do you want to do? ")
      if choose_action == "Spin":
        spin_amount = random.choice(spin_amount_list)
        if spin_amount == "Express":
          spin_amount = 1000
          print("You landed on Express!")
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              print("Please call a consonant!")
            else:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 1
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player3_total = player3_total + int((spin_amount * len(letter_index_list)))
                  print("You now have $", player3_total)
                  print("")
                  print(board)
                  print("")
                  express_input = input("Would you like to hop on? ")
                  if express_input == "Yes":
                    while "-" in board:
                      print("")
                      letter = input("Enter a letter or solve: ")
                      if letter == "Solve":
                        solve_puzzle = input("What is the puzzle? ")
                        if solve_puzzle == puzzle:
                          if player3_total < 1000:
                            player3_total = 1000
                          print("")
                          print("Player 3 wins with $" + str(player3_total) + "!")
                          solved = True
                          break
                        else:
                          print("")
                          print("This is incorrect!")
                          turn = 1
                          break
                      elif letter in puzzle:
                        if letter in letters_called_list:
                          print("Sorry, this letter has already been called!")
                          turn = 1
                          player3_total = 0
                          break
                        else:
                          if letter in vowel_list:
                            if player3_total >= 250:
                              letter_index_list = []
                              for pos, char in enumerate(puzzle):
                                if char == letter:
                                  letter_index_list.append(pos)
                              
                              for i in range(len(letter_index_list)):
                                x = letter_index_list[i]
                                board = board[:x] + letter + board[x+1:]
                              letters_called_list.append(letter)
                              player3_total = player3_total - 250
                              print("You now have $", player3_total)
                            else:
                              print("You do not have enough money to buy a vowel!")
                            print("")
                            print(board)
                          else:
                            spin_amount = 1000
                            letter_index_list = []
                            for pos, char in enumerate(puzzle):
                              if char == letter:
                                letter_index_list.append(pos)
                            
                            for i in range(len(letter_index_list)):
                              x = letter_index_list[i]
                              board = board[:x] + letter + board[x+1:]
                            letters_called_list.append(letter)
                            player3_total = player3_total + 1000 * len(letter_index_list)
                            print("You now have $", player3_total)
                            print("")
                            print(board)
                      else:
                        print("Sorry this letter is not in the puzzle!")
                        turn = 1
                        player3_total = 0
                        break
                else:
                  print("Sorry, this letter is not in the puzzle! ")
                  turn = 1
                  break
        
            break
        if spin_amount == "Bankrupt":
          print("You landed on a bankrupt! You lose all your money!")
          player3_total = 0
          turn = 1
          break
        elif spin_amount == "Lose a Turn":
          print("You landed on a Lose a Turn!")
          turn = 1
          break
        else:
          print("You landed on $", spin_amount)
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              print("Please call a consonant!")
            else:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 1
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player3_total = player3_total + int((spin_amount * len(letter_index_list)))
                  print("You now have $", player3_total)
                else:
                  print("Sorry, this letter is not in the puzzle! ")
                  turn = 1
                  break
        
            print("")
            print(board)
      
      elif choose_action == "Vowel":
        if player3_total >= 250:
          if "-" in board:
            print("")
            letter = input("Enter a letter: ")
            if letter in vowel_list:
              if letter in letters_called_list:
                print("Sorry, this letter has already been called!")
                turn = 1
                break
              else:
                if letter in puzzle:
                  letter_index_list = []
                  for pos, char in enumerate(puzzle):
                    if char == letter:
                      letter_index_list.append(pos)
                  
                  for i in range(len(letter_index_list)):
                    x = letter_index_list[i]
                    board = board[:x] + letter + board[x+1:]
                  letters_called_list.append(letter)
                  player3_total = player3_total - 250
                  print("You now have $", player3_total)
                else:
                  print("Sorry, this letter is not in the puzzle!")
                  turn = 1
                  break
            else:
              print("Please enter a vowel!")
        else:
          print("You do not have enough money to buy a vowel!")
        
        print("")
        print(board)
        
      elif choose_action == "Solve":
        solve_puzzle = input("What is the puzzle? ")
        if solve_puzzle == puzzle:
          if player3_total < 1000:
            player3_total = 1000
          print("")
          print("Player 3 wins with $" + str(player3_total) + "!")
          solved = True
          break
        else:
          print("")
          print("This is incorrect!")
          turn = 1
          break
