import math

# global caus f**k style :D
#          0       1      2
primes = [False, False, True]
def is_prime(n):

	# iter through primes checking modulo
	def check_prime(num):
		for a in range(2, int(math.sqrt(num))+1):
			if primes[a] and num % a == 0:
				return False
		return True

	# consult cache
	if n < len(primes):
		return primes[n]

	# iterate and fill in missing values
	for i in range(len(primes), n + 1):
		p = check_prime(i)
		primes.append(p)

	# return result
	return primes[n]


def iter_primes():
	for a in range(len(primes)):
		if primes[a]:
			yield a


# get a list of prime factors
p_factors = {}
def prime_factors(n):
	if n < 2:
		return []

	# consult cache
	if n in p_factors:
		return p_factors[n]

	# make sure we have primes up till n
	is_prime(n)

	for prime in iter_primes():
		if n % prime == 0:
			result = [prime] + prime_factors(n / prime)
			p_factors[n] = result
			return result

	return []

# coalesce common prime factors
pruned_p_factors = {}
def prune_prime_factors(n):

	# consult cache
	if n in pruned_p_factors:
		return pruned_p_factors[n]

	# get prime factors
	pf = prime_factors(n)

	# solve
	ans = []
	for p in pf:
		flag = True
		for i in range(len(ans)):
			if p == ans[i][0]:
				ans[i] = (ans[i][0], ans[i][1] + 1)
				flag = False
				break

		if flag:
			ans.append((p, 1))

	# save answer
	pruned_p_factors[n] = ans
	return ans

# get answ
def check_four_consec(n):
	pf1 = set(prune_prime_factors(n))
	pf2 = set(prune_prime_factors(n+1))
	pf3 = set(prune_prime_factors(n+2))
	pf4 = set(prune_prime_factors(n+3))

	if len(pf1) != 4 or len(pf2) != 4 or len(pf3) != 4 or len(pf4) != 4:
		return False

	s = pf1.union(pf2).union(pf3).union(pf4)
	if len(s) != 16:
		return False

	return True


# get solution :D
check = 0
while (True):

	# monitor progress
	if check % 1000 == 0:
		print check

	if check_four_consec(check):
		print check, check+1, check+2, check+3
		break

	check += 1



