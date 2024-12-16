import math

# Initialize starting point
x, y = 0, 0

# Movements: direction and steps
movements = [("UP", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2)]

# Process each movement
for direction, steps in movements:
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

# Calculate distance from origin
distance = math.sqrt(x**2 + y**2)

print(f"Distance from origin: {distance:.2f}")