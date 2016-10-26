import numpy as np
import matplotlib.pyplot as plt
import math
import pylab
import matplotlib.ticker as ticker
x = range(1, 8)
y = [204.6, 409.4, 614.8, 819.6, 1025.6, 1231.9, 1437.8]
koef = np.polyfit(x, y, deg=1, cov=True)
#print(koef)
plt.subplot(121)

plt.errorbar(x, y, xerr=0, yerr=0.1)
plt.yticks(range(200, 1500, 50))
plt.grid(True)
line1 = plt.plot(x, y)

y = [183.7, 368.3, 552.8, 738.3, 921.3, 1108.4, 1293.9]
plt.errorbar(x, y, xerr=0, yerr=0.1)
plt.yticks(range(200, 1500, 50))
plt.grid(True)
line1 = plt.plot(x, y)

y = [158.4, 318.2, 476.6, 636.8, 796.3, 958.3, 1118.3]
plt.errorbar(x, y, xerr=0, yerr=0.1)
plt.yticks(range(200, 1500, 50))
plt.grid(True)
line1 = plt.plot(x, y)

y = [131.9, 273.4, 396.8, 549, 665.4, 826.7, 936.2]
plt.errorbar(x, y, xerr=0, yerr=0.1, fmt='+')
v, p = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(v)
plt.yticks(range(0, 1500, 50))
plt.grid(True)
line1 = plt.plot(x, p_f(x))

y = [100.3, 202.5, 304.2, 407.6, 511.5, 615.6, 720.2]
plt.errorbar(x, y, xerr=0, yerr=0.1, fmt='+')
v, p = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(v)
plt.yticks(range(0, 1500, 50))
plt.grid(True)
line1 = plt.plot(x, p_f(x))


#plt.text(2.5, 1300, r"m=2.5 kg", bbox={'facecolor':'white', 'pad':10})
plt.title('')
pylab.legend( ("2.4 kg", "1.9 kg", "1.5 kg", "1 kg", "0.5 kg"), loc='best')

plt.subplot(122)
y = [103.3**2, 136.4**2, 160.7**2, 185.0**2, 205.6**2]
y = [x/10**3 for x in y]
print(y)
x = [4.9, 9.8, 14.21, 19.11, 23.81]
plt.grid()
plt.xticks(range(1, 25, 1))
plt.yticks(range(10, 45, 1))
v, p = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(v)
plt.title(r'$k = ' +str(round(v[0], 1))+' * 10^3$')
plt.errorbar(x, y, xerr=0, yerr=0.5, fmt='o')
plt.plot(x, p_f(x))
plt.show()
