print(2**3)


def raise_to_power(base, pow):
    result = 1
    for i in range(pow):
        print(f'i is: {i}')
        result *= base
    return result


print(raise_to_power(2, 3))
