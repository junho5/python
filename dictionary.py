my_dictionary = {
    '엄마': 'mom',
    '아빠': 'father',
    '아들': 'son'
}

print(my_dictionary['엄마'])
my_dictionary['딸'] = 'sister'
print(my_dictionary)

print(my_dictionary.values())
print(my_dictionary.keys())

print('mom' in my_dictionary.values())
print('엄마' in my_dictionary.keys())

for key in my_dictionary.keys():
    value = my_dictionary[key]
    print(key, value)


for key, value in my_dictionary.items():
    print(key, value)


