def get_contacts_by_name(contacts):
  """Return a dict list view of contact details that matches the given name"""
  
  name = input("Enter the name to search for: ")  # request name
  print()

  filtered_contacts = {k: v for k, v in contacts.items() if v["Name"].lower() == name.lower()}  # filter contacts by name

  return filtered_contacts.values()

def find_contact(contacts, name):
   for contact in contacts.values():  # We only need the contact information 
    if contact["Name"].lower() == name.lower(): 
      return contact
    return None


def get_names(contacts):
  names = []
  for contact_id, contact_info in contacts.items():
    names.append(contact_info["Name"])
  return names

















#def get_contacts_by_age(contacts):
 # return sorted(contacts.values(), key=lambda contact: contact["Age"])

#def get_phone_number_by_name(contacts, name):
  for contact_id, contact_info in contacts.items():
    if contact_info['Name'].lower() == name.lower():
      return contact_info['PhoneNumber']
    return None


#def sort_contacts_by_name(contacts):
 # sorted_contact_details = sorted(contacts.items(), key=lambda item: item[1]["Name"].lower())
 # return {contact_id: details for contact_id, details in sorted_contact_details}

#def sort_contacts_by_age(contacts):
#  """Return a dict list view of contact details sorted by age from youngest to oldest."""

 # return sorted(contacts.values(), key=lambda contact: contact["Age"])


#def sort_contacts_by_name(contacts):
 # """Return a dict list view of contact details sorted by name in alphabetical order."""

  #return sorted(contacts.values(), key=lambda contact: contact["Name"])

 # location = input("Enter the location to search for: ")  # request location
  #print()

  #filtered_contacts = {k: v for k, v in contacts.items() if v["Location"].lower() == location.lower()}  # filter contacts by location

  #return filtered_contacts.values()


#def get_contacts_by_number(contacts):
 # """Return a dict list view of contact details that matches the given number"""

  #number = input("Enter the phone number to search for: ")  # request phone number
  #print()

  #filtered_contacts = {k: v for k, v in contacts.items() if v["PhoneNumber"] == int(number)}  # filter contacts by phone number

  #return filtered_contacts.values()