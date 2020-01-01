def solution(s):

    ans_list=[]
    count_list=[]
    tmp_list=[]
    re=[]
    min=len(s)
    for i in range(len(s)):
        for j in range(len(s)):
            if j >= i:
                tmp_list.append(s[i:j+1])



    for i in range(len(tmp_list)):
        tmp_list[i].replace('',"")
    print("cut list result",tmp_list)

    for i in range(len(tmp_list)):
        x=tmp_list[i]
        count_list.append(str(s.count(x)))
    print("count list result",count_list)

    for i in range(len(tmp_list)):
        ans_list.append(count_list[i] + tmp_list[i])
    print("anwser list result",ans_list)


    for i in range(len(tmp_list)):
        re.append(s.replace(ans_list[i][1:],""))
    print("anwser list result",ans_list)
    print("re list result",re)


    for i in range(len(s)):
        re[i]=(ans_list[i] + re[i])

    print("re list 2 result",re)
    for i in range(len(s)):
        if min > len(re[i]):
            min = len(re[i])
    if min < len(s):
        return min
    else:
        return len(s)



a="abcabcabcabcdededededede"


print(solution(a))
#print(solution(a))
