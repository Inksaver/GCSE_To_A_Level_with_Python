In the last part, an Items class was introduced. This part has a new file called location.py,
which is the location class, from which game locations can be made, with exits, contained items, puzzles, enemies etc.

The code for this game stage can be found here: 

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

