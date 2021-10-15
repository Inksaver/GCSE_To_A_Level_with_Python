def get_string(prompt, with_title = False, min = 1, max = 20): # with_title, min and max can be over-ridden by calling code
	''' Public method: Gets a string from the user '''
	pass

def display_data(first_name, surname):
	''' all screen output from this procedure '''
	pass

def get_user_data():
	''' function to return 2 strings guaranteed to have validated values '''
	return "first_name", "surname"
def main():
	'''everything starts from here. Call specific functions to  run your program'''
	first_name, surname = get_user_data() # populate variables from function
	display_data(first_name, surname)
	
main()
input("Press Enter to quit")