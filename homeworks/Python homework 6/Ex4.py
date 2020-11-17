# *Create 2 collections for storing movies that have been watched by 2 persons,
# get movies that are watched by at least one of them,
# get movies that are watched by 1-st and not watched by 2-nd, print results

first_person = {'Game Night', 'Enola Holmes', 'Venom', 'Bridge of Spies', 'Spy'}
second_person = {'The Last Samurai', 'The Old Guard', 'Enola Holmes', 'Monos', 'Spy'}
print('movies that are watched by at least one of them: ', first_person&second_person)
print('movies that are watched by 1-st and not watched by 2-nd: ', first_person-second_person)
