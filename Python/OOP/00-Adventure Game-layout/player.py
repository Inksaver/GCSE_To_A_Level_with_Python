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
