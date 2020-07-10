# number = None
# user_input = input('Enter a number: ')
# try:
#     number = int(user_input)
#     print(number)
# except:
#     print(f'{user_input} is not a valid number')


try:
    # value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
