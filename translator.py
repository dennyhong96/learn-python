
def translate(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if not(letter.isupper()):
                result += "g"
            else:
                result += "G"
        else:
            result += letter
    return result


print(translate(input('Enter a phrase to translate: ')))
