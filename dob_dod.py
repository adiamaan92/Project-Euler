A = [('A',1992,2025),('B',1995,2020),('C',2000,2050),('D',1991,2050)]
T = A[0][1]
S = A[0][2]
temp = 0
final_cnt = 0
for i in A:
    if i[1] < T:
        T = i[1]
    if i[2] > S:
        S = i[2]
R = [x for x in range(T,S+1)]
  
for x in R:
    cnt = 0
    prev_cnt = 0 
    for i in A:
        if x >= i[1]:
            cnt+=1
        if i[2] <= x:
            cnt-=1
    print(x,cnt)
    # if cnt < prev_cnt:
    #     final_cnt == prev_cnt
    # elif cnt >= prev_cnt:
    #     final_cnt == cnt
    # prev_cnt == cnt
    # print(final_cnt)

    