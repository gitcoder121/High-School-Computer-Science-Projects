"""
Multiplayer Quiz Game
Created by Milaan Shah
Date: May 1, 2023
"""

#-------------------------------------------------------- Initialization
# imports tkinter; it allows for the creation of buttons and labels
import tkinter as tk

# introduces the game
print("Welcome to Multiplayer Quiz Game!")
print("")
# asks the users if they want to learn how to play the game
help = input("Would you like to learn how to play? ")
help = help.lower()
# if the users answer "yes", the instructions are shown
if help == "yes":
  print("This is a 3 player game in which the players answer questions to earn $$. The player with the most $$ wins! The questions are organized into categories and are worth different $$ amount. The higher the number of $$ a question is worth, the harder the question. To begin, press a button. This will display a question and a chance for the players to buzz in to answer the question. Player 1 presses the number 1, Player 2 presses the number 2, and Player 3 presses the number 3 on the keyboard to buzz in. The first player to buzz in gets a chance to answer the question. If the answer is correct, the player will be awarded the corresponding $$ amount. If the answer is incorrect, the player will lose the corresponding $$ amount. Good luck!")
  print("Note: If all players would like to skip the question, press the enter button on the keyboard during the buzzer (make sure that no player has buzzed in). Do not enter unnecessary spaces or letters, or capitalize any letter while answering the question.")
print("")
print("")

# main window
root = tk.Tk()
root.wm_geometry("1000x400")
root.wm_title("Multiplayer Quiz Game")

# frame that shows when button clicked
frame_answer = tk.Frame(root)
frame_answer.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="news")

# frame to display scoreboard
frame_scoreboard = tk.Frame(root)
frame_scoreboard.grid(row=0, columnspan=4, sticky="news")

# frame for category 1
frame_one = tk.Frame(root)
frame_one.grid(row=1, column=0, sticky="news")

# frame for category 2
frame_two = tk.Frame(root)
frame_two.grid(row=1, column=1, sticky="news")

# frame for category 3
frame_three = tk.Frame(root)
frame_three.grid(row=1, column=2, sticky="news")

# frame for category 4
frame_four = tk.Frame(root)
frame_four.grid(row=1, column=3, sticky="news")

#-------------------------------------------------------- Variables
# player scores
player_one_total = 0
player_two_total = 0
player_three_total = 0

# keeps track of number of buttons pressed
questions_answered = 0

# style
background_color = "#1707f7"
font_color = "#fcf405"

# assigns background color to frames and main window
root.config(bg=background_color)
frame_one.config(bg=background_color)
frame_two.config(bg=background_color)
frame_three.config(bg=background_color)
frame_four.config(bg=background_color)
frame_scoreboard.config(bg=background_color)
frame_answer.config(bg=background_color)

#-------------------------------------------------------- Lists
# category titles
category_names = ["HISTORY", "SPORTS", "SCIENCE", "COLLEGES"]

# Note: "c" is short form for category and "b" is short form for button (b1 is the top most button and b4 is the bottom most button)
# titles of buttons corresponding to the amount of $$ each button is worth
c1_button_names = ["$200 ", "$400 ", "$600 ", "$1000"]
# category 1 storage of questions and answers
c1_questions = ["Which land roads streched across Asia and allowed for the transfer of luxury goods in the Third-Wave Era?", "Which country was the first to allow women the right to vote?", "In the Indian Ocean, the Portuguese created which type of empire that aimed to control commerce, not large territories?", "Which U.S. President championed the concept of national self-determination?"]
# answers vary depending on user input; therefore, the program checks for multiple variations of the answer
c1_b1_answers = ["Silk Roads", "Silk Road", "Silk"]
c1_b2_answers = ["New Zealand"]
c1_b3_answers = ["Trading Post Empire", "Trade Post Empire", "Trading Post", "Trade Post"]
c1_b4_answers = ["Woodrow Wilson"]

# titles of buttons corresponding to the amount of $$ each button is worth
c2_button_names = ["$200 ", "$400 ", "$600 ", "$1000"]
# category 2 storage of questions and answers
c2_questions = ["Which country won the 2022 FIFA World Cup?", "Who was the winning quarterback of the 2023 Superbowl?" , "Who holds the record for the most 3-pointers in NBA?", "Which individual has won the most number of medals in the Olympics?"]
# answers vary depending on user input; therefore, the program checks for multiple variations of the answer
c2_b1_answers = ["Argentina"]
c2_b2_answers = ["Patrick Mahomes", "Mahomes"]
c2_b3_answers = ["Stephen Curry", "Steph Curry", "Curry"]
c2_b4_answers = ["Michael Phelps", "Phelps"]

# titles of buttons corresponding to the amount of $$ each button is worth
c3_button_names = ["$200 ", "$400 ", "$600 ", "$1000"]
# category 3 storage of questions and answers
c3_questions = ["What are the outermost electrons in an atom called?", "In plant cells, what is the green pigment that is involved in photosynthesis called?", "What is the 3-D structure of DNA called?", "What is the process of breaking apart molecules by passing an electric current through a solution called?"]
# answers vary depending on user input; therefore, the program checks for multiple variations of the answer
c3_b1_answers = ["Valence Electrons", "Valence Electron", "Valence"]
c3_b2_answers = ["Chlorophyll"]
c3_b3_answers = ["Double Helix", "Twisted Ladder"]
c3_b4_answers = ["Electrolysis"]

# titles of buttons corresponding to the amount of $$ each button is worth
c4_button_names = ["$200 ", "$400 ", "$600 ", "$1000"]
# category 4 storage of questions and answers
c4_questions = ["The mascot of Princeton University is what animal?", "Which college was Nevada's first medical school?", "Which is the oldest ivy league college?", "What college did quarterback Tom Brady attend?"]
# answers vary depending on user input; therefore, the program checks for multiple variations of the answer
c4_b1_answers = ["Tiger", "The Tiger"]
c4_b2_answers = ["University of Nevada", "UNR", "University of Nevada, Reno", "University of Nevada Reno"]
c4_b3_answers = ["Harvard", "Harvard University"]
c4_b4_answers = ["University of Michigan", "U-M", "UMich"]


#-------------------------------------------------------- Functions
# tells the user that a button is already clicked
def clicked_button():
  print("Already Clicked!")

"""  
function that determines which player, if any, "pressed the buzzer" to answer first
player 1 presses "1" on the keyboard to buzz
player 2 presses "2" on the keyboard to buzz
player 3 presses "3" on the keyboard to buzz
"""
def buzzer():
  # receives input and removes whitespace
  buzzer = str(input("Buzzer: "))
  buzzer.strip()

  # if no player buzzed in, function returns 0, meaning that no player answers
  if len(buzzer) == 0:
    return 0
  # looks at the first person to buzz, 
  chosen_player = buzzer[0]
  # if player 1 buzzed in first, function returns 1, meaning that player 1 gets the chance to answer; simiar concept for players 2 and 3
  if chosen_player == "1":
    return 1
  elif chosen_player == "2":
    return 2
  elif chosen_player == "3":
    return 3
  # if the first buzzer input letter is not from players 1, 2, or 3, function returns 0, meaning that no player answers
  else:
    return 0

# function below is called when all the buttons are clicked
def win():
  # recieves variables for the player score totals
  global player_one_total, player_two_total, player_three_total, questions_answered
  # empty print statements for formatting and distinguishing the results
  print("")
  print("")
  # determines the winner and displays which player won
  if (player_one_total > player_two_total) and (player_one_total > player_three_total):
    print("Player 1 wins!")
  elif (player_two_total > player_one_total) and (player_two_total > player_three_total):
    print("Player 2 wins!")
  elif (player_three_total > player_one_total) and (player_three_total > player_two_total):
    print("Player 3 wins!")
  # if there is a tie, it displays that it is a tie
  else:
    print("There is a tie!")

# function that recieves input from player who buzzed in first and checks whether answer is correct; if answer is correct, it awards $$ and displays that it is correct; if answer is wrong, it subtracts $$ and displays the correct answer
# parameters receive the question, answer, and question amount assigned to each button
def answer_function(question, answers, question_amount):
  # recieves variables for the player score totals and variable for the number of buttons clicked
  global player_one_total, player_two_total, player_three_total, questions_answered
  
  # prints questions and calls the buzzer function
  print(question)
  choose_player = buzzer()

  # set the correct_answer variable to false; this means that the program will not award points if they player's answer is not correct (player's answer is checked later; this is just to initate the variable)
  correct_answer = False

  # if player 1 buzzed in first
  if choose_player == 1:
    # recieves player 1 answer
    player_answer = str(input("Player 1 Answer: "))
    # formats answer to make format similar to correct answer (Ex: removes extra space at the end)
    player_answer = player_answer.strip()
    player_answer = player_answer.lower()
    # below checks whether answer is correct through all possible variations of the answer in the "answers" list
    # if player answer is correct, displays "correct" and adds $$ to player 1's total
    for answer in answers:
      answer = answer.lower()
      if player_answer == answer:
        correct_answer = True
    if correct_answer == True:
      print("Correct!")
      player_one_total += question_amount
    # if answer is wrong, displays "wrong", displays the correct answer, and subtracts $$ from player 1's total
    else:
      print("Wrong!")
      print("Correct answer is", answers[0])
      player_one_total -= question_amount
  
  # similar process as player 1
  elif choose_player == 2:
    player_answer = str(input("Player 2 Answer: "))
    player_answer = player_answer.strip()
    player_answer = player_answer.lower()
    for answer in answers:
      answer = answer.lower()
      if player_answer == answer:
        correct_answer = True
    if correct_answer == True:
      print("Correct!")
      player_two_total += question_amount
    else:
      print("Wrong!")
      print("Correct answer is", answers[0])
      player_two_total -= question_amount

  # similar process as player 1
  elif choose_player == 3:
    player_answer = str(input("Player 3 Answer: "))
    player_answer = player_answer.strip()
    player_answer = player_answer.lower()
    for answer in answers:
      answer = answer.lower()
      if player_answer == answer:
        correct_answer = True
    if correct_answer == True:
      print("Correct!")
      player_three_total += question_amount
    else:
      print("Wrong!")
      print("Correct answer is", answers[0])
      player_three_total -= question_amount
  
  # if no one buzzed in, program displays correct answer 
  else:
    print("Correct answer is", answers[0])

  # updates the player scores on the scoreboard
  player_total_display.config(text=("Player 1: $" + str(player_one_total) + "    Player 2: $" + str(player_two_total) + "    Player 3: $" + str(player_three_total)))

  # increases the number of buttons clicked by 1
  questions_answered += 1
  # if all the buttons are clicked, "win" function is initiated
  if questions_answered == 16:
    win()

def raise_frames():
  frame_one.tkraise()
  frame_two.tkraise()
  frame_three.tkraise()
  frame_four.tkraise()
  frame_scoreboard.tkraise()
"""
--> the below are functions for all buttons
--> they are called if a button is pressed
--> each function assigns a specific button its question (assigned in the list above), the corresponding possible answers to the question (assigned in lists above), and the amount of $$ the question is worth
--> then, the "answer_function" is called; this process displays question, determines who buzzed in first (if anyone), awards/subtracts $$ when applicable, displays correct answer if applicable, updates the player scores, and checks if all buttons are pressed
--> makes the button title blank and assigns the button the "clicked_button" function to indicate that the button is clicked
--> functions are named based on the button they correspond to (Ex: c1_b1 corresponds to category 1, button 1)
"""
def c1_b1():
  question = c1_questions[0]
  answers = c1_b1_answers
  question_amount = 200
  answer_function(question, answers, question_amount)
  btn_one_category_one.config(command=clicked_button, text="     ")

def c1_b2():
  question = c1_questions[1]
  answers = c1_b2_answers
  question_amount = 400
  answer_function(question, answers, question_amount)
  btn_two_category_one.config(command=clicked_button, text="     ")

def c1_b3():
  question = c1_questions[2]
  answers = c1_b3_answers
  question_amount = 600
  answer_function(question, answers, question_amount)
  btn_three_category_one.config(command=clicked_button, text="     ")

def c1_b4():
  question = c1_questions[3]
  answers = c1_b4_answers
  question_amount = 1000
  answer_function(question, answers, question_amount)
  btn_four_category_one.config(command=clicked_button, text="     ")

def c2_b1():
  question = c2_questions[0]
  answers = c2_b1_answers
  question_amount = 200
  answer_function(question, answers, question_amount)
  btn_one_category_two.config(command=clicked_button, text="     ")

def c2_b2():
  question = c2_questions[1]
  answers = c2_b2_answers
  question_amount = 400
  answer_function(question, answers, question_amount)
  btn_two_category_two.config(command=clicked_button, text="     ")

def c2_b3():
  question = c2_questions[2]
  answers = c2_b3_answers
  question_amount = 600
  answer_function(question, answers, question_amount)
  btn_three_category_two.config(command=clicked_button, text="     ")

def c2_b4():
  question = c2_questions[3]
  answers = c2_b4_answers
  question_amount = 1000
  answer_function(question, answers, question_amount)
  btn_four_category_two.config(command=clicked_button, text="     ")

def c3_b1():
  question = c3_questions[0]
  answers = c3_b1_answers
  question_amount = 200
  answer_function(question, answers, question_amount)
  btn_one_category_three.config(command=clicked_button, text="     ")

def c3_b2():
  question = c3_questions[1]
  answers = c3_b2_answers
  question_amount = 400
  answer_function(question, answers, question_amount)
  btn_two_category_three.config(command=clicked_button, text="     ")

def c3_b3():
  question = c3_questions[2]
  answers = c3_b3_answers
  question_amount = 600
  answer_function(question, answers, question_amount)
  btn_three_category_three.config(command=clicked_button, text="     ")

def c3_b4():
  question = c3_questions[3]
  answers = c3_b4_answers
  question_amount = 1000
  answer_function(question, answers, question_amount)
  btn_four_category_three.config(command=clicked_button, text="     ")

def c4_b1():
  question = c4_questions[0]
  answers = c4_b1_answers
  question_amount = 200
  answer_function(question, answers, question_amount)
  btn_one_category_four.config(command=clicked_button, text="     ")

def c4_b2():
  question = c4_questions[1]
  answers = c4_b2_answers
  question_amount = 400
  answer_function(question, answers, question_amount)
  btn_two_category_four.config(command=clicked_button, text="     ")

def c4_b3():
  question = c4_questions[2]
  answers = c4_b3_answers
  question_amount = 600
  answer_function(question, answers, question_amount)
  btn_three_category_four.config(command=clicked_button, text="     ")

def c4_b4():
  question = c4_questions[3]
  answers = c4_b4_answers
  question_amount = 1000
  answer_function(question, answers, question_amount)
  btn_four_category_four.config(command=clicked_button, text="     ")


#-------------------------------------------------------- Labels/Button
lbl_question = tk.Label(frame_answer, text="question goes here", font="Courier 12 bold", padx=10, pady=10, bg=background_color, fg="white")
lbl_question.pack()

lbl_buzzer = tk.Label(frame_answer, text="Buzzer: ", font="Courier 10 bold", padx=10, pady=10, bg=background_color, fg="white")
lbl_buzzer.pack()

ent_buzzer = tk.Entry(frame_answer)
ent_buzzer.pack()

lbl_player = tk.Label(frame_answer, text="chosen player answer:", font="Courier 10 bold", padx=10, pady=10, bg=background_color, fg="white")
lbl_player.pack()

ent_answer = tk.Entry(frame_answer)
ent_answer.pack()

lbl_answer = tk.Label(frame_answer, text="correct answer is ...", font="Courier 12 bold", padx=10, pady=10, bg=background_color, fg="white")
lbl_answer.pack()

#label that displays the scoreboard
player_total_display = tk.Label(frame_scoreboard, text=("Player 1: $" + str(player_one_total) + "    Player 2: $" + str(player_two_total) + "    Player 3: $" + str(player_three_total)), bg=background_color, fg=font_color, font="Arial 15 bold underline", padx=10, pady=10)
player_total_display.pack()

"""
--> the below are the creation of category titles and buttons
--> they are created in their respective frames
--> they are assigned background color, font color, font type, padding, and text to display
--> the naming is consistent with the category each label or button is located in and numbers 1-4 for each button from top to bottom
--> buttons are also assigned functions that are called when the buttons are pressed; the functions are created above
"""
# Category 1
lbl_category_one = tk.Label(frame_one,
                            text=str(category_names[0]),
                            font="Courier 12 bold",
                            padx=10,
                            pady=10, bg=background_color, fg="white")
lbl_category_one.pack()

btn_one_category_one = tk.Button(frame_one,
                                 text=str(c1_button_names[0]),
                                 font="Courier 10 bold",
                                 padx=10,
                                 pady=10,
                                 command=c1_b1, bg=background_color, fg=font_color)
btn_one_category_one.pack()

btn_two_category_one = tk.Button(frame_one,
                                 text=str(c1_button_names[1]),
                                 font="Courier 10 bold",
                                 padx=10,
                                 pady=10,
                                 command=c1_b2, bg=background_color, fg=font_color)
btn_two_category_one.pack()

btn_three_category_one = tk.Button(frame_one,
                                   text=str(c1_button_names[2]),
                                   font="Courier 10 bold",
                                   padx=10,
                                   pady=10,
                                   command=c1_b3, bg=background_color, fg=font_color)
btn_three_category_one.pack()

btn_four_category_one = tk.Button(frame_one,
                                  text=str(c1_button_names[3]),
                                  font="Courier 10 bold",
                                  padx=10,
                                  pady=10,
                                  command=c1_b4, bg=background_color, fg=font_color)
btn_four_category_one.pack()

# Category 2
lbl_category_two = tk.Label(frame_two,
                            text=str(category_names[1]),
                            font="Courier 12 bold",
                            padx=10,
                            pady=10, bg=background_color, fg="white")
lbl_category_two.pack()

btn_one_category_two = tk.Button(frame_two,
                                 text=str(c2_button_names[0]),
                                 font="Courier 10 bold",
                                 padx=10,
                                 pady=10,
                                 command=c2_b1, bg=background_color, fg=font_color)
btn_one_category_two.pack()

btn_two_category_two = tk.Button(frame_two,
                                 text=str(c2_button_names[1]),
                                 font="Courier 10 bold",
                                 padx=10,
                                 pady=10,
                                 command=c2_b2, bg=background_color, fg=font_color)
btn_two_category_two.pack()

btn_three_category_two = tk.Button(frame_two,
                                   text=str(c2_button_names[2]),
                                   font="Courier 10 bold",
                                   padx=10,
                                   pady=10,
                                   command=c2_b3, bg=background_color, fg=font_color)
btn_three_category_two.pack()

btn_four_category_two = tk.Button(frame_two,
                                  text=str(c2_button_names[3]),
                                  font="Courier 10 bold",
                                  padx=10,
                                  pady=10,
                                  command=c2_b4, bg=background_color, fg=font_color)
btn_four_category_two.pack()

# Cateogry 3
lbl_category_three = tk.Label(frame_three,
                              text=str(category_names[2]),
                              font="Courier 12 bold",
                              padx=10,
                              pady=10, bg=background_color, fg="white")
lbl_category_three.pack()

btn_one_category_three = tk.Button(frame_three,
                                   text=str(c3_button_names[0]),
                                   font="Courier 10 bold",
                                   padx=10,
                                   pady=10,
                                   command=c3_b1, bg=background_color, fg=font_color)
btn_one_category_three.pack()

btn_two_category_three = tk.Button(frame_three,
                                   text=str(c3_button_names[1]),
                                   font="Courier 10 bold",
                                   padx=10,
                                   pady=10,
                                   command=c3_b2, bg=background_color, fg=font_color)
btn_two_category_three.pack()

btn_three_category_three = tk.Button(frame_three,
                                     text=str(c3_button_names[2]),
                                     font="Courier 10 bold",
                                     padx=10,
                                     pady=10,
                                     command=c3_b3, bg=background_color, fg=font_color)
btn_three_category_three.pack()

btn_four_category_three = tk.Button(frame_three,
                                    text=str(c3_button_names[3]),
                                    font="Courier 10 bold",
                                    padx=10,
                                    pady=10,
                                    command=c3_b4, bg=background_color, fg=font_color)
btn_four_category_three.pack()

# Category 4
lbl_category_four = tk.Label(frame_four,
                             text=str(category_names[3]),
                             font="Courier 12 bold",
                             padx=10,
                             pady=10, bg=background_color, fg="white")
lbl_category_four.pack()

btn_one_category_four = tk.Button(frame_four,
                                  text=str(c4_button_names[0]),
                                  font="Courier 10 bold",
                                  padx=10,
                                  pady=10,
                                  command=c4_b1, bg=background_color, fg=font_color)
btn_one_category_four.pack()

btn_two_category_four = tk.Button(frame_four,
                                  text=str(c4_button_names[1]),
                                  font="Courier 10 bold",
                                  padx=10,
                                  pady=10,
                                  command=c4_b2, bg=background_color, fg=font_color)
btn_two_category_four.pack()

btn_three_category_four = tk.Button(frame_four,
                                    text=str(c4_button_names[2]),
                                    font="Courier 10 bold",
                                    padx=10,
                                    pady=10,
                                    command=c4_b3, bg=background_color, fg=font_color)
btn_three_category_four.pack()

btn_four_category_four = tk.Button(frame_four,
                                   text=str(c4_button_names[3]),
                                   font="Courier 10 bold",
                                   padx=10,
                                   pady=10,
                                   command=c4_b4, bg=background_color, fg=font_color)
btn_four_category_four.pack()

#-------------------------------------------------------- Mainloop
# mainloop keeps the program running until the window is closed
root.mainloop()
