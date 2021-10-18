import os, time
import lib.kboard as kb #note use of lib. to locte file inside a subdirectory called lib
import player, shared

debug: bool = True # set to false when development paused or completed

def add_to_items(key_name:str, description:str) -> None:
	''' add a new item to the shared.items dictionary '''

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
	
def setup_world() -> None:
	''' create locations '''
		
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