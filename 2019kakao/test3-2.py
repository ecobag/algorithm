def solution(key, lock):
    n=len(key)
    rot_key=[key]

    for i in range(3):
        rot_key.append(turn_90(key,i+1))

    up_keys=[]
    down_keys=[]
    left_keys=[]
    right_keys=[]

    for i in range(4):
        for j in range(n-1):
            up_keys.append(up_key(rot_key[i],j+1))

    for i in range(4):
        for j in range(n-1):
            down_keys.append(down_key(rot_key[i],j+1))

    for i in range(4):
        for j in range(n-1):
            left_keys.append(left_key(rot_key[i],j+1))

    for i in range(4):
        for j in range(n-1):
            right_keys.append(right_key(rot_key[i],j+1))


    left_up_keys=[]
    left_down_keys=[]
    up_left_keys=[]
    down_left_keys=[]


    for i in range(n):
        for j in range(n-1):
            left_up_keys.append(up_key(left_keys[i],j+1))
            left_down_keys.append(down_key(left_keys[i],j+1))

    for i in range(n):
        for j in range(n-1):
            up_left_keys.append(left_key(up_keys[i],j+1))
            down_left_keys.append(left_key(down_keys[i],j+1))


    right_up_keys=[]
    right_down_keys=[]
    up_right_keys=[]
    down_right_keys=[]



    for i in range(n):
        for j in range(n-1):
            right_up_keys.append(up_key(right_keys[i],j+1))
            right_down_keys.append(down_key(right_keys[i],j+1))

    for i in range(n):
        for j in range(n-1):
            up_right_keys.append(right_key(up_keys[i],j+1))
            down_right_keys.append(right_key(down_keys[i],j+1))

    god_keys=rot_key + left_up_keys + left_down_keys + up_left_keys + down_left_keys + right_up_keys + right_down_keys + up_right_keys + down_right_keys

'''처음작성
    # 회전된 열쇠 1~(n-1)번 왼쪽이동 한 열쇠
    for i in range(4):
        for j in range(n-1):
            master_keys11.append(left_key(rot_key[i],j+1))

    for i in range(4):
        for j in range(n-1):
            test.append(down_key(rot_key[i],j+1))

    for i in range(n):
        for j in range(n-1):
            master_keys1.append(up_key(master_keys11[i],j+1))
            master_keys1.append(down_key(master_keys11[i],j+1))

    for i in range(4):
        for j in range(n-1):
            master_keys22.append(right_key(rot_key[i],j+1))

    for i in range(n):
        for j in range(n-1):
            master_keys2.append(up_key(master_keys22[i],j+1))
            master_keys2.append(down_key(master_keys22[i],j+1))

    god_keys= master_keys1+master_keys2+test
'''

    #키 목록과 잠금장치 비교
    mat_num=0
    for i in range(len(god_keys)): #n번째 키선택
        for j in range(len(god_keys[i])):
            for k in range(len(god_keys[i][j])):
                if god_keys[i][j][k] != lock[j][k]:
                    #print("성공",i,j,k,"key : ",god_keys[i][j][k],"lock : ",lock[j][k])
                    mat_num = mat_num + 1
                #else:
                    #print("실패",i,j,k,"key : ",god_keys[i][j][k],"lock : ",lock[j][k])
        #print()
        if mat_num == n*n:
            return True
        mat_num = 0


    return False

def turn_90(key,count):
    n=len(key) # 3

    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n): # i = 0, 1, 2
        for j in range(n): #j = 0, 1, 2
            result[i][j]=key[n-j-1][i]
    count = count -1

    if count == 0:
        return result
    else:
        return turn_90(result,count)


def up_key(key, count):
    n=len(key)
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n): # i = 0, 1, 2
        for j in range(n): #j = 0, 1, 2
            if i == n-1:
                result[i][j] = 0
            else:
                result[i][j]=key[i+1][j]
    count = count -1

    if count == 0:
        return result
    else:
        return up_key(result,count)


def down_key(key,count):
    n=len(key)
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n): # i = 0, 1, 2
        for j in range(n): #j = 0, 1, 2
            if i == 0:
                result[i][j] = 0
            else:
                result[i][j]=key[i-1][j]
    count = count -1

    if count == 0:
        return result
    else:
        return down_key(result,count)

def right_key(key,count):
    n=len(key)
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n): # i = 0, 1, 2
        for j in range(n): #j = 0, 1, 2
            if j == 0:
                result[i][j] = 0
            else:
                result[i][j]=key[i][j-1]
    count = count -1

    if count == 0:
        return result
    else:
        return right_key(result,count)

def left_key(key,count):
    n=len(key)
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n): # i = 0, 1, 2
        for j in range(n): #j = 0, 1, 2
            if j == n-1:
                result[i][j] = 0
            else:
                result[i][j]=key[i][j+1]
    count = count -1

    if count == 0:
        return result
    else:
        return left_key(result,count)

key=[[1,0,0,0,1],
     [0,0,0,1,0],
     [0,1,0,0,1],
     [1,0,1,0,0],
     [1,0,0,0,1]]
key2=[[1,1,0,0,1],
      [0,0,1,0,0],
      [0,1,0,0,0],
      [0,0,0,1,0],
      [1,0,1,0,1]]
lock=[[1,1,1,1,1],
      [0,0,1,1,0],
      [1,1,0,1,1],
      [1,0,1,1,1],
      [1,1,1,0,1]]

print(solution(key2,lock))
