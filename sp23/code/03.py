from math import sqrt

# print all palindrome primes between 1 and N


def palPrime(N):
    n = 1
    while n <= N:
        if isPrime(n) and isPalindrome(str(n)):
            print(n)
        n = n + 1

# return True if n is prime, and false otherwise


def isPrime(n):
    i = 2
    while i <= int(sqrt(n)):
        if n % i == 0:
            return False
        i = i + 1
    return True

# return True if the string s is a palindrome, and false otherwise


def isPalindrome(s):
    return s == s[::-1]
