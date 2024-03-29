import lib.kboard as kb #note use of lib. to locate file inside a subdirectory called lib
import player, shared

def add_to_items(key_name:str, description:str) -> None:
	''' add a new item dictionary to the shared.items dictionary '''

def add_to_locations(key_name:str, description:str, tonorth:str = '', toeast:str = '', tosouth:str = '', towest:str = '', item_required:str = '', items:list = []) -> None:
	''' create a new location dictionary to shared.locations '''

def display_intro() -> None:
	''' Displays an introduction to the adventure '''
	
def setup_player() -> None:
	''' gets player details. Change the text to suit your adventure theme '''
	
def setup_items() -> None:
	''' create items '''
	
def setup_world() -> None:
	''' create locations '''

def play() -> None:
	''' game loop '''
	
def display_location(here) -> list:
	''' descrbe the current location, any items inside it, and exits '''
	exits:list = []
		
	return exits
		
def	take_action(here, exits:list) -> None:
	''' choose player action '''
	
def main() -> None:
	''' Everything runs from here '''
	setup_player()			# setup player name and character
	setup_items()			# create items found in your game
	setup_world()			# create locations in your game
	display_intro()			# set the scene for your adventure game
	play()				# play the game
	
main()
input("Enter to quit")
