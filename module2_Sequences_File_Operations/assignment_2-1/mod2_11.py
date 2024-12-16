#!/usr/bin/python3

input_list = [12,24,35,70,88,120,155]
output_list = [input_list[i] for i in range(len(input_list)) if i not in [0,4,5]]

print(output_list)






    