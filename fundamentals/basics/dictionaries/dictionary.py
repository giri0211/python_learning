# dictionary of strings
acronyms = {'LOL': 'laugh out loud',
            'IDK': 'I dont know',
            'TBH': 'to be honest'}
print(acronyms['LOL'])

# empty_dictionary = {}
# empty_dictionary['LOL'] = 'laugh out loud' 

# # deletes the element from dictionary
# # del empty_dictionary['LOL']
# value = empty_dictionary.get('LOL')
# # use get to avoid error in case of missing element by key.

# if value:
#     print('key exists', value)
# else:
#     print('key does not exist', value)
    
sentense = 'IDK' + ' what happend ' + "TBH"
print(acronyms.get('IDK'), 'what happend', acronyms.get('TBH'))