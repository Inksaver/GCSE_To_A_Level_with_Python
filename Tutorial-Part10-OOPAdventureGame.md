<h1>Tutorial Part10 Text Adventure Game </h1>

In the last part, the game is working and can be played through.

The code for this game stage can be found here: [04-Adventure Game+gameloop](/Python/OOP/04-Adventure%20Game%2Bgameloop)

This part adds a new class: Weapon

The weapon class is derived from the Item class. This means weapons are items, but have an extra property: damage - the amount of damage the item can do to an enemy or perhaps another item.

The code for the weapon class is:
```python
''' as this sub-class of item is a separate file, item has to be imported '''
import item
class Weapon(item.Item): #inherits item.Item class
	def __init__(self, name, description = "", damage = 0):
		item.Item.__init__(self, name, description)	# invoking the __init__ of the parent class	
		self._damage = damage
		
	@property
	def damage(self):
		return self._damage
	@damage.setter
	def damage(self, value):
		self._damage = value	

```
Most tutorials you see on sub-classing work on the principle that the sub-class is written in the same file as the main class. This one is not. It is a separate file, and so in Python, it has to import the item class file before it can be used.

It also means the "inherits from" class in the constructor is in the format `item.Item`
