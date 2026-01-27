import random
s1 = input('Enter the name of the first student: ')
s2 = input('Enter the name of the second student: ')
s3 = input('Enter the name of the third student: ')
s4 = input('Enter the name of the fourth student: ')
s5 = input('Enter the name of the fifth student: ')
chosen = random.choice([s1, s2, s3, s4, s5]) # random.choice() selects a random element from a list
print('The chosen student was {}'.format(chosen))