# Largest palindrome product

range1 = range(1, 100)
range2 = range(1, 100)
list_of_palindrome_products = []

# finding palindrome products and adding them to a list
for num1 in range1:
    for num2 in range2:
        product = str(num1*num2)
        reversed_product = product[::-1]
        if reversed_product == product:
            x = "".join(product)
            list_of_palindrome_products.append(x)

print(list_of_palindrome_products)

# printing the last element of the list as it'll be the largest
print(list_of_palindrome_products[-1])