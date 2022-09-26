#!/usr/bin/python3
def no_c(my_string):
    result ="".join([i for i in my_string if i != 'c' and i != 'C'])
    return (result)

no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

