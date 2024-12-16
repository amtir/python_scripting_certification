import numpy, matplotlib.pyplot as plt

x = numpy.arange(5)
plt.plot(x, x, label='linear')
plt.plot(x, x*x, label='square')
plt.plot(x, x*x*x, label='cube')

plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polynomial Graph')
plt.legend()
plt.savefig('plot.png')
plt.show()