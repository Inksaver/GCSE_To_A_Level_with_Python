Assuming you have looked at Tutorial-Part1, similar ideas can be implemented for your Python scripts.
Always start with a main() function.

In C, C++ C# and Java you have no choice, so get into the swing of it straight away. You could use any of these languages in future
```python
def main():
	''' start here. use main() as a launch pad for other functions '''
	print("Hello World")

main() # 'Call' function 'main()'
input("Press Enter to quit") # prevents closing if running from console/terminal
```
When starting a new script from now on, start with an empty `def main()` with the line `main()` at the bottom of the script, before you do anything else.

An example of writing a procedural script for the following task:

"Get the first name and surname from the user and greet them using both names".
Easy!
```python
first_name = input("Type your first name")
surname = input("Type your surname")
print("Hello", first_name, surname)
input("Enter to quit")
```
It works, but there are some minor problems:
1. No validation - The user can just press the Enter key
2. The input prompt does not have any separation from the text the user is entering
3. The appearance of the input/output is a bit basic
4. If there was a lot more data to be collected, more code needs to be added, and a single script can get very long.

This is how to do it in a procedural way:
1. We want to get 2 strings from the user, so maybe a function get_user_data()
2. Those strings should be validated for at least 2 characters per name, so 'Jo Lo' does not miss out. maybe get_string().
3. Finally output the name to the console, maybe display_data()

A quick code layout could be:
```python
def get_string(prompt, with_title = False, min = 1, max = 20): # with_title, min and max can be over-ridden by calling code
	''' Public method: Gets a string from the user '''
	pass

def display_data(first_name, surname):
	''' all screen output from this procedure '''
	pass

def get_user_data():
	''' function to return 2 strings guaranteed to have validated values '''
	return "first_name", "surname"
	
def main():
	'''everything starts from here. Call specific functions to  run your program'''
	first_name, surname = get_user_data() # populate variables from function
	display_data(first_name, surname)
	
main()
input("Press Enter to quit")
```
Note the use of 'docstrings' under each definition. They indicate what the function is used for.
The function get_string() takes one obligatory parameter: the 'prompt', and 3 optional parameters for title case, minimum and maximum length
Dummy data has been returned in the get_user_data() function to prevent errors
This will run OK, but it only gets the data, then finishes, but you can see how the relatively simple task of getting two
names and printing them out has been broken down into a total of four functions/procedures.
This is overkill in such a small application, but if it reached several hundred lines, it is far easier to maintain than a single non-branching script.
Also it prepares the way for using multiple files, which can make re-using code so much easier.

Starting with the get_string() function, its full code is:
```python
def get_string(prompt, with_title = False, min = 1, max = 20): # with_title, min and max can be over-ridden by calling code
	''' Public method: Gets a string from the user, with options for Title Case, length of the string. Set min to 0 to allow empty string return '''
	valid_input = False
	while not valid_input:  # altenative: while valid_input is False:
		user_input = input(f"{prompt}_").strip()
		if len(user_input) == 0 and min > 0:
			print("\nJust pressing the Enter key or spacebar doesn't work...")
		else:		
			if len(user_input) >= min and len(user_input) <= max:
				if with_title:
					user_input = user_input.title()
				valid_input = True
			else:
				print(f"\nTry entering text between {min} and {max} characters...")

	return user_input
```
This function has many useful features:
1. The loop uses a variable flag NOT the typical `While True: break` construct
2. Output strings use interpolation `f"{}"` to combine expressions and variables into the final string.
3. Leading and trailing spaces are removed prior to validation `.strip()`
4. Unless min has been set to 0, pressing Enter only does not validate
5. If the input string is outside the min/max bounds the input is not validated
6. Only validated input is returned. If you ask for 4 to 8 characters in Title Case, that's what you get.



