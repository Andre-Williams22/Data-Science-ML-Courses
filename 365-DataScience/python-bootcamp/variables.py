# x = 5 

# y = 12 

# z = x+y

# print(z) 

# z = x-y

# user_input = int(input(" how many apples do you have?\n >>> "))

# print('nice, you have ' + str(user_input) + ' apples.')

# Bob, Ann, Jane and Ashwin want to order pizza - they know the will each eat 4 slices of pizza. The local pizza shop sells pizzas of
# only 6 slices. What is the minimum number of pizzas needed - Use floor division

num_slices = 4*4 
pizza_slices = 6 
pizzas = (pizza_slices+num_slices) // 6

slices_left = pizzas*6 - num_slices

print("The minimum number of pizzas they will need is: " + str(pizzas)+ " there will be " + str(slices_left) + " slices left.")