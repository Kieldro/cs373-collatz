#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

import math

DEBUG = not True
cache = {}

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array on int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    # preconditions
    assert i > 0
    assert j > 0
    
    if i > j:	i, j = j, i		# swap
    assert i <= j
    
    if i < j/2:		# makes Sphere v1 run slower, idk why
    	i = j/2
    
    v = 1
    for n in xrange(i, j+1):		# xrange() does not include last number
    	cLen = cycleLength(n)
    	v = max(cLen, v)
    
    # invariant
    assert v >= cLen
    
    # return value validity
    assert v > 0
    
    return v

# -------------
# cycleLength
# -------------

def cycleLength (n):
	"""
	n is an integer > 0
	return the cycle length of n
	"""
	# preconditions
	assert n > 0;
	
	v = 1
	k = n
	while k != 1:
		if DEBUG: print k
		#check cache
		if k in cache:
			v += cache[k] -1
			break
		if k % 2:
			k = k + (k >> 1) + 1		# computes 2 steps
			v += 2
		else:
			k /= 2
			v += 1
	# cache n
	cache[n] = v
	
	# invariant
	assert k > 0, 'invariant violated.' + str(k)
	
	# postconditions
	assert cache != {}, 'Nothing was cached.'
	
	# return value validity
	assert v > 0
	
	return v

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)

# ----
# main
# ----

if __name__ == "__main__":
	import sys
	collatz_solve(sys.stdin, sys.stdout)
