<h1>Tutorial Part7 Text Adventure Game </h1>

In part 6 the player code module was used to define the player, and an introduction to the game initiated. In this part, the functions `add_to_items()` and `setup_items()` are implemented.

The code can be found here: [02-Adventure Game+player+items](/Python/OOP/02-Adventure%20Game%2Bplayer%2Bitems)

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
    def name(self) -> str:		# the @property decorator allows two def name(): functions 
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
So why the different ways of doing it? Why cant I use `print(torch.description)`?

In the Item class, two different ways of dealing with the class 'properties' (variables) has been used.<br>
The older method works ok, but is less intuitive:
```python
def get_description(self) -> str:
	return self._description
```
This uses a good old-fashioned function to 'get' the value, so you have to use `item.get_description()`<br>
Same with 'set' the value: `item.set_description(value)`

This is still the case in Java.<br>

The more modern approach is to use 'decorators' which allow you to have two functions with the same name, one of which 'gets' the value, the other 'sets' a new value:
```python
    @property
    def name(self) -> str:
	return self._name
    
    @name.setter
    def name(self, value:str) -> None:
	self._name = value
```

the 'getter' decorator is `@property`<br>
The 'setter' decorator is `@variable_name.setter`<br>
Use of decorators is becoming more popular. Decorators also match C#'s `public string Name {get; set;}` format.

Note the use of the variable `self`. This is added with the constructor, and allows the class to refer to itself when functions are called. This is what allows you to make multiple objects in memory at the same time. If you call a function in an object, it has its own copy of all the functions and variables given to it at construction, and uses `self` to refer to them.

The function in main(): `setup_items()` has now been implemented:

```python
   def setup_items() -> None:
	''' create items '''
	# example 1 use a temp object variable then add the object to the dictionary
	obj = item.Item("torch", "a flaming wooden torch")	# create an Item object - name: "torch", description "a flaming wooden torch"
	shared.items.update({"torch":obj})			# add it to the shared dictionary with the key 'torch'

	# example 2 add an iron key directly to the dictionary without temp variable. dictionary keys can contain spaces
	shared.items.update({"iron key":item.Item("iron key", "a 5 lever iron key")})

	#example 3 use a function to add a book
	add_to_items("book", "a copy of 'Python in easy steps' by Mike McGrath")
```

Note 3 different methods of creating an item and adding it to the shared.items dictionary.

The final method is to use a helper function:
```python
def add_to_items(key_name:str, description:str) -> None:
	''' add a new item to the shared.items dictionary '''
	shared.items.update({key_name: item.Item(key_name, description)})
```

Now you can use classes to create multiple item objects, such as torhes, keys, rocks, spells etc. and store them all in one dictionary.<br>
Add more properties to them if required such as value, cost, hitPoints, healing, etc.

Next part introduces a locations class which also has methods to carry out tasks related to each location, such as displaying a description, a list of items found within it, and the exits from it.
