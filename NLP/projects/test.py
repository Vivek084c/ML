def solve(x):
    for i in range(x):
        # print x-i spaces
        for j in range(x-i):
            print(" ",end="")
        #print a values
        ans = [j for j in range(i+1,2)]
        for z in ans:
            print(z,end=" ")
        for z in reversed(ans):
            print(z,end=" ")
        print("")
            


        # #print x-i spaces
        # for j in range(x-i):
        #     print(" ",end="")
solve(3)


