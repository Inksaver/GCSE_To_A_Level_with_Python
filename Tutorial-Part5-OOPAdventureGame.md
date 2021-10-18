<h1>Tutorial Part5 Text Adventure Game </h1>

This part  moves on to introduce simple classes and objects, in addition to using code modules as described in [Part3.](Tutorial-Part3.md)

The concept here is to design a simple text adventure game, where there is 1 player (code module)
that can collect items (class with object instances) and travel around different locations (class with object instances).

The [first implementation](/Python/OOP/00-Adventure%20Game-layout) is a design of the overall layout. The file [main.py](/Python/OOP/00-Adventure%20Game-layout/main.py) demonstrates this perfectly:

```python
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
```
This code needs the kboard library, which has been copied to this directory in lib/kboard.py for convenience.

As you can see, nothing much happens here, although it does run without error.

The shared module imported at the beginning is a simple code module holding only this code:
```python
items:dict = {}
locations:dict = {}
current_location:str = ""
```

Using a shared module allows you to keep a dictionary of all the game objects in a central repository. You can get and set variables with a simple `var = shared.var` and `shared.var = var` syntax as long as you import shared into other files. As with the kboard module, you can also use methods defined in the shared module, although there are none there presently.

The player is another code module imported at the beginning:

```python
''' This is a Python Module equivalent to a C# static class '''

# properties: Can be directly accessed for read/write
name:str = ""
health:int = 100
strength:int  = 100
character:str = ""
character_types:list = []
inventory:list = []

# public methods
def update_stats(character_index:int) -> None:
	''' modify health and strength depending on character selected '''
	pass
	
def add_to_inventory(item:str) -> None:
	''' add an item to player inventory '''
	pass

def remove_from_inventory(item:str) -> None:
	''' remove an item from player inventory '''
	pass
		
def display_inventory() -> None:
	''' display contents of player inventory '''
	pass

def display_player() -> None:
	''' main use for debug. prints all player properties '''
	pass
```

The skeleton of an adventure game is now there, ready to be built into a full game.
