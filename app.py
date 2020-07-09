# is_male = False
# is_tall = False


# if bool(is_male):
#     print('You are a male!')
# else:
#     print('You are not a male!')

# if is_male and is_tall:
#     print('Nice!')
# elif is_male and not(is_tall):
#     print('You are a short male')
# elif not(is_male) and is_tall:
#     print('You are not a male but tall')
# else:
#     print('You are not tall and not a male!')


# if is_male or is_tall:
#     print('Ok!')
# else:
#     print('You are neither male not tall')


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(4, 400, 3))

print(2 != 3)
print(2 == 2)
print(not(2 == 2))
