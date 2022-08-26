'''                    """Task #1  Տրված ֆայլում պարունակվում են թվեր։ Իրականացնել ծրագիր, որը հաշվում և վերադարձնում է ֆայլում պարունակվող թվերի գումարը։"""

sum = 0
given_file = open(
    "Filee.txt",
    "r",
)
for i in given_file:
    try:
        sum += int(i)
    except:
        print(f" {i}.is not number")
print(f"sum is {sum}")

given_file.close()

                    """Task #2 Տրված ֆայլում պարունակվում է տեքստ։ Իրականացնել ծրագիր, որը ֆայլի մեջ պարունակվող տեքստի բոլոր
                    բառերի առաջին տառերը դարձնում է մեծատառ և ձևափոխված ամբողջ տեքստը պահպանում մեկ այլ ֆայլում։"""

with open("File.txt", "r") as text_file:
    with open("Cap_letter", "w") as new_file:
        for line in text_file:
            line = line.title()
            new_file.write(line)

                    """Task #3 Օգտագործելով աղյուսակ (dictionary) հաշվել զանգվածում բոլոր թվերի կրկնությունների քանակը։"""

my_array = [1, 2, 4, 5, 3, 4, 1, 2, 1, 2, 1, 3, 4, 5, 7, 8, 9]
empty_array = {}

for num in my_array:
    if not empty_array.get(num):
        empty_array[num] = 1
    else:
        empty_array[num] += 1
print(empty_array)


                    """Task #4 Տեքստային ֆայլի համար իրականացնել ծրագիր, որը կհաշվի ֆայլում հանդիպող սիմվոլների քանակը:"""

sum = 0
with open("File.txt", "r") as file:
    for char in file.read():
        if char != " " and char != "\n":
            sum += 1
print(sum)

                    """Task #5 Իրականացնել ֆունկցիա, որը կհեռացնի ստացված տողի (string) ամեն երրորդ սիմվոլը։"""


str_example = "123123123123123123123123"


def del_third_sym(string, index):
    new_string = ""
    for i in range(0, len(string), index):
        new_string += string[i : i + index - 1]
    return new_string


print(f"Input: {str_example}")
print(f"Output: {del_third_sym(str_example, 3)}")

                    """Task #6 Իրականացնել ծրագիր, որը կհաշվի թե յուրաքանչյուր բառ քանի անգամ է հանդիպում տեքստային ֆայլում։"""

counter = {}
with open(
    "Lyric.txt",
    "r",
) as text:
    for line in text:
        for word in line.split():
            if counter.get(word):
                counter[word] += 1
            else:
                counter[word] = 1
print(counter)


                    """Task #7 Գրել ծրագիր, որը կհաշվի տրված զանգվածի արժեքների քառակուսիները և կպահի դրանք նոր զանգվածում՝ սորտավորված ձևով։"""

massive_2 = [1, 2, 4, 5, 3, 4, 1, 2, 1, 2, 1, 3, 4, 5, 7, 8, 9]
empety = []
for x in massive_2:
    empety.append(x**2)
empety.sort()

print(empety)

                    """Task #8 Հաշվել տրված թվի թվանշանների գումարը։ Օրինակ, տրված է 4637, վերադարձնել 4+6+3+7"""

number = 1998
box = 0
while number > 0:
    box += number % 10
    number //= 10
print(box)

                    """Task #9 Հաշվել տրված թվի թվանշանների արտադրյալի և գումարի տարբերությունը։ Օրինակ, տրված է 4637, վերադարձնել (4*6*3*7) - (4+6+3+7)"""

number = 1998
sum = 0
prod = 1
while number > 0:
    sum += number % 10
    prod *= number % 10
    number //= 10
print(prod - sum)

                    """Task #10 Գրել ֆունկցիա, որը ստանում է միջակայքի սկիզբ և վերջը (երկու թվեր) և հաշվում միջակայքում գտնվող կենտ թվերի քանակը։ 
                    Օրինակ, 3 և 7 միջակայքում կա երեք կենտ թիվ (3, 5, 7)։"""



def number_odds(start, end):
    count = 0
    for num in range(start, end + 1):
        if num % 2 != 0:
            count += 1
    return count


print(number_odds(3, 7))
print(number_odds(5, 111))
'''