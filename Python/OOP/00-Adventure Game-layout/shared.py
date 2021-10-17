'''
the items, enemies and locations are shared by multiple files, so are best kept in a code module
dictionaries of all these objects offer the greatest flexibility

Example of items dictionary, which is a dictionary of item objects
items["torch"] = <item object>

items["torch"].name -> "torch"
items["torch"].get_description() = "a flaming wooden torch"
items["key card"].name" = "key card",
items["key card"].get_description() = "Property of Holiday Inn"

example of locations dictionary which is a dictionary of location objects
locations["hotel room"].name = "hotel room"
locations["hotel room"].description = "a damp hotel room"
locations["hotel room"].to_north = ""
locations["hotel room"].to_east = "coridoor"
locations["hotel room"].to_south = ""
locations["hotel room"].to_west = ""
locations["hotel room"].item_required = "key card"              # key of an item from the items dictionary
locations["hotel room"].items = ["torch","plastic sword"]       # a Python list of the dictionary keys of items in the location
}
'''
items:dict = {}
locations:dict = {}
current_location:str = ""
