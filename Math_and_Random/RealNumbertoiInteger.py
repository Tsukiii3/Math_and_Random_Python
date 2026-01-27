import math
r = float(input('Enter a number with a decimal point: '))
i = math.trunc(r) #math.trunc() removes the fractional part of a number
print('The integer part is: ',i)