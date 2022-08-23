"""Task #1  Տրված ֆայլում պարունակվում են թվեր։ Իրականացնել ծրագիր, որը հաշվում և վերադարձնում է ֆայլում պարունակվող թվերի գումարը։"""

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
