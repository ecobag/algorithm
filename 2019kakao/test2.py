
def solution(words, queries):

    count = 0
    result=[]
    for i in range(len(queries)):
        #fro?? 호출
        for j in range(len(words)):
            #frodo 호출
            count=0
            if len(queries[i]) == len(words[j]): #단어길이비교
                for x in range(len(queries[i])): # 문자열비교
                    if queries[i][x] == words[j][x] or queries[i][x] == '?': #문자 같으면 카운트
                        count = count + 1
                        print(queries[i][x], words[j][x])
                        print(count)
            if count == len(queries[i]): #카운트와 문자길이가 같으면 결과값 추가
                result[i]=result[i]+1

    return result


w=["frodo", "front", "frost", "frozen", "frame", "kakao"]
q=["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(w,q))
