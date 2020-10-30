# Lets generate some triangle numbers

triangle_numbers = []

sum = 0
for num in range(1, 100000):
    sum += num
    triangle_numbers.append(sum)

# now we need to print the factors of these numbers

factors = []

for tri_num in triangle_numbers:
    factors_of_tri_num = []
    for possible_divisors in range(1, tri_num+1):
        if tri_num % possible_divisors == 0:
            factors_of_tri_num.append(possible_divisors)
    factors.append(factors_of_tri_num)

for list_of_factors in factors:
    if len(list_of_factors) >= 500:
        index_of_desired_number = factors.index(list_of_factors)
        print(triangle_numbers[index_of_desired_number])
        break
