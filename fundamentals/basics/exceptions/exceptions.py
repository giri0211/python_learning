# dictionary of strings
acronyms = {'LOL': 'laugh out loud',
            'IDK': 'I dont know',
            'TBH': 'to be honest'}
print(acronyms['LOL'])

def get_reminder_and_divison_results(a, b):
    if b == 0: 
        raise ZeroDivisionError
    
    divisionResult = a // b
    reminder =  a % b
    print('division result is:', divisionResult)
    print('reminder result is :', reminder)

try:
    
    get_reminder_and_divison_results(10, 0)
    # lol = acronyms['LOL1']
except:
    print('acronym does not exist')
finally:
    print('Below are the acronyms: ')
    for acronym, value in acronyms.items():
        print(acronym, value)


raise ZeroDivisionError