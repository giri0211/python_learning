try:
    with open('data/guido_bio.txt') as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print ('None')