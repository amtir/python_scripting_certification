#!/usr/bin/python3

n = int(input("Enter a number (n>0): "))
sum_series = sum([i / (i + 1) for i in range(1, n + 1)])

print(f"{sum_series:.2f}")








 