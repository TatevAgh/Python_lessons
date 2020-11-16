# *Create a collection of filenames with their size,
# print how many files are greater than 15Mb, how many filenames start from ‘a’ letter,
# increase size of the file which name ends with ‘.txt’

files = {'main.js': 25, 'index.html': 10, 'armenia.html': 10, 'style.css': 50,  'main.py': 15, 'myNotes.txt': 12, 'apple.js': 25}
count_15_greater = 0
starts_from_a = 0
files_txt = []
for file in files.values():
    if file > 15:
        count_15_greater += 1
print('Files count that are greater than 15Mb:', count_15_greater)
for file in files.keys():
    if file[0] == 'a':
        count_15_greater += 1
print('Count of filenames start from ‘a’ letter:', count_15_greater)
for txt in files.keys():
    if 'txt' in txt:
        files[txt] += 25

print(files)

