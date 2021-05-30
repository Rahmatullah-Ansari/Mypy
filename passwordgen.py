import random
import string
a = string.ascii_letters
a1 = string.digits
a2 = string.punctuation
lst = []
lst.extend(list(a))
lst.extend(list(a1))
lst.extend(list(a2))
random.shuffle(lst)
# print(lst)
plen = input('Enter length of password:')
if not(plen.isdigit()):
    print('Please enter digit.')
else:
    plen = int(plen)
print('Your password is = ',end=" ")
print("".join(lst[0:plen]))
