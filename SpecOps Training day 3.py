
                        """Գրել ծրագիր, որը հաշվում է 1-ից 100 թվերի գումարի քառակուսին (1+...+100)^2, հաշվում է 1-ից 100
                        թվերի քառակուսիների գումարը՝ (1^2 + 2^2 + … + 100^2): Ծրագիրը տպում է ստացված թվերի տարբերությունը։"""


sum_square = 0
squares_sum = 0

for i in range(1, 101):
    sum_square += i
    squares_sum += i**2
sum_square = sum_square**2

print(sum_square - squares_sum)


                        """Տրված է անուններ պարունակող ֆայլը (https://projecteuler.net/project/resources/p022_names.txt),
                        արտագրել արժեքները մեկ այլ ֆայլում, որտեղ մեծատառով կլինեն միայն անունների առաջին տառերը։ """


from urllib.request import urlopen

with open("Capitalized_names.txt", "w") as file:
    for line in urlopen("https://projecteuler.net/project/resources/p022_names.txt"):
        file.write(line.decode("utf-8").title())
        
        

"""https://leetcode.com/problems/palindrome-number/
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Constraints:
-2^31 <= x <= 2^31 - 1"""

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

print(isPalindrome(515))
print(isPalindrome(-242))
print(isPalindrome(434))
print(isPalindrome(123454321))