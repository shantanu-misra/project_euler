

def prime_hunter(range_of_numbers, primes_only):
    for num in range_of_numbers:
        factors = []
        list_of_possible_factors = list(range(2, int((num**0.5)+1)))
        for n in list_of_possible_factors:
            if num % n == 0:
                factors.append(n)
        if len(factors) == 0:
            primes_only.append(num)
    print(primes_only)
    print(primes_only[1000])


limit = 100000
range_to_be_hunted_in = list(range(2, limit))
prime_hunter(range_to_be_hunted_in, [])