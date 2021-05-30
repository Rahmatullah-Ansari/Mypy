from random import *
import pyautogui
password = input('Enter your password:')
lst = '0123456789'
password_list = list(lst)
guess = ''
while guess != password:
    guess = ''
    for i in range(len(password)):
        letter = password_list[randint(0,9)]
        guess = str(letter) + str(guess)
    print('----'+str(list(guess))+'----')
print('Your password is :'+guess)