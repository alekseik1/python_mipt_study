import math
# Проверка числа на простоту.
def check(N):
	for i in range(2, round(math.sqrt(N))+1):
		if N % i == 0:
			return False
	return True
# Тесты.
print(check(int(input())))
