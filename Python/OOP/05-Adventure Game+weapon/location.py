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
		
	# properties
	@property
	def name(self) -> str:
		return self._name

	@property
	def description(self) -> str:
		return self._description

	@property
	def to_north(self) -> str:
		return self._to_north

	@property
	def to_east(self) -> str:
		return self._to_east

	@property
	def to_south(self) -> str:
		return self._to_south

	@property
	def to_west(self) -> str:
		return self._to_west
	
	@property
	def items(self) ->list:
		''' return a list of all items in this location '''
		return self._items
	
	@items.setter
	def items(self, list_of_items:list) -> None:
		''' allows items in this location to be set in bulk '''
		# list_of_items is a list of dictionary keys sent as
		# ["torch", "key"]
		self._items = list_of_items	
	
	@property
	def item_required(self) -> str:
		''' return item required to enter this location '''
		return self._item_required 
	
	@item_required.setter		
	def item_required(self, value:str) -> None:
		''' set the item required to enter this location '''
		self._item_required = value	
	
	# methods
	def add_item(self, item_key:str) -> None:
		''' add an item to the list of items in this location '''
		if item_key not in self._items:
			self._items.append(item_key)
	
	def get_items_count(self) -> int:
		''' return no. of items in this location '''
		return len(self._items) 
			
	def location_dict(self) -> dict:
		''' return a dictionary of surrounding locations '''
		return {'n':self._to_north, 'e':self._to_east, 's':self._to_south, 'w':self._to_west} # Dictionary of strings	
		           
	def location_list(self) -> list:
		''' return a list of surrounding locations '''
		return [self._to_north, self._to_east, self._to_south, self._to_west] # List of strings
	
	def remove_item(self, item_key:str) -> None:
		''' removes an item from list of items in this location '''
		if item_key in self._items:
			self._items.remove(item_key)
		
	def set_locations(self, to_north:str, to_east:str, to_south:str, to_west:str) -> None:
		''' allows surrounding locations to be changed '''
		#self-corrects for spaces e.g " " = "", "room " = "room"
		self._to_north = to_north.strip()
		self._to_east = to_east.strip()
		self._to_south = to_south.strip()
		self._to_west = to_west.strip()
	
	def display_location(self) -> list:
		''' descrbe the current location, any items inside it, and exits '''
		exits:list = []
		if self._to_north != "":
			exits.append("north")
		if self._to_east != "":
			exits.append("east")
		if self._to_south!= "":
			exits.append("south")
		if self._to_west != "":
			exits.append("west")				
	
		print(f"You are in {self._description}")
		if len(exits) > 0:
			output:str = "There are exits: "
			for exit in exits:
				output += exit + ", "
			output = output.strip()[:-1] # remove comma
		else:
			output = "There are no exits"
		print(output)
	
		if len(self._items) > 0:
			output = "In this location there is: "
			for item in self._items:
				output += item + ", "
			output = output.strip()[:-1] # remove comma
			print(output)
	
		return exits	