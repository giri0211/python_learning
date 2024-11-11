# what to add
# add definition of acronym
# write both to the File

acronym = input('give the acronym to add: ?\n')
acronymDef = input('give the acronym definition to add: ?\n')

with open('input.txt', 'a') as file:
    file.write(acronym + '-' + acronymDef + '\n')
