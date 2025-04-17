my_dictionary={"name":"abir",
               "age":25,
               "major":"cse",
               "university":"ccn",
               "year":"4th"}

for key,vlaue in my_dictionary.items():
    print(key ,":" ,vlaue)

print(my_dictionary.keys())
print(my_dictionary.values())

print(my_dictionary['age'])


new_dics={'a','b','c','d'}
vlaue=10

update=dict.fromkeys(new_dics,vlaue)
print(update)

getonevlaue=update.get('b')
print(getonevlaue)
allvalue=update.items()
print(allvalue)
new_dics.update({'e':7})