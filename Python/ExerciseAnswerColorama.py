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

1. it imports the ui module to get guaranteed return from the user and coloured output
2. it begins in main()
3. there are no global variables
4. Interpolated strings have been used
5. All while loops use a flag instead of while True: break
'''
import lib.ui as ui

def input_box(text_lines:list, box_colour:str, prompt:str, title_case:bool = False, min_length:int = 0, max_length:int = 65536) -> str:
	ui.clear()
	num_lines:int = ui.draw_multi_line_box("s", text_lines, box_colour, "black", "white", "black", "left")
	num_lines = num_lines + ui.add_lines(5, num_lines) # pad Console to leave 5 empty lines
	num_lines = num_lines + ui.draw_line("d", "white", "black") # now leaves 4 empty lines
	return ui.get_string(num_lines, prompt, ">_", "white", "black", title_case, min_length, max_length)	

def add_account(accounts:dict, account:dict) -> dict:
	''' create account	'''	
	if account["username"] not in accounts:
		accounts.update({account["username"]:account}) # store username/password as dictionary pair
	return accounts

def create_account() -> dict:
	''' data input '''
	text_lines:list = ["","Type your ~green~first name ~white~in the box below.","","You must enter at least ~red~2 ~white~characters","", "Maximum of ~red~20",""]
	firstname:str = input_box(text_lines, "green", "Type your ~green~first name~white~", True, 2, 20)

	text_lines:list = ["","Type your ~magenta~surname ~white~in the box below","","You must enter at least ~red~2 ~white~characters","and a maximum of ~red~20",""]
	surname:str = input_box(text_lines, "magenta", "Type your ~magenta~surname~white~", True, 2, 20)
	
	text_lines:list = ["","Type your ~blue~username ~white~in the box below","","You must enter at least ~red~8 ~white~characters","and a maximum of ~red~15",""]
	username:str = input_box(text_lines, "blue", "Type your ~blue~username~white~", False, 8, 15)
	
	password:str = ""
	passwordcheck:str = " "
	while password != passwordcheck:
		text_lines:list = ["","Type your ~red~password ~white~in the box below","","You must enter at least ~red~8 ~white~characters","and a maximum of ~red~15",""]
		password:str = input_box(text_lines, "red", "Type your ~red~password~white~", False, 8, 15)

		text_lines:list = ["","~magenta~Re-type ~white~your ~red~password ~white~in the box below","","The case must match the original ~red~password ~white~typed earlier","",""]
		passwordcheck:str = input_box(text_lines, "magenta", "~magenta~Re-type ~white~your password", False, 0, 15)
		if password != passwordcheck:
			ui.display_message("Passwords do not match. Try again", False, True, "cyan", "dgrey")
	
	account = {"firstname":firstname, "surname":surname, "username":username, "password":password}

	return account

def display_account(account:dict) -> None:
	''' start application '''
	text_lines:list = ["Error 404:",f"Your account {account['username']} has been compromised",
					   "","Your data has been sold on the dark web.",
					   "","Please make sure you have a bitcoin account",
					   "You will shortly be scammed by multiple parties",
					   "","Thank you for joining the workshop",
					   "","", "~blue~©user-friendly interfaces inc. ® ™"]
	input_box(text_lines, "red", "Press Enter to quit", False, 0, 15)
	

def intro() -> None:
	''' intro '''
	ui.clear()
	num_lines:int = ui.draw_box_outline("s", "top", "yellow", "black", "centre")
	num_lines += ui.draw_box_outline("s", "body", "yellow", "black", "centre")
	num_lines += ui.draw_box_body("s", "Welcome to this ~magenta~workshop", "centre", "yellow", "black", "green", "black", "centre")
	num_lines += ui.draw_box_outline("s", "body", "yellow", "black", "centre")
	num_lines += ui.draw_box_outline("s", "bottom", "yellow", "black", "centre")	
	text_lines:list = ["","You will now be forced to create an account, accept all terms and conditions,",
					   "whether you like it or not.",
					   "", "You will be asked to create a ~green~username ~white~and ~cyan~password~white~,",
					   "but will not be given any idea of the type or number of characters needed",
					   "until you try and enter it.","",
					   "This is ~red~by design ~white~and for your ~green~health ~white~and ~yellow~safety","","",
					   "~blue~©user-friendly interfaces inc. ® ™"]
	num_lines += ui.draw_multi_line_box("d", text_lines, "red", "black")
	ui.add_lines(5, num_lines)
	ui.draw_line("d", "white", "black")
	ui.display_message("Press Enter to continue:", True, False)	

def sign_in(accounts:dict) -> None:
	''' request sign in '''
	valid:bool = False
	account:dict = None
	while not valid:
		text_lines:list = ["", "", "", "Type your ~blue~username ~white~in the box below","","",""]
		username:str = input_box(text_lines, "blue", "Type your ~blue~username~white~", False, 0, 15)		
		if username not in accounts.keys():
			ui.display_message("Username not recognised. Try again", False, True, "cyan", "dgrey")
		else:
			valid = True
			account = accounts[username]
	
	valid = False		
	while not valid:
		text_lines:list = ["","", "Type your ~red~password ~white~in the box below","","",""]
		password:str = input_box(text_lines, "red", "Type your ~red~password~white~", False, 0, 15)		
		if password != account["password"]:
			ui.display_message("Incorrect password. Try again", False, True, "cyan", "dgrey")
		else:
			valid = True

def welcome(account) -> None:
	''' welcome message '''
	ui.clear()
	num_lines:int = ui.draw_box_outline("d", "top", "green", "black", "centre")
	num_lines += ui.draw_box_outline("d", "body", "green", "black", "centre")
	num_lines += ui.draw_box_body("d", f"~white~Thank you ~green~{account['firstname']} ~white~for signing up to this ~magenta~workshop", "centre", "green", "black", "green", "black", "centre")
	num_lines += ui.draw_box_outline("d", "body", "green", "black", "centre")
	num_lines += ui.draw_box_outline("d", "bottom", "green", "black", "centre")	
	text_lines:list = ["","You can now sign in to your account using the username and password","",
					   "you entered when creating the account","","If you get it wrong, you will be ~red~deleted.",
					   "", "", "~blue~©user-friendly interfaces inc. ® ™"]
	num_lines += ui.draw_multi_line_box("d", text_lines, "blue", "black")
	ui.add_lines(5, num_lines)
	ui.draw_line("d", "white", "black")
	ui.display_message("Press Enter to continue:", True, False)		
	
def main() -> None:		
	ui.set_console(80, 25, "white", "black")
	accounts:dict = {}
	intro()
	account:dict = create_account()
	accounts = add_account(accounts, account)
	welcome(account)
	sign_in(accounts)
	display_account(account)
	
main()
input("Enter to quit") # only required if running in console/terminal
