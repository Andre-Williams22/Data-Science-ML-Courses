
#help(range)


# for i in range(10):
#     print(i)

# to have it start at 1 instead of 0
# for i in range(1, 10):
#     print(i)

# range (start, stop, step)
# for i in range(0, 21, 2):
#     print(i)

# word = 'python'

# for i in word:
#     print(i, end=' ')

data = [50, 80, 88, 90, 3, 32, 40, 50, 32]

# data[0]
# data[-1]
# data[:-1] ## everything except last number 
# data[::-1] ## flips order of the list
# data[:5] ## first five elements

# sum of contents in the list
# total = 0 
# for num in data:
#     total += num
# print(total)

# total_2 = sum(data)
# print(total_2)

# write a function to find maximum value in a list
# find_max = 0
# for item in data:
#     if item > find_max:
#         find_max = item
# print('the maximum number is: ',find_max)

# my_list = [1, 21, 32, 24, 54, 60]
# for i in range(6):
#     print(my_list[i])

# Bubble Sort
# data = [50, 80, 88, 90, 3, 32, 40, 50, 32]
# data_copy = data[:]
# for i in range(len(data_copy)):
#     for j in range(0, len(data_copy)-i-1):
#         if data_copy[j] > data_copy[j+1]:
#             data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j] 

# print(data_copy)
## Built in sort function 
# print(sorted(data))

# new_list = [1, 55, 77]
# new_list.append(45)
# new_list.remove(55)
# new_list.reverse() # or new_list[::-1]
# new_list.extend([37,38,39])# allows you to add another list
# new_list.index(77)


# While loops 
# n = 10 

# while n > 0:
#     print(n)
#     n = n-1

# user_input = int(input('enter ages of class member. Type -1 to end: '))
# ages = []
# while user_input > 0:
#     ages.append(user_input)
#     user_input = int(input('The next age: '))
# print('The ages are',ages)

## put a counter in the while loop 

# user_input = input('please enter names. Type n to end: ')
# counter = 0
# names = []
# while user_input != 'n':
#     counter +=1 
#     names.append(user_input)
#     print(f'{user_input} was added.')
#     user_input = input('The next age: ')
# print(f'There are {counter} people and they are {names}.')

# Modulos - gives the remainder of division 

# Fizzbuzz game
# n = 100
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, 'Fizzbuzz')
#     elif i % 3 == 0:
#         print(i, 'Fizz')
#     elif i % 5 == 0:
#         print(i, 'Buzz')
#     else:
#         print(i)

print(list(range(0,10,1)))
# print(list(range(0,10,2)))