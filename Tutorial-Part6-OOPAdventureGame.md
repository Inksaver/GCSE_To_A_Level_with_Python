<h1>Tutorial Part6 Text Adventure Game </h1>

In part 5 the skeleton of a game was presented. In this part, the functions `display_intro()` and `setup_player()` are implemented.

There are some changes to `main()`:
```python
def main() -> None:
	''' Everything runs from here '''
	player.character_types:list = ["Fighter", "Wizard", "Ninja", "Theif"] 	# set the possible character types in player first
	display_intro("| Welcome to an Epic Adventure Game |")			# set the scene for your adventure game
	setup_player(1.5)							# set the value for the delay between text output
	setup_items()								# create your world
	setup_world()								# setup the world
	play()									# play the game
```
1. The list of possible character types is assigned to the player module.
2. A string is passed to `display_intro()`
3. A 1.5 second delay is passed to `setup_player()`

Starting with `display_intro()`:

```python
def display_intro(intro_text:str) -> None:
	''' Displays an introduction to the adventure using the supplied intro_text '''
	os.system('cls') #os.system("clear") on mac/linux/replit
	separator = "".ljust(len(intro_text),"+")
	print(separator)
	print(intro_text)
	print(separator)
	time.sleep(2)
	os.system('cls')
```

This can be made as elaborate as you want. In this case the text required to describe your game is passed in from main() using `display_intro('some text')`

Note `os.system('cls')` is Windows specific, and `os.system('clear')` works on Mac and Linux.
It will only work when running in a console, not in the typical IDE output pane.

The line `separator = "".ljust(len(intro_text),"+")` creates a string of + characters of the same length as the supplied text.

Note the use of a 2 second delay to clear the screen again after the intro is displayed.

Next: `setup_player()`:
```python
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
 ```
 
 The line `if debug:` refers to a global boolean variable set to True at the start of the script.
 This allows you to see the result of the changes you have made to the player code module.
 The display of the player properties is called from a function inside the player module: `player.display_player()`:
 
```python
 def display_player() -> None:
	''' main use for debug. prints all player properties '''
	print(''.ljust(60,'-'))
	print("Player properties:")
	print(''.ljust(60,'-'))
	print(f"Characters available: {character_types}")
	print(''.ljust(60,'-'))
	print(f"Name:                 {name}")
	print(f"Health:               {health}")
	print(f"Strength:             {strength}")
	print(f"Character:            {character}")
	print(f"Inventory:            {inventory}")
	print(''.ljust(60,'-'))
```

There is no need to use the `global` keyword in this function, as the variables referred to are read-only here, and display without problems
