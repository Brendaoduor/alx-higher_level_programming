#!/usr/bin/python3
def fizzbuzz(x):
    is_fizz = x % 3 == 0
    is_buzz = x % 5 == 0

    if is_fizz and is_buzz:
        return 'FizzBuzz'

    if is_fizz:
        return 'Fizz'

    if is_buzz:
        return 'Buzz'

    return x


r = map(fizzbuzz, range(1, 100))

print(list(r))
