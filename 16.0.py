

def power_adder(number, power):
    our_number = number**power
    string_of_our_number = str(our_number)
    list_of_numbers = []
    for n in string_of_our_number:
        list_of_numbers.append(int(n))
    print(sum(list_of_numbers))


power_adder(2, 1000)