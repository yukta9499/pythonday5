# print tables of all odd numbers from 1 to 10 
for n in range(1,11,2):
    print("Table of ", n)

    for i in range(1,11):
        print(n,"*",i,"=",n*i)

# ------------------------------------------------------>

# create a heterogenous list of numbers and names. SPlit the list from highhest number

a = ['yukta', 'sujal', 89, 68, 'sonal', 67, 79]

m = max (i for i in a
        if type(i) == int)

b = a[:a.index(m)]
c = a[a.index(m):]

print(b)
print(c)


# ------------------------------------------------------>

# insert two numbers at the 3rd and 4th index of list and append a name in the list
b = ['yukta', 'sujal', 89, 68, 'sonal', 67, 79]
print(b)
b.insert(3,90)
print(b)
b.insert(4,70)
print(b)
b.append('diksha')
print(b)

# ------------------------------------------------------>

# accept the name and check its palindrome
name = input("Enter a name :")
rev = name[::-1]
if rev==name:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


#------------------------------------------------------>


# print sum of digits
n = int(input("Enter a number: "))
s = 0

while n > 0:
    r = n % 10
    s = s + r
    n = n // 10

print("Sum of digits:", s)