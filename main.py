from contacts import *

contact_dictionary = {}
choice = 0
while(choice >= 0 and choice < 6):
	print ("Please choose from the following choice")
	print ("1.)Add contact")
	print ("2.)Modify contact")
	print ("3.)Delete contact")
	print ("4.)Print contact list")
	print ("5.)Find contact")
	print ("6.)Exit the program")
	choice = int(input("Enter menu choice:"))
	if choice == 1:
		I = int(input("Please type in their phone number:"))
		firstname = input("What is the first name:")
		lastname = input("What is the last name:")
		add_contact(contact_dictionary,  first_name=firstname, last_name=lastname, id=I)
	elif choice == 2:
		I = int(input("What is the phone number of the contact you want to modify:"))
		firstname = input("What is the first name:")
		lastname = input("What is the last name:")
		modify_contact(contact_dictionary, first_name=firstname, last_name=lastname, id=I)
	elif choice == 3:
		I = int(input("What is the phone number of the contact you want to delete:"))
		delete_contact(contact_dictionary, id=I)
	elif choice == 4:
		print ("Last Name              First Name             Phone Number")
		check = dict(sorted(contact_dictionary.items(), key=lambda x: (x[1][1].lower(), x[1][0].lower()), reverse = False)) 
		for key,value in check.items():
			print(f'{value[1]:22}{value[0]:22}{str(key):8}')
	elif choice == 5:
		f = input("What is the phone number of the person you want to find")
		found_contacts=find_contact(contact_dictionary, find = f)
		for key,value in found_contacts.items():
                        print(f'{value[1]:22}{value[0]:22}{str(key):8}')
