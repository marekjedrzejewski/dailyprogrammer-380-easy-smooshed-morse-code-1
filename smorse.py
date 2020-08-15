morse_letters = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. ' + \
    '--- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'

char_to_morse = {}
i = ord('a')
for letter in morse_letters.split():
    char_to_morse[chr(i)] = letter
    i += 1


def smooshed_morse(text):
    morse = ''
    for letter in text:
        morse += char_to_morse[letter]
    return morse
