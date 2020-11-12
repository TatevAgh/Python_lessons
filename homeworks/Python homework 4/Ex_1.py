# *Define a collection of weekdays, print following: first 5 week days, total days number, last 2 days, odd days

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('first 5 week days: ', weekdays[:5])
print('total days number is: ', len(weekdays))
print('last 2 days', weekdays[-2:])
print('odd days', weekdays[::2])