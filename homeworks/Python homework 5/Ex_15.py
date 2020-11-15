# *Create a collection for storing hotel visitors (name, country),
# input several visitors from console, print how many visitors are now in hotel,
# what is their country, what is their name

guests = {'Gregory': 'Georgia', 'Sergey': 'Russia', 'Anahit': 'Armenia', 'John': 'Usa'}
while len(guests) <= 6:
    add_name = input('Enter Name of guest: ')
    guests[add_name] = input('Add country: ')

print('In hotel are now', len(guests), 'gouests')
print('Guests countries are', guests.values())
print('Guests names are', guests.keys())