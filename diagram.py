import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)

lower_bound = np.percentile(data, 25)
upper_bound = np.percentile(data, 75)

filtered_data = [x for x in data if x >= lower_bound and x <= upper_bound]

plt.plot(filtered_data)
plt.show()