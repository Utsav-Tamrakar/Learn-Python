#Prime factorization
def prime_factors(n):
  i = 2
  factors = []
  while i * i <= n:
    while n % i == 0:
      factors.append(i)
      n //= i
    i += 1
  if n > 1:
    factors.append(n)
  return factors

num = int(input("Enter a number for prime factorization: "))
factors = prime_factors(num)
print("Prime factors:", factors)