<h1>Tutorial Part4</h1>

This part demonstrates one method of taking the code from [Tutorial-Part3](Tutorial-Part3.md) and breaking it into functions and procedures.
The file is now here at [ExerciseAnswer.py](/Python/ExerciseAnswer.py).

There is a completely over-the-top solution [here](/Python/ExerciseAnswerColorama.py). that uses the colorama-based [ui.py](/Python/lib/ui.py). module to output in colour, but who would be stupid enough to use over 1200 lines of code to do the same job?

Going through the code:
```python
def main() -> None:		
	accounts:dict = {}
	intro()
	account:dict = create_account()
	accounts = add_account(accounts, account)
	welcome(account)
	sign_in(accounts)
	clear()
	print("We are ready to go!") # start application
 ```
An empty dictionary called accounts (note:plural) is created, and after an introduction to the program, a new dictionary called account (note:singular) is created from user input and added to accounts.

A welcome message is displayed.

The user is invited to sign in to their new account.

The application can start from here, so a simple text message is printed out instead.
