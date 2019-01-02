# Calculate binary(Find secret map)
def makeBinary(x):
        result = []
        while(x>1):
                r = int(x % 2)
                x = x / 2
                result.append(r)
                
                # exception
                if x<2 and r==0:
                    result.append(1)
        return(result)

# Find Secretmap
def findMap(m1,m2,n):
        result = []
        for i in range(n):
                if ((m1[i] | m2[i]) == 1):
                        result[i] = '#'
                else:
                        result[i] = ' '
        return (result)

# Input map size
n = input("지도의 크기를 입력하세요 : ")
n = int(n)

# Initialize map
map1 = [0 for i in range(n)]
map2 = [0 for i in range(n)]
secret_map = [0 for in range(n)]

# Input each row value
for i in range(n):
        k = input("Map1의 {}번 데이터를 입력하세요 : ".format(i+1))
        map1.append(i)


print("Map1 의 데이터입력을 마쳤습니다")
print()

for i in range(n):
        k = input("Map2의 {}번 데이터를 입력하세요 : ".format(i+1))
        map2.append(i)


print("Map2 의 데이터입력을 마쳤습니다")
print()


# Do it
map1_b = makeBinary(map1).reverse
map2_b = makeBinary(map2).reverse
secret_map = findMap(map1_b,map2_b,n)

print(secret_map)



'''
Sequence

Input n
Input map1,2

Compare map1,2(bit operation) and make secretmap
Convert data in secretmap (decimal -> binary)
Convert data (binary-> '#', ' ')

Print result

'''