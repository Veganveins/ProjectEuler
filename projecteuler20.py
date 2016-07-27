
def factorial(x):
    product = 1
    n = 2
    while n < x+1:
        product = product * n
        n += 1

    product = list(str(product))
    product = map(int, product)
    product = sum(product)
    return product

print factorial(100)


    