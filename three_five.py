"""
A program that prints thu numbers from 1 to 100

1. If number multiple of 3: Three
1. If number multiple of 5: Five
1. If number multiple of booth 3 and 5: ThreeFive
1. If any another result print the real number
"""


def multiple():
    for i in pos:
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)


pos = range(1, 101)

multiple()
