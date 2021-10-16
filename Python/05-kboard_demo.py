'''  
This file needs kboard.py: https://pastebin.com/UceAJsaV  OR
https://github.com/Inksaver/GCSE_To_A_Level_with_Python/blob/main/Python/kboard.py
'''

import kboard as kb # shortens the module (static class) name to kb

def display_data(data):
	''' displays the contents of the dictionary 'data' '''
	#separator = "------------------------------------------------"
	separator = "".rjust(40, "-") # far less typing needed here!
	print(separator)
	print(f"  Name :         {data['name']}")
	print(f"  Age :          {data['age']}")
	print(f"  Height :       {data['height']}")
	print(f"  Likes Python : {data['pythoner']}")
	print(separator)
	print(f"{data['name']} thinks this utility is: {data['opinion']}")
	print(separator)
	
	
def get_data(data):
	''' dictionary with existing data is modified and returned '''
	# get_string(prompt, with_title = False, min = 1, max = 20)             # parameter list of kboard.get_string()
	data["name"] = kb.get_string("Type your name", True, 3, 10) 			# returns user input in Title Case
	data["age"] = kb.get_integer("How old are you", 5, 120) 				# gets an integer between 5 and 120 from the user
	data["height"]= kb.get_float("How tall are you in metres?", 0.5, 2.5) 	# gets a float between 0.5 and 2.5 from the user
	data["pythoner"] = kb.get_boolean("Do you like Python? (y/n)") 			# returns True or False from the user
	
	menu_title = "What do think of this utility?"
	menu_list = ["Brilliant", "Not bad", "Could do better", "Rubbish"]
	user_choice = kb.menu(menu_title, menu_list)	
	data["opinion"] = menu_list[user_choice]
	
	return data	

def main():
	''' uses the dictionary datatype to store random data '''
	# data is local to function main()
	data = {"name":"",
			"age":0,
			"height":0.0,
			"pythoner":False,
			"opinion":""}
	
	data = get_data(data)
	display_data(data)
	
main()
# if running from a console instead of an IDE
kb.get_string("Press Enter to Quit", False, 0, 20) # Used instead of input("Press Enter to Quit")