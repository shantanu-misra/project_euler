

def finding_last_n_digits_of_an_exponent_sum(upper_limit, last_n_digits):
    numbers_to_be_raised = list(range(1, upper_limit+1))
    expo_nums = []
    for number in numbers_to_be_raised:
        expo_nums.append(number ** number)
    post_sigma_number = sum(expo_nums)
    post_sigma_number = str(post_sigma_number)
    post_sigma_number_reversed = post_sigma_number[::-1]
    print(post_sigma_number_reversed[0:last_n_digits])


finding_last_n_digits_of_an_exponent_sum(1000, 10)