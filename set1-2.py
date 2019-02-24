def vowel_or_consonant(c):
    if not c.isalpha():
        return 'Neither'
    vowels = 'aeiou'
    if c.lower() in vowels:
        return 'Vowel'
    else:
        return 'Consonant'
for c in input():
    print (c, vowel_or_consonant(c))
