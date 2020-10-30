from math import sqrt

list_of_primes = []


def list_prime_hunter(list_of_integers):
    for element in list_of_integers:
        factors = 0
        list_of_integers = list(range(2, int(sqrt(element))+1))
        for each_number in list_of_integers:
            if element % each_number == 0:
                factors += 1
        if factors == 0:
            list_of_primes.append(element)
        if 1 in list_of_primes:
            list_of_primes.remove(1)


list_prime_hunter(list(range(10)))
print(sum(list_of_primes))


