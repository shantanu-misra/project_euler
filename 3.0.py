number = 60085147

if number == 1:
    print('1 is not a prime number')

else:
    list_of_possible_factors_for_specific_number = list(range(1, number+1))
    factors_1 = []

    # selecting the factors
    for possible_factor in list_of_possible_factors_for_specific_number:
        if number % possible_factor == 0:
            factors_1.append(possible_factor)


    def prime_test(list_of_numbers, primes):
        # doing a primality test of each number in the factor list

        for num in list_of_numbers:
            list_of_possible_factors = list(range(2, int((num**0.5)+1)))
            factors = []
            for each_number in list_of_possible_factors:
                if num % each_number == 0:
                    factors.append(each_number)
            if len(factors) == 0:
                primes.append(num)

        largest_prime_factor = max(primes)

        print(f'The largest prime factor of {number} is {largest_prime_factor}')


    prime_test(factors_1, [])


















