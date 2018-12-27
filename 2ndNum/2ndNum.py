# Find 2nd high number

a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

num=[a,b,c]
num.sort()

print(num[1])