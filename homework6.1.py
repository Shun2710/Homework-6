# Task 6.1

import string

s = input().strip()
start, end = s.split('-')
alphabet = string.ascii_letters

i1 = alphabet.index(start)
i2 = alphabet.index(end)

print(alphabet[i1:i2+1])