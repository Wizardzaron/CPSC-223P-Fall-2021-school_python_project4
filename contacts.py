#Ryan Haddadi
#September 18 2021
#The purpose of this file is to add, modify, and delete contacts from the users listings as well as use key value pairs 

#this function adds a contact to the list and uses keyword and positional parameters, if statements, and key value pairs
def add_contact(contact_dictionary, id, first_name, last_name):
	if (id in contact_dictionary):
		return str("error")
	else:
		contact_dictionary[id] = [first_name, last_name]
		return contact_dictionary[id]
#this function modifies the contacts list and uses keyword and positional parameters, if statements, and key value pairs
def modify_contact(contact_dictionary, id, first_name, last_name):
	if (id not in contact_dictionary):
		return "error"
	else:
		contact_dictionary[id] = [first_name, last_name]
		return contact_dictionary[id]
#this function deletes contacts from the list and uses keyword and positional parameters, and if statemests
def delete_contact(contact_dictionary,id):
	if (id not in contact_dictionary):
		return str("error")
	else:
		return contact_dictionary.pop(id)
#this function sorts through the list from lastname and then first name
def sort_contacts(contact_dictionary):
	contact_dictionary = dict(sorted(contact_dictionary.items(), key =lambda x:x[1][1].lower(), reverse=False))
	contact_dictionary = dict(sorted(contact_dictionary.items(), key = lambda x:x[1][0].lower(), reverse = False))	
	return contact_dictionary
#this finds the specified contact from the list the user desires
def find_contact(contact_dictionary, find):
	dictionary = {}
	if (find.isnumeric() and int(find) in contact_dictionary.keys()):
		dictionary[int(find)] = contact_dictionary[int(find)]
	else:
		for key, value in contact_dictionary.items():
			if (find.lower() == value[0].lower() or find.lower() ==value[1].lower()):
				dictionary[key] = value
				sort_contacts(dictionary)
	return dictionary
