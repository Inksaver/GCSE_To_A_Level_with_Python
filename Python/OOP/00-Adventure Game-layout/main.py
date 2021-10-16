import lib.kboard as kb #note use of lib. to locate file inside a subdirectory called lib
import player, shared

def add_to_items(key_name, description):
	''' add a new item dictionary to the shared.items dictionary '''

def add_to_locations(key_name, description, tonorth = '', toeast = '', tosouth = '', towest = '', item_required = '', items = []):
	''' create a new location dictionary to shared.locations '''

def display_intro():
	''' Displays an introduction to the adventure '''
	
def setup_player():
	''' gets player details. Change the text to suit your adventure theme '''
	
def setup_items():
	''' create items '''
	
def setup_world():
	''' create locations '''

def play():
	''' game loop '''
	
def display_location(here):
	''' descrbe the current location, any items inside it, and exits '''
	exits = []
		
	return exits
		
def	take_action(here, exits):
	''' choose player action '''
	
def main():
	''' Everything runs from here '''
	setup_player()			# setup player name and character
	setup_items()			# create items found in your game
	setup_world()			# create locations in your game
	display_intro()			# set the scene for your adventure game
	play()					# play the game
	
main()
input("Enter to quit")