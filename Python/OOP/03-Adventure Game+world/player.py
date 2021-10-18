''' This is a Python Module equivalent to a static class '''

# properties: Can be directly accessed for read/write

name:str = ""
health:int = 100
strength:int = 100
character:str = ""
character_types:list = []
inventory:list = []

def update_stats(character_index:int) -> None:
	''' modify health and strength depending on character selected '''
	global health, strength # major failing in Python. Declared in body of script = global?
	health += character_index * 2
	strength -= character_index * 2
	
def add_to_inventory(item:str) -> None:
	''' add an item to player inventory '''
	global inventory
	if item not in inventory:
		inventory.append(item)
		
def remove_from_inventory(item:str) -> None:
	''' remove an item to player inventory '''
	global inventory
	if item in inventory:
		inventory.remove(item)
		
def display_inventory() -> None:
	''' display player;s inventory '''
	# global not needed as the value of inventory is not being changed
	if len(inventory) == 0:
		print("Your inventory is empty")
	else:
		print("In your inventory you have:")
		output:str = ""
		for item in inventory:
			output += f"{item}, "
		output = output.strip()[:-1]
		print(output)
		
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
