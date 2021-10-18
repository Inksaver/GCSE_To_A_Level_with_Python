<h1>Tutorial Part7 Text Adventure Game </h1>

In part 6 the player code module was used to define the player, and an introduction to the game initiated. In this part, the functions `add_to_items()` and `setup_items()` are implemented.

There are no changes to `main()`

There is another file added [item.py:](/Python/OOP/02-Adventure%20Game%2Bplayer%2Bitems/item.py), which has to be added to the imports.
```python
class Item:
    #constructor
    def __init__(self, name:str, description:str = ""):
	self._name:str  = name
	self._description:str = description
    
    def get_description(self) -> str:
	return self._description
	
    def set_description(self, value:str) -> None:
	self._description = value
  
    @property
	def name(self) -> str:			# the @property decorator allows two def name(): functions 
	    return self._name
    
    @name.setter
	def name(self, value:str) -> None:	# same signature but the @name.setter allows this
	self._name = value
```

