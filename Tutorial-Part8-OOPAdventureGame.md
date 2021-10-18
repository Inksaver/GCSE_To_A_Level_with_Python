<h1>Tutorial Part8 Text Adventure Game </h1>

In the last part, an Items class was introduced. This part has a new file called location.py,
This is the location class, from which game locations can be made, with exits, contained items, puzzles, enemies etc.

The code for this game stage can be found here: [03-Adventure Game+world](/Python/OOP/03-Adventure%20Game%2Bworld)

The locations class definition and constructor:
```python
class Location:
	#constructor
	def __init__(self,
	             name:str,
	             description:str,
	             to_north:str = "",
	             to_east:str = "",
	             to_south:str = "",
	             to_west:str = "",
	             items:list = [],
	             item_required:str = ""):
		
		self._name:str = name
		self._description:str = description
		self._to_north:str = to_north
		self._to_east:str = to_east
		self._to_south:str = to_south
		self._to_west:str = to_west
		self._items:list = items
		self._item_required:str = item_required
```
The file has a fair number of properties, including the names of any other locations to the n /e /s /w of the current one<br>
Also a list of any items contained in the current location.<br>
Finally, if a specific item is required to enter.

There are methods to display the location, description, exits and items inventory
There are methods to add and remove items from the inventory.

The function `setup_world()` in `main.py` has now been implemented:
```python
def setup_world() -> None:
	''' create locations '''
	# all locations are stored in the dictionary shared.locations
	# method 1 use a temp object variable
	obj:location.Location = location.Location("hotel room", "a damp hotel room",
							"", "coridoor", "", "",
							["torch","book"],"key card")
	shared.locations.update({"hotel room":obj})

	# method 2 directly to shared.locations
	shared.locations.update({"coridoor":location.Location("coridoor", "a dark coridoor with a worn carpet",
								"magic portal", "lift", "", "hotel room",
								["key card"], "")})
	# method 3 use a function
	# add_to_locations(name, description, tonorth, toeast, tosouth, towest, item_required, items)
	add_to_locations("lift", "a dangerous lift with doors that do not close properly", "", "", "", "coridoor", [], "")
	add_to_locations("magic portal", "the end of the adventure. Well done", "", "", "", "", [], "") # no exits: end game
	shared.current_location = "hotel room"

	if debug:
		print("\nThe Dictionary shared.locations contains the following data:\n")
		print("key/name     description           toNorth      toEast      toSouth       toWest       required     items")
		print("".ljust(110,"-"))
		for key,value in shared.locations.items():
			description = value.description
			if len(description) > 17:
				description = description[:18] + "... "
			else:
				description = description.ljust(22," ")
			print(f"{key.ljust(13)}{description}", end="")
			print(f"{value.to_north.ljust(13)}{value.to_east.ljust(13)}{value.to_south.ljust(13)}{value.to_west.ljust(13)}", end = "")
			print(f"{value.item_required.ljust(13)}{value.items}")
		print("".ljust(110,"-") + '\n')
		input("Enter to continue")
```
As with the items class, 3 methods of adding a location are described, including a helper function:

```python
def add_to_locations(key_name:str, description:str, tonorth:str = '', toeast:str = '', tosouth:str = '', towest:str = '', items:list = [], item_required:str = "") -> None:
	''' add a new location to the shared.locations ditionary '''
	shared.locations.update({key_name: location.Location(key_name, description)})
	shared.locations[key_name].set_locations(tonorth, toeast, tosouth, towest)
	shared.locations[key_name].items = items
	shared.locations[key_name].item_required = item_required
```
The helper function creates the new location object using only the name and description initially, then adds it to the dictionary.<br>
Exits, Items and item_required are added later, partly to show how to use one of the methods, and 2 properties directly.

The game is now constructed, the player and all the elements are there.<br>
The next stage is to move around the world and interact with the items within it.
