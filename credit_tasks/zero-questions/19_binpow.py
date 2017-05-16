# Быстрое возведение в степень
def binpow(a, n):
	if n == 0:
		return 1
	if n % 2 == 1:
		return binpow(a, n-1) * a
	else:
		b = binpow(a, n/2)
		return b*b
# Тесты
import random
for i in range(100):
	print(*[x**i - binpow(x, i) for x in random.sample(range(100), 10)])
