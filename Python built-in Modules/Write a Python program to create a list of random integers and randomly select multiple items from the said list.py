import random
print("Create a list of random integers:")
population = range(0,100)
nums_list = random.sample(population, 10)
print(nums_list)
no_element = 4 
print("\nRandomly select",no_element,'multiple items from the said list:')
result_elements = random.sample(nums_list,no_element)
print(result_elements)
no_element = 8
print("\nRandomly select",no_element,"multiple items from the said list:")
result_elements = random.sample(nums_list,no_element)
print(result_elements)