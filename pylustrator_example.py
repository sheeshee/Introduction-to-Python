import matplotlib.pyplot as plt
import pylustrator

# Create some data
xdata = [i/2 for i in range(-20, 20)]
ydata = [x**2 for x in xdata]

pylustrator.start()

plt.plot(xdata, ydata)
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.title('My Fe from pylustrator
plt.show()