contacts = {
    'number': 4,
    'students': 
        [
            {'name':'girish', 'email': 'girish@example.com'},
            {'name':'ramu', 'email': 'ramu@example.com'}
        ]
}
# drill down into dictionary that has list of dictionaries
for student in contacts.get('students'):
    print (student['name'] )
    
    
# try key value pair
for key , value in contacts.items():
    print(key, value)