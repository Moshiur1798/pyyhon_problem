print('Please, input the character')
character = input()

if character >= 'a' and character <= 'z':
    print('Lower case')
elif character >= 'A' and character <= 'Z':
    print('Upper case')
else:
    print('Nothing')
