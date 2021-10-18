<h1>Tutorial Part9 Text Adventure Game </h1>

In the last part, all game elements are in place, the player is defined, a few items have been created, and 4 locations: hotel room, coridoor, lift and magic portal.

The code for this game stage can be found here: [04-Adventure Game+gameloop](/Python/OOP/04-Adventure%20Game%2Bgameloop)

This part adds the all-important game loop to get things running.

The game loop is the function `play()` which has 2 new helper functions `take_action()` and `check_exit()`

```python
def play() -> None:
	''' game loop '''
	action:str = ""
	while action != "quit":
		os.system('cls') #os.system("clear") on mac/linux/replit
		here:location.Location = shared.locations[shared.current_location]
		exits:list = here.display_location()
		action, param = take_action(here, exits)
		#action:str, param:str = take_action(here, exits)
		if action == "go":
			#check if next location has item_required
			shared.current_location = check_exit(here, param)		
		elif action == "examine":
			print(f"You examine the {param}:")
			print(f"{shared.items[param].get_description()}")
			time.sleep(2)
		elif action == "take":
			print(f"You take the {param} and put it in your backpack")
			player.add_to_inventory(param)
			here.remove_item(param)
			time.sleep(2)
		elif action == "inventory":
			player.display_inventory()
			time.sleep(2)
```
This loop continues until the player selects 'quit' from the menu.<br>
This version does not use free text entry to control the actions, a fixed menu system only requires choosing a numbered option.<br>
Every time the loop runs, the following takes place:
1. Clear screen
2. set the local variable `here` to the current location. This contains the location object as hinted in the line: `here:location.Location = shared.locations[shared.current_location]`
3. Get a list of exits from the 'here' object
4. pass here and the exits list to the `take_action()` helper function:

```python
def	take_action(here:object, exits:list) -> [str,str]:
	''' choose player action '''
	options:list = []
	# examine / take any items
	if here.get_items_count() > 0:
		for item in here.items:
			options.append(f"Examine {item}")
			options.append(f"Take {item}")
	# open inventory
	options.append("Open your inventory")
	# take an exit
	if len(exits) > 0:
		for exit in exits:
			options.append(f"Go {exit}")

	# quit the game	
	options.append("Quit")
	choice:str = options[kb.menu("What next?", options)]

	if choice == "Quit":
		return "quit", ""
	elif "Go " in choice:
		# get direction 
		direction = f"to_{choice[3:]}" # to_north, to_east, etc
		return "go", direction
	elif "Examine" in choice:
		# get item
		item = choice[8:]
		return "examine", item
	elif "Take" in choice:
		item = choice[5:]
		return "take", item
	else:
		# open inventory
		return "inventory", ""
```
