'''
the items and locations are shared by multiple files, so are best kept in this code module
using dictionaries offers the greatest flexibility

example of items dictionary, which is a dictionary of dictionaries:
items["torch"] = 
{
	"name": "torch",
	"description": "a flaming wooden torch"
}
items["key card"] = 
{
	"name": "key card",
	"description": "Property of Holiday Inn"
}
example of locations dictionary which is a dictionary of dictionaries:
locations["hotel room"] =
{
    "name":"hotel room",
	"description": "a damp hotel room",
	"to_north":"",
	"to_east":"coridoor",
	"to_south":"",
	"to_west":"",
	"item_required":"key card"              # key of an item from the items dictionary
	"items":["torch","plastic sword"]       # a Python list of the dictionary keys of items in the location
}
'''
items = {}
locations = {}
current_location = ""
