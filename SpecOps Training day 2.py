                        """Իրականացնել strmove() ֆունկցիան, որը տրված տողը ցիկլիկ տեղաշարժում է դեպի աջ տրված քանակով։
                        Օրինակ, strmove(“hello”, 2); կտեղաշարժի “hello”-ն 2 դիրքով դեպի աջ և կստանա “lohel”։"""



def shift_right(string, move):
    return string[len(string) - move :] + string[: len(str) - move]


print(shift_right("hello", 2))

                        """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
                        The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."""

sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)

                        """Each new term in the Fibonacci sequence is generated by adding the previous two terms.
                        By starting with 1 and 2, the first 10 terms will be:
                        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
                        By considering the terms in the Fibonacci sequence whose values do not exceed four million,
                        find the sum of the even-valued terms."""


def fibonacci(n):
    first = 1
    seconds = 2

    while n > 1:
        first, seconds = seconds, first + seconds
        n -= 1
    return first


num = 1
fib_num = 0
sum = 0
while fib_num < 4000000:
    fib_num = fibonacci(num)
    if num % 2 == 0:
        sum += fib_num
    num += 1

print(sum)
