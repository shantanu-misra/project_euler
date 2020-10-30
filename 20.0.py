

def factorial_sum(number):
    list_of_numbers = list(range(1, number+1))
    result = 1
    for each_number in list_of_numbers:
        result = result * each_number
    list_of_numbers_in_factorial = []
    string_of_result = str(result)
    for n in string_of_result:
        list_of_numbers_in_factorial.append(int(n))
    print(sum(list_of_numbers_in_factorial))


factorial_sum(100)