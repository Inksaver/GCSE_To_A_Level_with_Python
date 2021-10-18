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

1. Download, import and use the kboard.py code module from https://github.com/Inksaver/GCSE_To_A_Level_with_Python/blob/main/Python/lib/kboard.py
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
