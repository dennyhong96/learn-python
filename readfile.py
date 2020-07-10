# open('text.txt', 'r')  # read mode
# open('text.txt', 'r+')  # read and write mode
# open('text.txt', 'a')  # append mode

text_file = open('text1.txt', 'w')  # write mode
print(text_file.readable())  # r and r+ mode
print(text_file.writable())  # w, a, and r+ mode

# print(text_file.read())
# print(text_file.readline())
# print(text_file.readline())

# for line in text_file.readlines():
#     print(line)

text_file.write('this is a brand new line\n')

text_file.close()
print(text_file.closed)
