import math
import random

length = int(input('password length: '))

caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lows = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums = ['0','1','2','3','4','5','6','7','8','9']
other = ['!','"','§','$','%','&','/','(',')','=','?','{','[',']','}','+','*','~','#','\'','-','_','.',':',',',';','<','>','|',]

def get_random_char():
    lists = [caps, lows, nums, other]
    chosen = lists[random.randint(0,len(lists)-1)]
    return chosen[random.randint(0, len(chosen)-1)]

pw_as_list = []

if length < 8:
    print('That is too insecure!')
else:
    for i in range(length):
        pw_as_list.append(get_random_char())
    
    password = ''.join(pw_as_list)

    print(password)