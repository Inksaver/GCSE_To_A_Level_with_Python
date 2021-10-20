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

The code here has been re-factored from the student's original attempt

1. it imports the kboard module to get guaranteed return from the user
2. importing os and time allow clearing the console between sections
3. it begins in main()
4. there are no global variables
5. Interpolated strings have been used
6. All while loops use a flag instead of while True: break
'''
import os, time
import lib.kboard as kb

def clear() -> None:
	''' clear the console '''
	is_console:bool = False
	try:
		window_width:int = os.get_terminal_size().columns # this will fail if NOT in a console
		is_console = True
	except:
		pass
	if is_console:
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
	else:
		for i in range(25):
			print()


def intro() -> None:
	''' intro '''
	clear()
	print("Welcome to this workshop")
	print("You will shortly be able to create an account")
	time.sleep(3)

def create_account() -> dict:
	''' data input '''
	clear()
	firstname:str = kb.get_string("Type your first name (min 2 chars)", True, 2, 30)
	clear()
	surname:str = kb.get_string("Type your surname (min 2 chars)", True, 2, 30)
	clear()
	username:str = kb.get_string("Type a username (min 8 chars)", False, 8, 30)
	password:str = ""
	passwordcheck:str = " "
	while password != passwordcheck:
		clear()
		password = kb.get_string("Type a password (min 8 chars)", False, 8, 30)
		passwordcheck = kb.get_string("Re-type your password", False, 8, 30)
		if password != passwordcheck:
			print("passwords do not match. Try again")
	
	account:dict = {"firstname":firstname, "surname":surname, "username":username, "password":password}

	return account

def add_account(accounts:dict, account:dict) -> dict:
	''' create account	'''	
	if account["username"] not in accounts:
		accounts.update({account["username"]:account}) # store username/password as dictionary pair
	return accounts

def welcome(account:dict) -> None:
	''' welcome message '''
	clear()
	print(f"Thank you {account['firstname']} for signing up to this workshop")
	print("You can now sign in to your account")
	time.sleep(3)
	

def sign_in(accounts) -> None:
	''' request sign in '''
	clear()
	valid:bool = False
	account:dict = None
	while not valid:
		username:str = kb.get_string("Enter your username", False, 2, 30)
		if username not in accounts.keys():
			print("Username not recognised. Try again")
		else:
			valid = True
			account = accounts[username]
	
	valid = False		
	while not valid:
		password:str = kb.get_string("Enter your password", False, 2, 30)
		if password != account["password"]:
			print("Incorrect password Try again")
		else:
			valid = True
			
def main() -> None:		
	accounts:dict = {}
	intro()
	account:dict = create_account()
	accounts = add_account(accounts, account)
	welcome(account)
	sign_in(accounts)
	clear()
	print("We are ready to go!") # start application
	
main()
input("Enter to quit") # only required if running in console/terminal