# *Create a collection of dates (date like ‘1/11/2018’ with weekday like ‘Monday’),
# print total number of date, dates for non-working days (Saturday, Sunday)

weekdays = {'11/05/2020': 'Monday', '15/07/2020': 'Saturday', '20/04/2020': 'Wednesday', '06/07/2020': 'Sunday', '15/04/2020': 'Saturday'}
count = 0
holydays = []
print('Total number of  date is:', len(weekdays))
for day in weekdays.items():
    if 'Saturday' in day or 'Sunday' in day:
        holydays.append(day[0])
        count += 1

print('Count of non-working days:', count)
print('Datesfor non-working days:', holydays)
