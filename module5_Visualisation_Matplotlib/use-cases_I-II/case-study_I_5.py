import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data points for X and y
X = [1, 2, 3, 4]
y = [20, 21, 20.5, 20.8]
y_error = [0.12, 0.13, 0.2, 0.1]

# 5.1: Draw a Simple plot
plt.figure(figsize=(4, 5), dpi=100)
plt.plot(X, y)
plt.show()

# 5.2: Configure the line and markers in simple plot
plt.figure(figsize=(4, 5), dpi=100)
plt.plot(X, y, linestyle='--', marker='o', color='b')
plt.show()

# 5.3: Configure the axes
plt.figure(figsize=(4, 5), dpi=100)
plt.plot(X, y, linestyle='--', marker='o', color='b')
plt.xlim(0, 5)
plt.ylim(19, 22)
plt.show()

# 5.4: Give title of Graph & labels of x axis and y axis
plt.figure(figsize=(4, 5), dpi=100)
plt.plot(X, y, linestyle='--', marker='o', color='b')
plt.xlim(0, 5)
plt.ylim(19, 22)
plt.title('Sample Plot', fontsize=14)
plt.xlabel('X Axis', fontsize=14)
plt.ylabel('Y Axis', fontsize=14)
plt.show()

# 5.5: Give error bar
plt.figure(figsize=(4, 5), dpi=100)
plt.errorbar(X, y, yerr=y_error, linestyle='--', marker='o', color='b')
plt.xlim(0, 5)
plt.ylim(19, 22)
plt.title('Sample Plot with Error Bars', fontsize=14)
plt.xlabel('X Axis', fontsize=14)
plt.ylabel('Y Axis', fontsize=14)
plt.show()

# 5.6: Define width, height as figsize=(4,5) DPI and adjust plot dpi=100
# (already applied in previous plots)

# 5.7: Give a font size of 14
# (already applied in previous plots)

# 5.8: Draw a scatter graph of any 50 random values of x and y axis
random_x = np.random.rand(50)
random_y = np.random.rand(50)
plt.figure(figsize=(4, 5), dpi=100)
plt.scatter(random_x, random_y)
plt.title('Random Scatter Plot', fontsize=14)
plt.xlabel('Random X', fontsize=14)
plt.ylabel('Random Y', fontsize=14)
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()

# 5.9: Create a dataframe and draw a scatterplot
data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
}
df = pd.DataFrame(data)

# Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
plt.figure(figsize=(4, 5), dpi=100)
plt.scatter(df['preTestScore'], df['postTestScore'], s=df['age']*10, alpha=0.5)
plt.title('Pre Test Score vs Post Test Score', fontsize=14)
plt.xlabel('Pre Test Score', fontsize=14)
plt.ylabel('Post Test Score', fontsize=14)
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()

# 5.10: Scatterplot with size = 300 and the color determined by sex
plt.figure(figsize=(4, 5), dpi=100)
plt.scatter(df['preTestScore'], df['postTestScore'], s=300, c=df['female'], alpha=0.5, cmap='bwr')
plt.title('Pre Test Score vs Post Test Score by Gender', fontsize=14)
plt.xlabel('Pre Test Score', fontsize=14)
plt.ylabel('Post Test Score', fontsize=14)
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()
