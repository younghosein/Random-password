import string
import random

def str_random(length):
    letters = string.ascii_lowercase
    result = ''.join((random.choice(letters))for x in range(length))
    print('random string :',result)
    
length = int(input('please enter length :'))
str_random(length)