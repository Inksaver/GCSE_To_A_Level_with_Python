'''
    This file is kboard.py: https://pastebin.com/UceAJsaV version 1.1
	Demo available from https://pastebin.com/CkfybTVb
	
    kboard static class returns string, integer, float, boolean and menu choices
	Use:
	import kboard as kb #shortens the class name to kb
	
	user_name = kb.get_string("Type your name", True) # returns user input in Title Case
	
	user_age = kb.get_integer("How old are you", 5, 120) # gets an integer between 5 and 120 from the user
	
	user_height = kb.get_float("How tall are you in metres?", 0.5, 2.5) # gets a float between 0.5 and 2.5 from the user
	
	user_likes_python = kb.get_boolean("Do you like Python? (y/n)") # returns True or False from the user
	
	menu_list = ["Brilliant", "Not bad", "Could do better", "Rubbish"]
	user_choice = kb.menu("What do think of this utility?", menu_list)
	print(f"User thinks this utility is: {menu_list[user_choice]}")
	
	kb.get_string("Press Enter to Quit", False, 0, 20) # Used instead of input("Press Enter to Quit")
	at the end of a file to prevent the console closing (does not apply when run from IDE)

'''
def process_input(prompt, min, max, data_type):
	''' This function is not called directly from other files. Python does not have a 'Private' keyword'''
	valid_input = False
	while valid_input is False:
		print(prompt, end="_")
		user_input = input()    # Could use: user_input = input(f"{prompt}_"), but these 2 lines can be used with other languages
		if len(user_input) == 0:
			print("\nJust pressing the Enter key doesn't work...")
		else:
			if data_type == "bool":		
				if user_input[0].lower() == "y":
					user_input = True
					valid_input = True
				elif user_input[0].lower() == "n":
					user_input = False
					valid_input = True
				else:
					print("\nOnly anything starting with y or n is accepted...")
			else:
				try:
					if data_type == "int":
						user_input = int(user_input)
					elif data_type == "float":
						user_input = float(user_input)				
						
					if user_input >= min and user_input <= max:
						valid_input = True
					else:
						print(f"\nTry a number from {min} to {max}...")
				except:
					print(f"\nTry entering a number - {user_input} does not cut it...")
			
	return user_input
			
def get_string(prompt, with_title = False, min = 1, max = 20): # with_title, min and max can be over-ridden by calling code
	''' Public method: Gets a string from the user, with options for Title Case, length of the string. Set min to 0 to allow empty string return '''
	valid = False
	while not valid:
		user_input = input(prompt + "_").strip()	# change '_' for any preferred character eg '>'
		if len(user_input) == 0 and min > 0:
			print("\nJust pressing the Enter key or spacebar doesn't work...")
		else:		
			if len(user_input) >= min and len(user_input) <= max:
				if with_title:
					user_input = to_title(user_input)	# Python has string.title() function. C#, Lua and Java do not, so not used here
				valid = True
			else:
				print(f"\nTry entering text between {min} and {max} characters...")

	return user_input
	
def get_integer(prompt, min = 0, max = 65536): # min and max can be over-ridden by calling code
	''' Public Method: gets an integer from the user '''
	return process_input(prompt, min, max, "int")

def get_float(prompt, min = 0.0, max = 1000000.0): # min and max can be over-ridden by calling code
	''' Public Method: gets a float from the user '''
	return process_input(prompt, min, max, "float")
	
def get_boolean(prompt):
	''' Public Method: gets a boolean (yes/no) type entries from the user '''
	return process_input(prompt, 1, 3, "bool")

def to_title(input_text):
	''' Private Method: makes text into Title Case '''
	temp_list = list(input_text.lower())
	for index in range(len(temp_list)):
		if index == 0:
			temp_list[0] = temp_list[0].upper()
		elif temp_list[index - 1] == " ":
			temp_list[index] = temp_list[index].upper()

	return ''.join(temp_list)

def menu(title, menu_list):
	''' displays a menu using the text in 'title', and a list of menu items (string) '''
	print(title)
	for i in range(1, len(menu_list) + 1):    # this range numbers the menu items starting at 1
		print(f"\t{i}) {menu_list[i - 1]}")   # -1 as the iterator starts at 1 instead of 0
		
	return get_integer(f"Type the number of your choice (1 to {len(menu_list)})", 1, len(menu_list)) - 1 # -1 to return correct list index
