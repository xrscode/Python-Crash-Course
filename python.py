# from datetime import datetime
# current_time = datetime.now()

# import random

# random_list = [random.randint(1,100) for i in range(101)]

# import module_name as name_you_pick_for_the_module

# #random.sample takes a list and randomly selects k items from it
# new_list = random.sample(list, k)
# #for example:
# nums = [1, 2, 3, 4, 5]
# sample_nums = random.sample(nums, 3)
# print(sample_nums) # 2, 5, 1

# import codecademylib3_seaborn
# from matplotlib import pyplot as plt

# Add your code below:
# import codecademylib3_seaborn
# from matplotlib import pyplot as plt
# import random

# numbers_a = range(1, 13)
# numbers_b = random.sample(range(1000), 12)

# plt.plot(numbers_a, numbers_b)
# plt.show()

cost_of_gum = 0.10
cost_of_gumdrop = 0.35
 
cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.44999999999999996

from decimal import Decimal
 
cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')
 
cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996




# Import library below:
from library import always_three


# Call your function below:
print(always_three())