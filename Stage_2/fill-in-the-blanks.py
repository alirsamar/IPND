# Stage 2 Final Project

# DATA BANK
easy_quiz = '''In this stage, you will use the (1) programming language to build your own (2). 
You will use a fill-in-the blank style to (3) a (2) that can even be used as a study tool 
to help you remember important (4).'''
easy_answer = ['Python', 'quiz', 'creat', 'vocabulary']

medium_quiz = '''For this (1), you'll be building a Fill-in-the-Blanks (2).
Your (2) will prompt a user with a paragraph containing several (3)s.
The user should then be asked to fill in each blank appropriately to complete the paragraph.
This can be used as a study tool to help you remember important (4)!'''
medium_answer = ['project', 'quiz', 'blank', 'vocabulary']

hard_quiz = '''A (1) is created with the def keyword. You specify the inputs a (1) takes by
adding (2) separated by commas between the parentheses. (1)s by default return (3) if you
don't specify the value to return. (2) can be standard data types such as string, number, dictionary,
tuple, and (4) or can be more complicated such as objects and lambda functions.'''
hard_answer = ['function', 'variables', 'nothing', 'list']

white_blanks = ['(1)', '(2)', '(3)', '(4)']

levels = ['easy', 'medium', 'hard']

# Default warnings/messages
welcome = "*" * 50 + "\n" + "  Welcome to this quiz. \n  Please, type the level." + "\n" + "*" * 50
congratulation = "*" * 50 + "\n" + "  Congratulation! You have completed this quiz! " + "\n" + "*" * 50
sorry = "*" * 50 + "\n" + "  GAME OVER! " + "\n" + "*" * 50

def check_answer(user_input_answer, answer, index_blank):
	'''Check the answer right or wrong.
	Input: [user_input_answer, answer, index_blank].
	Output: [Correct or Incorrect]'''
	if user_input_answer == answer[index_blank]:
		return 'Correct'
	else:
		return 'Incorrect'

def level_chosen(user_input_level):
	'''Determine the game level, quiz, and answer. 
	Input: [user_inpu]. 
	Output :[quiz, answer, and level]'''	
	while user_input_level not in levels:
		user_input_level = raw_input( "Wrong input! \nPossible choices are easy, medium, and hard: "" ")
	if user_input_level == 'easy':
		return easy_quiz, easy_answer, 'easy'
	if user_input_level == 'medium':
		return medium_quiz, medium_answer, 'medium'
	else:
		return hard_quiz, hard_answer , 'hard'

# Main quize logic
def fill_in_blanks():
	'''Fill in blank game, chose game level first, and then fill all the white blanks'''
	user_input_level = raw_input( "Possible choices are easy, medium, and hard: "" ")
	quiz, answer, difficulty_chosen = level_chosen(user_input_level)
	print ("\n" + "You've chosen " + difficulty_chosen + " difficulty." + "\n" + "*" * 50 + "\nYou will get 5 guesses per problem.\nThe quiz is: \n" + quiz + "\n")
	index_blank, num_guess, total_guess = 0, 1, 5
	while index_blank < len(white_blanks) and num_guess < total_guess: # Check make the game end. 
		num_guess = 0 # Guess number reset.
		user_input_answer = raw_input("What should be filled in for " + str(white_blanks[index_blank]) + "? ")
		while check_answer(user_input_answer, answer, index_blank) == 'Incorrect' and num_guess < total_guess:# Force the answer_input stop.
			print "You have " + str(total_guess - num_guess) + " try left"
			user_input_answer = raw_input("The answer is wrong, try again: " + " ")
			num_guess += 1		
		if 	check_answer(user_input_answer, answer, index_blank) == 'Correct': # Answer being checked.
			quiz = quiz.replace(white_blanks[index_blank], user_input_answer)
			print "Correct! \n" + quiz + "\n"
		index_blank += 1
	if index_blank == len(white_blanks):
		return congratulation 
	return sorry

print welcome
print fill_in_blanks() 
