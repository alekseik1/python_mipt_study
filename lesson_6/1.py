import random
import matplotlib.pyplot as plt

random.seed(0)
values1 = [random.normalvariate(0, 1) for i in range(100)]
values2 = [random.normalvariate(0, 1) for i in range(1000)]
values3 = [random.normalvariate(0, 1) for i in range(10000)]
values4 = [random.normalvariate(0, 1) for i in range(100000)]

plt.subplot(221)
plt.hist(values1, bins=100)

plt.subplot(222)
plt.hist(values2, bins=100)

plt.subplot(223)
plt.hist(values3, bins=100)

plt.subplot(224)
plt.hist(values4, bins=100)

plt.show()