# import math

# print(math.pi)

# import random 
# # j = random.randint(1,10)
# counter = 0 
# while counter < 10:
#     counter += 1
#     j = random.randint(1,10)
#     print(j)

# import webbrowser
# webbrowser.open('https://docs.python.org/3/library/webbrowser.html') # opens up the website 

## Dictionaries 

# capitals = {'France': 'Paris', 'England':'London', 'USA':'D.C.', 'Mexico':'Mexico City','Spain': 'Madrid', 
#     'Ireland':'Dublin', 'Greece': 'Athens', 'Italy':'Rome'}

#capitals['Germany] ## grab a value
#capitals.get('Germany') ## grab a value

# capitals['South Korea'] = 'Seoul' ## add a new entry

# print(capitals)
# capitals.keys() # prints all the keys 
# capitals.values() ## prints all the values
# capitals.items() ## prints everything out into tuples

# iterate over keys
# for country in capitals:
#     print(country)

# iterate over values
# for country,city in capitals.items():
#     print(f'The country is {country} and the city is {city}')

# L = [2, 4, 5,2,1,7,8]
# print(4 in L) # this will quickly tell if a number is in the list


list1 = [1, 2, 4, 6, 7, 28, 12, 33]
list2 = ['a', 'b', 'c', 'd']

joined = list(zip(list1, list2)) # zip has its on type. zip indexes both items together, so index 1 in both lists will still be index 1
print(joined)

i,j = zip(*joined)
print(joined[0])