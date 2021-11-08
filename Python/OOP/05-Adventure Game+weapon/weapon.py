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