# Description: Putting collections together
# Author: Israel Colman

# Creating contact info
contact_info = {
    'name': 'Israel',
    'address': '123 Main Street',
    'city': 'Salt Lake City',
    'state': 'Utah',
    'zip_code': '84101'
    }

print(
    f'{contact_info['name']}\n'
    f'{contact_info['address']}\n'
    f'{contact_info['city']}, {contact_info['state']}\n'
    f'{contact_info['zip_code']}'

)

# Removing name
contact_info.pop('name')
print(contact_info)

# New variable Full Name
full_name = {
    'first name': 'Israel',
    'last name': 'Colman'
    }

# Using update
full_name.update({'honorific': 'Mr.'})

print(full_name)

contact_info.update({'full_name': full_name})

print(
    f'{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}\n'
    f'{contact_info['address']}\n'
    f'{contact_info['city']}, {contact_info['state']}\n'
    f'{contact_info['zip_code']}'
)