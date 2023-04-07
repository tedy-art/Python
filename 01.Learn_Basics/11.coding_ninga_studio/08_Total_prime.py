def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def totalPrime(S,E):
    count = 0
    for i in range(S, E+1):
        if is_prime(i):
            count += 1
    return count

S,E = map(int,input().split(' '))
print(totalPrime(S,E))