stack = [ i for i in range(6)]
popNow = False
c=0
while c!=len(stack)-1:
    if popNow:
        #poping the last index at zero and appending to last
        popIndex = stack.pop(0)
        print(f"the pop index is {popIndex}")
        stack.append(popIndex)
        print(f"the appending index value is {stack[-1]}")
        popNow=False
    else:
        index = stack[0]
        c+=1
        print(f"the index value is {index}")
        stack.pop(0)
        popNow = True