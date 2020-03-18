import random
import string

numbers= int(input("how many passwords do you want? "))
length = int(input("how long shall the password be? "))

chars = string.ascii_letters + string.digits + '!@#$%^&*().,;-_"£€?^§°ç[]}{'

for n in range(numbers):
    rnd = random.SystemRandom()
    print(''.join(rnd.choice(chars) for i in range(length)))