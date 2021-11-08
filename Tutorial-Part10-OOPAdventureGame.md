<h1>Tutorial Part10 Text Adventure Game </h1>

In the last part, the game is working and can be played through.

The code for this game stage can be found here: [05-Adventure Game+weapon](/Python/OOP/05-Adventure%20Game%2Bweapon)

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
Most tutorials you see on sub-classing work on the principle that the sub-class is written in the same file as the main class. This one is not. It is a separate file, which has a number of consequenses:
1. It has to import the item class file before it can be used.
2. It also means the "inherits from class" in the constructor is in the format `item.Item` as seen in `class Weapon(item.Item):`
3. The keyword 'super' as used in `super.__init__()` cannot be used.
