# sum of the first even 4 million fibonacci numbers


def fib(upper_limit):
    a = 0
    b = 1
    d = [0, 1]

    # printing the sequence for specific values of the upper limit
    if upper_limit == 0:
        print([])

    elif upper_limit == 1:
        print([a])

    elif upper_limit == 2:
        print(d)

    # defining a general sequence
    else:
        for x in range(2, upper_limit):
            # defining the next number in the sequence and switching values of variables
            c = a + b
            a = b
            b = c
            d.append(c)
        return d


sequence = fib(40000)
sequence_of_only_even_numbers = []

# selecting for only even numbers
for each_number in sequence:
    if each_number % 2 == 0:
        sequence_of_only_even_numbers.append(each_number)

sum_of_even_fib_numbers = sum(sequence_of_only_even_numbers)

print(sum_of_even_fib_numbers)
