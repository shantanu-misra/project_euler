# Sum square difference

upper_limit = 100
list_of_natural_numbers = list(range(1, upper_limit+1, 1))
list_of_squares = []

for each_number in list_of_natural_numbers:
    squared_numbers = each_number**2
    list_of_squares.append(squared_numbers)

sum_square_difference = sum(list_of_natural_numbers)**2 - sum(list_of_squares)
print(sum_square_difference)