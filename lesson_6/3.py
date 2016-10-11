import numpy as np
import random
import matplotlib.pyplot as plt

def get_percentile(values, bucket_number):
    p = 100/bucket_number
    res = []
    count = 0
    res.append(0.0)
    count += p
    while count < 100:
        res.append(np.percentile(values, count))
        count += p
    return res

def get_percentile_number(value, percentiles):
    i = 0
    while percentiles[i] <= value:
        i += 1
        if i >= len(percentiles):
            i -= 1
            return i
    return i-1

def value_equalization(value, percentiles, addRandom=False):
    if not addRandom:
        idx = get_percentile_number(value, percentiles)
        step = 1 / len(percentiles)
        value = idx*step
        return value
    else:
        idx = get_percentile_number(value, percentiles)
        step = 1 / len(percentiles)
        random_noise = random.uniform(0, step)
        value = idx*step + random_noise
        return value

def values_equalization(values, percentiles, addRandom=False):
    res = []
    for i in values:
        res.append(value_equalization(i, percentiles, addRandom))
    return res

v = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
p = (get_percentile(v, 4))
#print(p)
#print(get_percentile_number(7.75, p))
#print(get_percentile_number(5.5, p))
#print(values_equalization(v, p))
#print(values_equalization(v, p, addRandom=True))

s = []
with open('img.txt', 'r') as f:
    for line in f:
        v = list(map(float, line.strip().split()))
        s.append(v)
#print(s)
data = np.array(s)


plt.subplot(321)
plt.imshow(data, cmap=plt.get_cmap('gray'))

plt.subplot(322)
val = [data.flatten()]
plt.hist(val, bins=10)

#n = int(input())
p = get_percentile(val, 200)

new_data = np.array(values_equalization(data.flatten(), p, addRandom=True))
ready = new_data.reshape(200, 267)

plt.subplot(323)
plt.imshow(ready, cmap=plt.get_cmap('gray'))

plt.subplot(324)
data = [ready.flatten()]
plt.hist(data, bins=10)

plt.subplot(325)

plt.show()
