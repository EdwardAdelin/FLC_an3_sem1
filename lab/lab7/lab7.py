import matplotlib.pyplot as plt
import numpy as np

#ex1
list1 = [1.4, 5.9, 2.6, 7.3, 8.5, 9.3, 6.1]
array1 = np.array(list1)
print(array1)

#ex2
even_numbers = np.arange(70, 92, 2)
print(even_numbers)

#ex3
diagonal_elements = [3, 7, 11]
matrix = np.diag(diagonal_elements)
print(matrix)

#ex4
array_1d = np.arange(10, 16)
array_2x3 = array_1d.reshape(2, 3)
print(array_2x3)

#ex5, presupub ca ex5 e singurul vector cu care lucram 
ex5 = np.array([[10, 50, 70, 20, 40], [5, 45, 95, 35, 65]])

below_43 = ex5[ex5 < 43]
print("Numbers below 43:", below_43)
above_43 = ex5[ex5 > 43]
print("Numbers above 43:", above_43)

#ex6
ex5 = np.array([[10, 50, 70, 20, 40], [5, 45, 95, 35, 65]])
np.savetxt("ex5.txt", ex5, fmt="%d")
loaded_ex5 = np.loadtxt("ex5.txt", dtype=int)
print("Loaded array from file:")
print(loaded_ex5)

#ex7,ex8,ex9
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 8))

# plot1
plt.subplot(3, 2, 1)
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker='o', color='b', markerfacecolor='r')  # Custom marker color
plt.title("Line with Custom Marker Color")
# plot2
plt.subplot(3, 2, 2)
plt.plot(x, np.cos(x), linestyle='--', color='g')  # Custom line style
plt.grid(True)
plt.title("Line with Custom Style and Grid")
# plot3
plt.subplot(3, 2, 3)
bars = np.random.randint(1, 10, 5)
bar_x = np.arange(len(bars))
plt.bar(bar_x, bars, color='purple', width=0.5)  # Custom color and width
plt.title("Vertical Bars with Custom Color and Width")
# plot4
plt.subplot(3, 2, 4)
y_scatter = np.random.rand(50)
x_scatter = np.random.rand(50)
colors = np.random.rand(50)  # Different colors for points
plt.scatter(x_scatter, y_scatter, c=colors, cmap='viridis')  # Color map
plt.title("Scattered Points with Different Colors")
# plot5
plt.subplot(3, 2, 5)
plt.plot(x, np.sin(x), linestyle='-', color='blue', label="sin(x)")
plt.plot(x, np.cos(x), linestyle=':', color='orange', linewidth=3, label="cos(x)")  # Custom width, color
plt.legend()
plt.title("Lines with Custom Style and Width")
# Plot 6
plt.subplot(3, 2, 6)
bars_h = np.random.randint(1, 10, 5)
bar_x_h = np.arange(len(bars_h))
plt.barh(bar_x_h, bars_h, color='cyan', height=0.7)  # Custom color and height
plt.title("Horizontal Bars with Custom Color and Height")
# afisez plots
plt.tight_layout() 
plt.show()
# Plot 7
plt.figure(figsize=(6, 4))
plt.plot(x, np.sin(x), color='blue', label="sin(x)")
plt.plot(x, np.cos(x), color='red', label="cos(x)")
plt.title("Intersecting Lines of Different Colors")
plt.legend()
plt.show()
# Plot 8
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 25, 35, 10, 15]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=140)
plt.title("Pie Chart with Custom Colors and Shadow")
plt.show()
