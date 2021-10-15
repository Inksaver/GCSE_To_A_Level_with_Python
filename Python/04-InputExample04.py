def get_string(prompt, with_title = False, min = 1, max = 20): # with_title, min and max can be over-ridden by calling code
	''' Public method: Gets a string from the user, with options for Title Case, length of the string. Set min to 0 to allow empty string return '''
	valid_input = False
	while not valid_input:  # altenative: while valid_input is False:
		user_input = input(f"{prompt}_").strip()
		if len(user_input) == 0 and min > 0:
			print("\nJust pressing the Enter key or spacebar doesn't work...")
		else:		
			if len(user_input) >= min and len(user_input) <= max:
				if with_title:
					user_input = user_input.title()
				valid_input = True
			else:
				print(f"\nTry entering text between {min} and {max} characters...")

	return user_input

def display_data(first_name, surname):
	''' all screen output from this procedure '''
	print(f"Hello {first_name} {surname}")

def get_user_data():
	''' function to return 2 strings guaranteed to have validated values '''
	first_name = get_string("Please type your first name (min 1 chars, max 10)", True, 1, 10)
	surname = get_string("Please type your surname (min 2 chars, max 20)", True, 2, 20)
	return first_name, surname

def main():
	'''everything starts from here. Call specific functions to  run your program'''
	first_name, surname = get_user_data() # populate variables from function
	display_data(first_name, surname)
	
main()
input("Press Enter to quit")