# *Define a collection of programming languages (names), add new language name from console if it’s not C#

languages = ['Python', 'Javascript', 'Java', 'C#', 'C++']
new_language = input('Add new language: ')

if new_language != 'C#':
    languages.append(new_language)
    print(languages)
else:
    print('You inputed C#')
