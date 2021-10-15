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
This will run OK, but it only gets the data, then finishes, but you can see how the relatively simple task of getting two
names and printing them out has been broken down into a total of four functions/procedures.
This is overkill in such a small application, but if it reached several hundred lines, it is far easier to maintain than a single non-branching script.
Also it prepares the way for using multiple files, which can make re-using code so much easier.


