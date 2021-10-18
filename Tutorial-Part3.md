<h1>Tutorial Part3</h1>

In Part2 the idea of writing a function that could be re-used by copy/pasting to another file emerged.
This was the `get_string()` function.
Why not take this a step further and create a library of similar input related functions, say to get guaranteed return of integer,
float and boolean values, and maybe even a numbered menu system.<br>
An example of such a library can be found [here.](/Python/lib/kboard.py) It is 91 lines long, so will not be shown in full here but one of the methods, which is an adaptation of the function first seen in [03-inputExample02.py](/Python/03-InputExample02.py) now appears as:

```python
def get_string(prompt:str, with_title:bool = False, min_value:int = 1, max_value:int = 20) -> str: # with_title, min_value and max_value can be over-ridden by calling code
	''' Public method: Gets a string from the user, with options for Title Case, length of the string. Set min_value to 0 to allow empty string return '''
	valid:bool = False
	while not valid:
		user_input:str = input(prompt + "_").strip()	# change '_' for any preferred character eg '>'
		if len(user_input) == 0 and min_value > 0:
			print("\nJust pressing the Enter key or spacebar doesn't work...")
		else:		
			if len(user_input) >= min_value and len(user_input) <= max_value:
				if with_title:
					user_input = user_input.title()
				valid = True
			else:
				print(f"\nTry entering text between {min_value} and {max_value} characters...")

	return user_input
```
Notice the relatively new (Python 3.5) Type hinting is used. As a C# programmer, the hinting is extremely useful, as it gives an indication of the variable type when declared or passed as parameters, and the return type of a function.

A return type of `-> None` means it is a procedure, equivalent to C#'s void return type.

There is a [demo](/Python/05-kboard_demo.py) for use in this tutorial:

```python
# import kboard as kb   # if kboard.py is in same directory
import lib.kboard as kb # if kboard.py is in a separate /lib/kboard.py sub-directory
# as kb shortens the module name to kb

def display_data(data):
	''' displays the contents of the dictionary 'data' '''
	#separator = "------------------------------------------------"
	separator = "".rjust(40, "-") # far less typing needed here!
	print(separator)
	print(f"  Name :         {data['name']}")
	print(f"  Age :          {data['age']}")
	print(f"  Height :       {data['height']}")
	print(f"  Likes Python : {data['pythoner']}")
	print(separator)
	print(f"{data['name']} thinks this utility is: {data['opinion']}")
	print(separator)
	
def get_data(data):
	''' dictionary with existing data is modified and returned '''
	# get_string(prompt, with_title = False, min = 1, max = 20)             # parameter list of kboard.get_string()
	data["name"] = kb.get_string("Type your name", True, 3, 10) 	        # returns user input in Title Case
	data["age"] = kb.get_integer("How old are you", 5, 120) 		# gets an integer between 5 and 120 from the user
	data["height"]= kb.get_float("How tall are you in metres?", 0.5, 2.5)   # gets a float between 0.5 and 2.5 from the user
	data["pythoner"] = kb.get_boolean("Do you like Python? (y/n)") 	        # returns True or False from the user
	
	menu_title = "What do think of this utility?"
	menu_list = ["Brilliant", "Not bad", "Could do better", "Rubbish"]
	user_choice = kb.menu(menu_title, menu_list)	
	data["opinion"] = menu_list[user_choice]
	
	return data	

def main():
	''' uses the dictionary datatype to store random data '''
	# data is local to function main()
	data = {"name":"",
		"age":0,
		"height":0.0,
		"pythoner":False,
		"opinion":""}
	
	data = get_data(data)
	display_data(data)
	
main()
# if running from a console instead of an IDE
kb.get_string("Press Enter to Quit", False, 0, 20) # Used instead of input("Press Enter to Quit")
```
To follow this tutorial, download the [demo file](/Python/05-kboard_demo.py) seen above.

Download the [kboard.py file](/Python/lib/kboard.py) and place it inside a sub-directory of your project called 'lib'.

When you run it, there is a dictionary created in main(), which remains local to the main() function.
This dictionary is passed between functions as required, a behaviour rarely seen in student projects.
(They normally declare their variables globally at the top of the script.)

`main()` has only the dictionary declaration and two functions are called: `get_Data()` and `display_data()`

This has already split a very simple script into three parts, which makes it much easier to manage.
Note the import at the top of the script: `import lib.kboard as kb`. This format does 2 things:
1. Allows the import of a file in a subdirectory (Lua uses `require lib.kboard`)
2. Renames the imported library as kb so it can be used with less typing: `kb.get_string()`

As a C# programmer I do not like the import to remove parts of the class. I will always use `import random` and then `random.randint()`.
`from random import *` does not go down well. I like to see where functions are coming from.

`get_data(data)` uses the external kboard.py library to get guaranteed input from the user. All the errors that could be generated by incorrect input is dealt with before the values are returned.<br>
Four variable types are returned,: string, integer, float and boolean. These are the actual datatypes, not string represetations of them. That is all handled in the library.

Finally a useful menu utility is called which gives the user numbered options, and guarantees one of them will be returned. The return value is an integer representing the index of the list used to supply the options, `user_choice = kb.menu(menu_title, menu_list)` which can then be used to obtain the contents of that list item if required: `data["opinion"] = menu_list[user_choice]`

There is an [exercise that you can use](/Python/06-Exercise.py) to convert a typical student script without functions into a fully procedural script by re-factoring the code.<br>
Why not give it a go?
```python
'''
Write a program to create an account for a web or application login.

1. Introduce the application's name/purpose etc.
2. Get first name, surname, username and password from the user
3. Ensure firstname and surname are a minimum of 2 characters each and in Title Case
4. Ensure username and password are at least 8 characters.
5. Check the entered password by asking for it to be re-typed.
6. Create the account in a data structure of your choice to become one of a collection of accounts
   (this data is not currently stored on disc, so will be lost on exit)
7. Confirm account creation and ask user to sign in with their new credentials
8. Check username exists
9. Check password if username exists.
10. Start the application

The code here represents a typical student effort, which works ok, but is a little rough.
There are no comments or docstrings, no functions or procedures.
The account when created only holds the username and password.

Re-factor this code as follows:

1. Download, import and use the kboard.py code module from https://pastebin.com/UceAJsaV or [here](/Python/lib/kboard.py)
2. import os to allow os.system('cls') windows or os.system('clear') mac/unix
3. import time to work with os.system('cls') for smooth transitions
4. Break it into a series of functions/procedures, starting with def main()
5. Do not use global variables.
6. Use a dictionary of dictioaries for the accounts that can contain all input data
7. Use interpolated strings wherever possible, eg welcome message
8. Do NOT use while True: break loops
9. Add docstrings to functions
10. Comment any code that may not have a clear intent


'''
print("Welcome to this workshop")
print("please create an account")
print()

firstname = ""
while len(firstname) < 3:
	firstname = input("Type your first name (min 2 chars)_")
firstname = firstname.title()	
surname = ""
while len(surname) < 3:
	surname = input("Type your surname (min 2 chars)_")
surname = surname.title()
username =""
while len(username) < 8:
	username =  input("Type a username (min 8 chars)_")
password = ""
passwordcheck = " "
while password != passwordcheck:
	while len(password) < 8:
		password =  input("Type a password (min 8 chars)_")	
	passwordcheck = input("Re-type your password_")
	if password != passwordcheck:
		print("passwords do not match. Try again")
	
accounts = {}
accounts.update({username:{username:password}}) 

print("Thank you",firstname,"for signing up to this workshop")
print("You can now sign in to your account")

while True:
	username = input("Enter your username_")
	if username not in accounts.keys():
		print("Username not recognised. Try again")
	else:
		break
	
while True:
	password = input("Enter your password_")
	if password != accounts[username][username]:
		print("Incorrect password Try again")
	else:
		break
		
print("We are ready to go!")
input("Enter to quit") # only required if running in console/terminal
```
