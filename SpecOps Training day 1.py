"""Task #1  Տրված ֆայլում պարունակվում են թվեր։ Իրականացնել ծրագիր, որը հաշվում և վերադարձնում է ֆայլում պարունակվող թվերի գումարը։"""

sum = 0
given_file = open(
    "C://Users//Asus//Desktop//Python//my_root//Classroom//Anaconda-SpecOps-Training//Filee.txt",
    "r",
)
for i in given_file:
    try:
        sum += int(i)
    except:
        print(f"{i} is not number")
    finally:
        print(f"sum is {sum}")

given_file.close()

"""Task #2 Տրված ֆայլում պարունակվում է տեքստ։ Իրականացնել ծրագիր, որը ֆայլի մեջ պարունակվող տեքստի բոլոր
    բառերի առաջին տառերը դարձնում է մեծատառ և ձևափոխված ամբողջ տեքստը պահպանում մեկ այլ ֆայլում։"""
