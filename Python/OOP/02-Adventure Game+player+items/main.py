import os, time
import lib.kboard as kb #note use of lib. to locte file inside a subdirectory called lib
import player, shared, item

debug: bool = True # set to false when development paused or completed

def add_to_items(key_name:str, description:str) -> None:
	''' add a new item to the shared.items dictionary '''
	shared.items.update({key_name: item.Item(key_name, description)})

def add_to_locations(key_name:str, description:str, tonorth:str = '', toeast:str = '', tosouth:str = '', towest:str = '', items:list = [], item_required:str = "") -> None:
	''' add a new location to the shared.locations ditionary '''

def display_intro(intro_text:str) -> None:
	''' Displays an introduction to the adventure using the supplied intro_text '''
	os.system('cls') #os.system("clear") on mac/linux/replit
	separator = "".ljust(len(intro_text),"+")
	print(separator)
	print(intro_text)
	print(separator)
	time.sleep(2)
	os.system('cls')
	
def setup_player(delay:float) -> None:
	''' gets player details. Change the text to suit your adventure theme '''
	print("I am the overlord, and I will help you to find my lost treasure")
	time.sleep(delay)

	print("I just need to get to know you before I let you in...")
	time.sleep(delay)
	
	player.name = kb.get_string("What is your name?", True, 2, 20)
	print(f"Hello {player.name}. You are the adventurer destined to find my lost treasure")
	time.sleep(delay)

	title:str = "Let me know your character, so you can be awarded your skills"
	choice:int = kb.menu(title, player.character_types)
	player.character = player.character_types[choice]
	player.update_stats(choice)
	if debug:
		player.display_player()
		input("Enter to continue")
	print(f"I see you are a {player.character} with {player.health} health and {player.strength} strength")	
	
	time.sleep(delay)
	print("Welcome. Serve me well and you will be rewarded")
	time.sleep(delay * 2)
	os.system('cls')
	
def setup_items() -> None:
	''' create items '''
	# example 1 use a temp object variable then add the object to the dictionary
	obj = item.Item("torch", "a flaming wooden torch")	# create an Item object - name: "torch", description "a flaming wooden torch"
	shared.items.update({"torch":obj})			# add it to the shared dictionary with the key 'torch'

	# example 2 add an iron key directly to the dictionary without temp variable. dictionary keys can contain spaces
	shared.items.update({"iron key":item.Item("iron key", "a 5 lever iron key")})

	#example 3 use a function to add a book
	add_to_items("book", "a copy of 'Python in easy steps' by Mike McGrath")
	
	if debug:
		print("The Dictionary shared.items contains the following objects:")
		print("key       name      description")
		print("".ljust(80,"-"))
		for key,value in shared.items.items():
			print(f"{key.ljust(10)}{value.name.ljust(10)}{value.get_description()}")
		print("".ljust(80,"-"))
		input("Enter to continue")
	
def setup_world() -> None:
	''' create locations '''
	# all locations are stored in the dictionary shared.locations
		
def play() -> None:
	''' game loop '''		
	
def main() -> None:
	''' Everything runs from here '''
	player.character_types:list = ["Fighter", "Wizard", "Ninja", "Theif"] 	# set the possible character types in player first
	display_intro("| Welcome to an Epic Adventure Game |")				# set the scene for your adventure game
	setup_player(1.5)													# set the value for the delay between text output
	setup_items()														# create your world
	setup_world()														# setup the world
	play()																# play the game

main()
input("Enter to quit")