# similar to longest repeating char rep

def getMinFlips(st):
    p2=0
    count=0
    st=list(st)
    for p1 in range(1,len(st)):
        if st[p1]==st[p2]:
            if p1-p2 == 1:
                p2+=1
        else:
            p2+=1

    while(p1-p2 != 0):
        st[p2]=st[p1]
        p2+=1
        count+=1

    if (p1-p2)%2 == 0:
        return count
    else:
         return count+1