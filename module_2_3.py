numbers = [1, 2, 1, 4, 5, 0, 6, 7, 8, 9, 10, 73, 1, 101, 11, 12, 13, 14, 15]
primes = []
not_primes = []
not_not_primes = []
for i in numbers:
  if i < 2:
    not_not_primes.append(i)
  for j in range(2, i+1):
    if i % j == 0 and i != j:
      not_primes.append(i)
      break
    elif i % j == 0 and i == j:
      primes.append(i)
print('Простые числа: ', primes)
print('Не простые числа :', not_primes)
print('Не простые, не составные: ', not_not_primes)