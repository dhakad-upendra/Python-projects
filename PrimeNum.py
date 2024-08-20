# Your task is to write a function checking whether a number is prime or not.

def factorial(num):
    fact_is = num
    for i in range(1, fact_is):
        fact_is = fact_is * i
    return fact_is


def check_is_prime(num):
    factorial_is = factorial(num - 1)
    if factorial_is % num == num - 1:
        results = True
        return results
    else:
        results = False
        return results


def is_prime(results_is):
    if results_is == True:
        print('''
          The number is 
           ------------
          |            |
          |   Prime    |
          |            |
           ------------ ''')
    else:
        print('''
                  The number is 
                  ------------
                 |            |
                 | Not-Prime  |
                 |            |
                  ------------ ''')


print('''
    --------------------------------------
    Program to find the number is prime or not ...
    --------------------------------------''')
number = int(input("Enter the number:"))

result = check_is_prime(number)
is_prime(result)
