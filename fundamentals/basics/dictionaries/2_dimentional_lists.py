menus = {'breakfast': ['egg snadwitch', 'beagel', 'coffee'],
         'lunch' : ['Turkey sandwitch','BLT']}

print('breakfast menu:\t', menus['breakfast'])

# use items() method on the dictionary
for name, menu in menus.items():
    print(name , menu)
    
# print(menus.get('breakfast'))