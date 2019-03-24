"""Problem S2: Pretty Average Primes
Problem Description
For various given positive integers N > 3, find two primes, A and B such that N is the average
(mean) of A and B. That is, N should be equal to (A + B)/2.
Recall that a prime number is an integer P > 1 which is only divisible by 1 and P. For example,
2, 3, 5, 7, 11 are the first few primes, and 4, 6, 8, 9 are not prime numbers.
Input Specification
The first line of input is the number T (1 ≤ T ≤ 1000), which is the number of test cases. Each of
the next T lines contain one integer Ni (4 ≤ Ni ≤ 1 000 000, 1 ≤ i ≤ T).
For 6 of the available 15 marks, all Ni < 1 000.
Output Specification
The output will consist of T lines. The ith line of output will contain two integers, Ai and Bi
,
separated by one space. It should be the case that Ni = (Ai + Bi)/2 and that Ai and Bi are prime
numbers.
If there are more than one possible Ai and Bi for a particular Ni
, output any such pair. The order
of the pair Ai and Bi does not matter.
It will be the case that there will always be at least one set of values Ai and Bi for any given Ni
.
Sample Input
4
8
4
7
21
Possible Output for Sample Input
3 13
5 3
7 7
13 29
Explanation of Possible Output for Sample Input
Notice that:
8 = (3 + 13)/2,
4 = (5 + 3)/2,
7 = (7 + 7)/2, """

""" Slower version
primes = [2]
t0 = time.time()
for p in range (2, 100000):
    prime = True
    if (p % 2 != 0 and p % 3 != 0):
        max_divisor = math.floor(math.sqrt(p))
        for i in primes:
            if (i < 1 + max_divisor):
                if (p % i == 0):
                    prime = False
            else: break
        if prime:
            primes.append(p)
print(primes)
t1 = time.time()
print(t1-t0)
"""

import time
import math

### make a list of primes
primes = list()
def is_prime(n):

    if n== 1:
        return False

    if n ==2:
        return True
    if n> 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n% d == 0:
            return False
    return True

for n in range(1, 1000000):
    if is_prime(n):
        primes.append(n)

### make a list of Primes

times = int(input())

for i in range(times):
    number = int(input())*2
    max_check = math.floor(number)
    for i in primes:
        if (i < max_check):
            resultant = number - i
            if is_prime(resultant):
                print(i, " ", resultant)
                break
