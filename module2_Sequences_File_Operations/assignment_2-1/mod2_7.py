#!/usr/bin/python3

input_string = input("Enter a string: ")
character_count = {}

for character in input_string:
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1

for character, count in character_count.items():
    print(f"{character},{count}")







