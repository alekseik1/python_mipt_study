import equalize as eq

values = [3.0, 4.0, 1.0, 2.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

print('Test eq.get_percentile()')
print(eq.get_percentile(values, 4))
print(eq.get_percentile(values, 3))

print('Test eq.get_percentile_number()')
print(eq.get_percentile_number(2.5, eq.get_percentile(values, 4)))
print(eq.get_percentile_number(5.5, eq.get_percentile(values, 4)))
print(eq.get_percentile_number(100, eq.get_percentile(values, 4)))

print('Test eq.value_equalization()')
print(eq.get_percentile(values, 5))
print(eq.value_equalization(5.5, eq.get_percentile(values, 5)))
print("#", eq.value_equalization(5.5, eq.get_percentile(values, 5), add_random = True))

print('Test eq.values_equalization()')
print(eq.get_percentile(values, 4))
print(eq.values_equalization(values, eq.get_percentile(values, 4)))
print("#", eq.values_equalization(values, eq.get_percentile(values, 4), add_random = True))