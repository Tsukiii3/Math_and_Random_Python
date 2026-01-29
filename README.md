# Math_and_Random_Python

**Python Projects – Math and Random Modules**

This repository contains small Python programs that demonstrate the use of the math and random modules, focusing on basic mathematical calculations and random operations.

**Features**

1 - Generate a random number

Generates a random floating-point number between 0 and 1 and displays it with two decimal places.

import random
num = random.random()
print("Number is {:.2f}".format(num))

2 - Integer part of a number

Receives a real number from the user and displays only its integer part.

import math
r = float(input('Enter a real number (use a dot): '))
i = math.trunc(r)
print(i)

3 - Hypotenuse calculation

Calculates the hypotenuse of a right triangle using the opposite and adjacent sides provided by the user.

import math
co = float(input('Enter the opposite side value: '))
ca = float(input('Enter the adjacent side value: '))
hi = math.hypot(co, ca)
print('The hypotenuse value is {:.2f}'.format(hi))

4 - Trigonometric functions

Calculates the sine, cosine, and tangent of an angle entered by the user.

import math
angle = float(input('Enter the angle value: '))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))
print('The angle {}° has sine {:.2f}, cosine {:.2f}, and tangent {:.2f}'.format(angle, sine, cosine, tangent))

5 - Random student selection

Randomly selects one student from five names provided by the user.

import random
a1 = input('Enter the first student name: ')
a2 = input('Enter the second student name: ')
a3 = input('Enter the third student name: ')
a4 = input('Enter the fourth student name: ')
a5 = input('Enter the fifth student name: ')
choice = random.choice([a1, a2, a3, a4, a5])
print('The selected student is {}'.format(choice))

6 - Shuffle students order

Randomly shuffles the order of the five students entered by the user.

import random
a1 = input('Enter the first student name: ')
a2 = input('Enter the second student name: ')
a3 = input('Enter the third student name: ')
a4 = input('Enter the fourth student name: ')
a5 = input('Enter the fifth student name: ')
students = [a1, a2, a3, a4, a5]
random.shuffle(students)
print('The order will be {}'.format(students))
Technologies Used

**Python 3.14**

math module: trunc(), hypot(), sin(), cos(), tan()

random module: random(), choice(), shuffle()

**How to Use**

Clone the repository:

git clone https://github.com/Tsukiii3/Math_and_Random_Python

Navigate to the project folder:

cd Math_and_Random_Python

Run the desired script using Python:

python file_name.py

Follow the instructions displayed in the terminal.
