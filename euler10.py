# #Find the sum of all the primes below 2 million
#15.7 seconds
import time
start_time = time.time()

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
# function that determines if a number is prime
from math import pow
 
j=2
A=[]
for z in xrange(0,2000000):
    A.append(z)
    A[z]=True
 
#for j in xrange(2,3):
while j<1415:
    n=0
    if A[j]==True:
 
        while n*j+pow(j,2) <2000000:
            k=int(n*j+pow(j,2))
            n=n+1
            A[k]=False #set all the numbers to false such that when you square 
            #them they are less than 2 million (getting rid of nonprimes)
    j=j+1
 
 
B=[]    #all the numbers that are still true at this point must be prime
#add all those primes into an array called B
for m in xrange(2,2000000):
    if A[m]==True:
        B.append(m)
stop=len(B)
 
sum = 0
for s in xrange(0,stop):
    sum = sum + B[s]
print "Sum of all primes below two million is: <<", sum , ">> Result returned in: ", (time.time() - start_time), "seconds"
 
 
