# adding multiples of 3 and 5 


def adder(upper_limit):
    # Defining 2 sets with multiples of 3 and 5
    multiples_of_3 = set(range(0, upper_limit, 3))
    multiples_of_5 = set(range(0, upper_limit, 5))
    
    # Take a union of the two lists
    set_of_multiples_of_3_and_5 = multiples_of_5.union(multiples_of_3)

    # Take the sum of the elements in the set
    return sum(set_of_multiples_of_3_and_5)



#print(adder(100000))
