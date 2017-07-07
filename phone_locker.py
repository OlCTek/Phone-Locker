import csv
import time
import sys

password = '3486'
phone_dict = {}
confirm = ['yes', 'Yes', 'y', 'Y']
add_phone = ['add', 'Add']
no = ['no', 'No', 'n', 'N']
cancel = ['cancel', 'Cancel', 'quit', 'Quit']
exit = ['no', 'No', 'exit', 'Exit', 'n', 'N']

def exit_pro():
	print("Very well.")
	time.sleep(1)
	print("Shutting down database...")
	time.sleep(1)
	print("Goodbye!")
	time.sleep(1)
	sys.exit()
	
def add():
	a = 0
	print("Please enter phone number owner: ")
	user_key = raw_input("User input: ")
	time.sleep(1)
	if user_key in exit:
		exit_pro()
	elif user_key in cancel:
		print("Canceling database editor...")
		time.sleep(1)
		return
	while a == 0:
		print("Please enter phone number: ")
		user_phone = raw_input("User input: ")
		time.sleep(1)
		if user_phone in exit:
			exit_pro()
		elif user_phone in cancel:
			print("Canceling database editor...")
			time.sleep(1)
			return
		if len(user_phone) != 10:
			print("Invalid number.")
			time.sleep(1)
		else:
			try:
				int(user_phone)
				a += 1
			except ValueError:
				print("Invalid number.")
				time.sleep(1)
	print("Saving new number to database...")
	time.sleep(1)
	global phone_dict
	phone_dict.setdefault(user_key, user_phone)

def main():
	while True:
		print("Please enter desired number: ")
		user_in = raw_input("User input: ")
		time.sleep(1)
		if user_in in phone_dict.keys():
			print("Phone number for " + user_in + ": " + phone_dict[user_in])
			time.sleep(1)
		elif user_in in exit:
			exit_pro()
		elif user_in in add_phone:
			print("Preparing to add phone number to directory...")
			time.sleep(1)
			add()
		else:
			print("Phone number for " + user_in + " does not exist. Add to database?")
			user_in = raw_input("User input: ")
			time.sleep(1)
			if user_in in confirm or user_in in add_phone:
				add()
			elif user_in in no:
				print("Very well.")
				time.sleep(1)
			elif user_in in exit:
				exit_pro()
			else:
				print("Very well.")
				time.sleep(1)
		print("Would you like to continue?")
		user_in = raw_input("User input: ")
		time.sleep(1)
		if user_in in exit:
			exit_pro()

print("Welcome to Phonebook Database (PBD)")
time.sleep(1)
a = 0
while a < 3:
	print("Please input master password for access: ")
	user_in = raw_input("User input: ")
	time.sleep(1)
	if user_in == password:
		print("Access granted.")
		time.sleep(1)
		print("Initiating phone number database lookup...")
		time.sleep(1)
		main()
	else:
		print("Access denied.")
		time.sleep(1)
		a += 1
print("Exiting system.")
time.sleep(1)
sys.exit()