print('Please, input the character')
character = input()

if character >= 'a' and character <= 'z' or character >= 'A' and character <= 'Z':
    if character in 'aeiouAEIOU':
        print('Vowel')
    else:
        print('consonant')
else:
    print('Nothing')
