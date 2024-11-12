oceans = ["pacific", 'atlantic',"indian", 'southern', 'arctic']

# overwrite
# with open('data/oceans.txt', 'w') as file:
#     for ocean in oceans:
#         file.write(ocean)
#         file.write('\n')

# file Append
# with open('data/oceans.txt', 'a') as file:
#     for ocean in oceans:
#         file.write(ocean)
#         file.write('\n')

# use print to write into file
with open('data/oceans.txt', 'a') as f:
    for ocean in oceans:
        print(ocean, file=f)