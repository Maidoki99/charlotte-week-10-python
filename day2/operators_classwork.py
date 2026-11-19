# 1. Arithmetic Operators
number1 = 24
number2 = 6

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)
print(25 // 4)
print(25 % 4)
print(3 ** 2)


# 2. Comparison Operators
score = 65

print(score > 50)
print(score < 50)
print(score == 65)
print(score != 65)


# 3. Assignment Operators
points = 20
points += 5
points -= 3
points *= 2

print(points)


# 4. Logical Operators
age = 19
has_ticket = True
print(age >= 18 and has_ticket)

day = 'Saturday'
print(day == 'Saturday' or day == 'Sunday')

is_raining = False
print(not is_raining)


# 5. Membership Operators
my_foods = ['rice', 'beans', 'yam', 'masa', 'fufu']

print('rice' in my_foods)
print('pizza' not in my_foods)


# 6. Identity Operators
first = [10, 20]
second = first
third = [10, 20]

print(first is second)
print(first is third)
print(first is not third)
print(first == third)
# Difference: == checks if the values inside the lists are the same, while 'is' checks if both variables point to the exact same list in memory.


# 7. Bitwise Operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(6 << 1)
print(6 >> 1)
print(~6)
# ~6 gives -7 because Python flips all the binary bits of 6 using signed two's complement, which follows -(x + 1).


# 8. Ternary Expression
temperature = 30
status = 'Hot' if temperature > 25 else 'Cool'
print(status)


# 9. Mini Project: Personal Score Checker (with Extension)
name = input('Abdullahi:')
score = int(input('150: '))

if score < 0 or score > 100:
    print('Invalid score')
else:
    remaining = 100 - score
    passed = score >= 50
    result = 'Pass' if passed else 'Try again'

    print('Hello', name)
    print('Your score is', score)
    print('Marks to reach 100:', remaining)
    print('Passed:', passed)
    print('Result:', result)
