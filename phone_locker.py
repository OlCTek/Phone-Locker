import csv
import time
import sys

password = '3486'
name = ["name", "Name"]
number = ["number", "Number", "#"]
confirm = ['yes', 'Yes', 'y', 'Y']
add_phone = ['add', 'Add']
no = ['no', 'No', 'n', 'N']
cancel = ['cancel', 'Cancel', 'quit', 'Quit']
exit = ['no', 'No', 'exit', 'Exit', 'n', 'N']

with open('phonebook.csv', 'rb') as phonebook:
	reader = csv.reader(phonebook)
	phone_dict = dict(reader)

def exit_pro():
	print("Very well.")
	time.sleep(1)
	print("Shutting down database...")
	with open('phonebook.csv', 'wb') as phonebook:
		writer = csv.writer(phonebook)
		for name, number in phone_dict.items():
			writer.writerow([name, number])
	time.sleep(1)
	print("Goodbye!")
	time.sleep(1)
	sys.exit()
	
def add():
	print("Please enter phone number owner: ")
	user_key = raw_input("User input: ")
	time.sleep(1)
	if user_key in exit:
		exit_pro()
	elif user_key in cancel:
		print("Canceling database editor...")
		time.sleep(1)
		return
	while True:
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
				break
			except ValueError:
				print("Invalid number.")
				time.sleep(1)
	print("Saving new number to database...")
	time.sleep(1)
	global phone_dict
	phone_dict.setdefault(user_key, user_phone)

def edit_name():
	while True:
		user_old = raw_input("Which contact would you like to edit?\nUser input: ")
		user_new = raw_input("What would you like to chance the contact name to?\nUser input: ")
		try:
			phone_dict[user_new] = phone_dict[user_old]
			break
		except KeyError:
			user_in = raw_input("Contact not in directory. Add to database?\nUser input: ")
			time.sleep(1)
			if user_in in yes:
				print("Preparing to add phone number to directory...")
				time.sleep(1)
				add()
			else:
				print("Very well.")
				time.sleep(1)
				print("Exiting database editor...")
				time.sleep(1)
				break
		
			
	
def edit():
	while True:
		print("Would you like to edit a name or number?")
		user_in = raw_input("User input: ")
		time.sleep(1)
		if user_in in name:
			edit_name()
			break
		elif user_inn in number:
			edit_number()
			break
		else:
			print("Invalid input.")
	
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
				print("Preparing to add phone number to directory...")
				time.sleep(1)
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
	elif user_in in cancel or user_in in exit:
		exit_pro()
	else:
		print("Access denied.")
		time.sleep(1)
		a += 1
print("Exiting system.")
time.sleep(1)
sys.exit()