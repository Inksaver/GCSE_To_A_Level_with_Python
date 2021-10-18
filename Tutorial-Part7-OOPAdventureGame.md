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
So we are finally starting OOP.<br>
This is a class, given the name Item with Capital first letter by convention. Because the file name is item.py, once imported it is used by calling `item.Item()` (assuming `import item` is used, rather than `from item import Item`.

Unlike the player static class equivalent (code module), used up to now, you cannot simply use it in the same way: `player.name = "Fred"`<br>
Instead you have to create an 'object' or 'instance' of the class with the following code:
```python
torch = item.Item("torch", "a flaming wooden torch")
```
This will create a variable called 'torch' which contains an instance of the Item class, so you can use the variable 'torch' to get it's name and description, or change it's name or description.

```python
print(torch.name)
print(torch.get_description())

torch.name = "LED Torch"
torch.set_description("Cheap LED torch from the pound shop")
```

