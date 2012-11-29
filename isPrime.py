import sys

def isPrime(n):

    if n is 2 or n is 3:
        return True
        
    if n is 1 or n%2 is 0 or n < 0:
        return False

    i = 3

    while ( i*i <= n ):

        if n % i is 0:
            return False

        i+=2
        
    return True

def nextPrime(n):

    if n%2 is 0: n+=1

    while ( isPrime(n) is not True ):
        n+=2

    return n

def nthPrime(n):

    k      = 3
    primes = [2]
    
    while len(primes) < n:
  
            if isPrime(k) is True:
                primes.append(k)
            
            k += 2
            
    return primes[n-1]


n = int(raw_input())

if isPrime(n) is True:
    print n, "is a prime number."

else:
    print n, "is NOT a prime number."
    print "The next prime number is", nextPrime(n)

primes = []

for i in range(1, 10000):
    if isPrime(i) is True:
        primes.append(i)


print "There are", len(primes), "primes between 1 and 10,000."

print "The", n, "th prime is", nthPrime(n)
    
