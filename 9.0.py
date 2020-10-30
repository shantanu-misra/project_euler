
for a in range(190, 300):
    for b in range(190, 400):
        for c in range(190, 500):
            if (c>a)and(c>b):
                if a**2 + b**2 == c**2:
                    if a+b+c == 1000:
                        print(f'Triplet: [{a}, {b}, {c}], product = {a*b*c}')
