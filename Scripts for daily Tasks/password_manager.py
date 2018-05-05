"""	stores (account_name, password) in the form of dictionaries
	and copies password in clipboad on running the script by entering
	the account name as input.
"""
import pyperclip
import sys
PASSWORDS = {'email':'mark@gmail.com', 'password': 1234}


if len(sys.argv) < 2:
	print('[account] - copy account password')
	sys.exit()
account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password of ' + account + ' is copied.')
else:
	print('there is no account named as ' + account)
