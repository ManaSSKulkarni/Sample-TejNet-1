"""SAMPLE2"""

n1 = int(input("Enter a number="))

for row in range(1, n1 + 1):
    for column in range(1, row + 1):
        print(column, end=" ")
    print(" ")
k = n1
for i in range(0, n1 + 1):
    for j in range(k - i, 0, -1):
        print(j, end=" ")
    print()

str1 = input("Enter a Sentence=")
str2 = input("Enter another sentence=")


def concatenation(str11, str12):
    """Concatenation"""
    return str11 + str12


print("Together=", concatenation(str1, str2))
print("A/a in s1=", str1.lower().count("a"))
print("A/a in s2=", str2.lower().count("a"))


arr1 = []
n2 = int(input("Enter Array length="))
for i in range(0, n2):
    arr1.append(int(input(f"Enter {i}th element=")))

print("Minimum element=", min(arr1))
print("Maximum element=", max(arr1))

print("Reversed :-")


def reverse_array(arr):
    """Reversing"""
    return arr.reverse()


print(reverse_array(arr1))

print("Sorted:-")
arr1.sort()

for i in range(0, len(arr1)):
    print(arr1[i], " ")


def add(a, b):
    """Addition"""
    return a + b
