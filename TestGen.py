
def maxCycle (i, j):
	cLen = 1
	for n in xrange(i, j+1):
		v = cycleLength(n)
		cLen = max(cLen, v)
	
	return cLen

def cycleLength (k):
	v = 1

	while k != 1:
		if k % 2:
			k = k + (k >> 1) + 1		# computes 2 steps
			v += 2
		else:
			k /= 2
			v += 1
	
	return v

# main
step = 100
for i in xrange(1, 10**3-step, step):
	j  = i + step
	print str(i)	 + ' ' + str(j) + ' ' + str(maxCycle(i, j) )

