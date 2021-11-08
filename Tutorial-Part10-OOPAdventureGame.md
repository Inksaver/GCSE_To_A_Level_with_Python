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
Most tutorials you see on sub-classing work on the principle that the sub-class is written in the same file as the main class. This one is not. It is a separate file, which has a number of consequences:
1. It has to import the item class file before it can be used.
2. It also means the "inherits from class" in the constructor is in the format `item.Item` as seen in `class Weapon(item.Item):`
3. The keyword 'super' as used in `super.__init__()` cannot be used. You get the error `builtins.TypeError: descriptor '__init__' requires a 'super' object but received a 'Weapon'`

There are a few changes to main.py
1. import weapon
2. new function add_to_weapons.
3. new line in setup_items()
4. change to line in setup_world to include a weapon in the location

```python
def add_to_weapons(key_name:str, description:str, damage:int) -> None:
	''' add a new weapon to the shared.items dictionary '''
	shared.items.update({key_name: weapon.Weapon(key_name, description, damage)})
```

setup_items() new line:

```python
# add a weapon to items dictionary. Weapon is a sub-class of Item, with damage
add_to_weapons("sword", "a toy plastic sword: a dog has chewed the handle..Yuk!", 25)
```

change to setup_world():
```python
# method 2 directly to shared.locations. Include weapon in list of items
shared.locations.update({"coridoor":location.Location("coridoor", "a dark coridoor with a worn carpet",
							"magic portal", "lift", "", "hotel room",
							["key card","sword"], "")})
```

The newly created weapon object can be stored in the same dictionary as other items, even in C# or Java equivalents, which are much stricter about the datatype of objects stored in them.

You can add other properties and methods which are unique to weapons, for example an attack() method which inflicts the amount of damage the weapon contains onto an enemy or other object.


A challenge for you at this stage is to improve the output of the game. During play a menu appears with a list of exits:
```
You are in a dark coridoor with a worn carpet
There are exits: north, east, west
In this location there is: key card, sword
What next?
        1) Examine key card
        2) Take key card
        3) Examine sword
        4) Take sword
        5) Open your inventory
        6) Go north
        7) Go east
        8) Go west
        9) Quit
Type the number of your choice (1 to 9)_
```

It would be great if this menu could be a bit more helpful, So it looks like this:
```
You are in a dark coridoor with a worn carpet
There are exits: north, east, west
In this location there is: key card, sword
What next?
        1) Examine key card
        2) Take key card
        3) Examine sword
        4) Take sword
        5) Open your inventory
        6) Go north -> magic portal
        7) Go east -> lift
        8) Go west -> hotel room
        9) Quit
Type the number of your choice (1 to 9)_

```

Alter the code to make this happen.
In order to do this, you must be able to follow the code logic and make changes on the way:
Hints:

1. Where is the menu created?
2. Where does the menu get it's data from
3. If I change anything in the menu output to screen, will this have consequences further down the line?
4. Does the exit list get sliced to obtain just the direction?
5. If so can it be adapted?
