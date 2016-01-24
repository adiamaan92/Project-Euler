def amicable(n):
    sum = 0
    A=[[0,0]]
    for i in range(1,n,1):
        amicable1 = 0
        for k in range(1,i//2+1,1):
            if i%k == 0:
                amicable1 += k
        A.insert([i,0],i)
        A.insert([i,1],amicable1)
    print(A)
amicable(10000)

    # for j in range(0,len(A)):
    #     temp1 = A[[j,1]]
    #     if A[[temp1,1]] == j:
    #         print(A[j])
            
            
            