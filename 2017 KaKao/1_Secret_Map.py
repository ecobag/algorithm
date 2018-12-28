
n = input('지도의 크기를 입력하세요 : ')
n = int(n)

map1 = [[0 for i in range(n)] for j in range(n)]
map2 = [[0 for i in range(n)] for j in range(n)]
secret_map = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        map1[i][j] = input("지도1의 데이터를 입력하세요 : ")
        map1[i][j] = int(map1[i][j])

print("지도 1의 데이터 입력이 끝났습니다.")
print()

for x in range(n):
    for y in range(n):
        map2[x][y] = input("지도2의 데이터를 입력하세요 : ")
        map2[i][j] = int(map2[i][j])

print('MAP1')
for i in range(n):
    for j in range(n):
        print(map1[i][j], end=' ')
    print()

print()

print('MAP2')
for i in range(n):
    for j in range(n):
        print(map2[i][j], end=' ')
    print()



print("Secret Map")
for i in range(n):
    for j in range(n):
        secret_map[i][j] = map1[i][j] | map2[i][j]
        secret_map[i][j] = int(secret_map[i][j])
    



print("Secret Map")
for i in range(n):
    for j in range(n):
        print(secret_map[i][j], end=' ')
    print()