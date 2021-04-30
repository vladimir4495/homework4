
#task 1
"""
Write a program that generates a random number
between 1 and 10 and lets the user guess what number
was generated. The result should be sent
back to the user via a print statement.
"""

if __name__ == '__main__':
    import random

atempt = 10
print('Угадайте число от 1 до 10')
number = random.randint(1, 10)
while atempt < 10:
    usrnumb = int(input('Введите число: '))
    atempt += 1
    if number < usrnumb:
        print('Число было меньше. Попробуйте еще раз.')
    elif number > usrnumb:
        print('Число было больше. Попробуйте еще раз.')
    else:
        print('Вы угадали ')
if usrnumb == number:
    atempt = str(atempt)
    print('Вы угадали с ' + atempt + ' попыток.')
else:
    print('ВЫ не угадалию')



# Task 2
"""
Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”
"""

print('Your name')
name = input()
age = int(input('Enter your age:'))
age1 = age + 1
print('Congrats ' + name + ' next year you`ll be the ', + age1, 'years old.')


"""
Task 3

Words combination
Create a program that reads an input string and then creates and 
prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should 
print 5 random strings(words) that combine characters 
‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
"""
import random


def my_function(lenght):
    W = input('Enter the word: ')
    res = ''.join(random.choice(W) for i in range(lenght))
    print('', res.lower())


my_function(10)
