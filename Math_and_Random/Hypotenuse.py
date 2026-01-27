import math
opposite = float(input('Enter the value of the opposite side: '))
adjacent = float(input('Enter the value of the adjacent side: '))
hypotenuse = math.hypot(opposite, adjacent) # math.hypot() calculates the hypotenuse using the Pythagorean theorem
print('The value of the hypotenuse is {:.2f}'.format(hypotenuse))