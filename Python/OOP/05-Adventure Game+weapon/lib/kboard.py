'''
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
def process_input(prompt:str, min_value:int, max_value:int, data_type:str) -> str:
	''' This function is not called directly from other files. Python does not have a 'Private' keyword'''
	valid_input:bool = False
	while valid_input is False:
		print(prompt, end="_")
		user_input:str = input()    # Could use: user_input = input(f"{prompt}_"), but these 2 lines can be used with other languages
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
						
					if user_input >= min_value and user_input <= max_value:
						valid_input = True
					else:
						print(f"\nTry a number from {min_value} to {max_value}...")
				except:
					print(f"\nTry entering a number - {user_input} does not cut it...")
			
	return user_input
			
def get_string(prompt:str, with_title:bool = False, min_value:int = 1, max_value:int = 20) -> str: # with_title, min_value and max_value can be over-ridden by calling code
	''' Public method: Gets a string from the user, with options for Title Case, length of the string. Set min_value to 0 to allow empty string return '''
	valid:bool = False
	while not valid:
		user_input:str = input(prompt + "_").strip()	# change '_' for any preferred character eg '>'
		if len(user_input) == 0 and min_value > 0:
			print("\nJust pressing the Enter key or spacebar doesn't work...")
		else:		
			if len(user_input) >= min_value and len(user_input) <= max_value:
				if with_title:
					user_input = user_input.title()
				valid = True
			else:
				print(f"\nTry entering text between {min_value} and {max_value} characters...")

	return user_input
	
def get_integer(prompt:str, min_value:int = 0, max_value:int = 65536) -> int: # min_value and max_value can be over-ridden by calling code
	''' Public Method: gets an integer from the user '''
	return process_input(prompt, min_value, max_value, "int")

def get_float(prompt:str, min_value:float = 0.0, max_value:float = 1000000.0) -> float: # min_value and max_value can be over-ridden by calling code
	''' Public Method: gets a float from the user '''
	return process_input(prompt, min_value, max_value, "float")
	
def get_boolean(prompt:str) -> bool:
	''' Public Method: gets a boolean (yes/no) type entries from the user '''
	return process_input(prompt, 1, 3, "bool")

def menu(title:str, menu_list:list) -> int:
	''' displays a menu using the text in 'title', and a list of menu items (string) '''
	print(title)
	for i in range(1, len(menu_list) + 1):    # this range numbers the menu items starting at 1
		print(f"\t{i}) {menu_list[i - 1]}")   # -1 as the iterator starts at 1 instead of 0
		
	return get_integer(f"Type the number of your choice (1 to {len(menu_list)})", 1, len(menu_list)) - 1 # -1 to return correct list index