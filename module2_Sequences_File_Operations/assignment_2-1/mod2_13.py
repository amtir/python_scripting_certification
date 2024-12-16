#!/usr/bin/python3

import random

output_list = [num for num in random.sample(range(1, 1001), 1000) if num % 5 == 0 and num % 7 == 0][:5]

print(output_list)






    