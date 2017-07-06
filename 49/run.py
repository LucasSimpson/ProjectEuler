
# COMPUTE PRIMES LIST
PRIMES = 10000

# calc all primes
primes = [True for a in range(PRIMES+1)]
primes[0] = False
primes[1] = False
primes[2] = True
check = 0
while(check <= len(primes) / 2 + 1):
	
	# find next prime	 
	while(not primes[check]):
		check += 1

	# flag all non-primes
	flag = check * 2
	while(flag < len(primes)):
		primes[flag] = False
		flag += check

	check += 1

# consolidate
filtered_primes = []
for i in range(len(primes)):
	if primes[i] and len(str(i)) == 4:
		filtered_primes.append(i)

# rename
primes = filtered_primes

# find combos
combos = []
for a in range(len(primes)):
	print primes[a]
	for b in range(a+1, len(primes)):
		for c in range(b+1, len(primes)):

			# check easy stuff first
			if primes[c] - primes[b] == primes[b] - primes[a]:

				# be explicit!
				p1 = set(str(primes[a]))
				p2 = set(str(primes[b]))
				p3 = set(str(primes[c]))
				
				# check numbers are the same
				if p1 == p2 == p3:
					combos.append((primes[a], primes[b], primes[c]))

print combos

for c in combos:
	print '%s%s%s' % (c[0], c[1], c[2])