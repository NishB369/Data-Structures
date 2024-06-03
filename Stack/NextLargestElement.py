l=[5,2,3,4]
s=[]
ans=[]
l.reverse()
# print('ans: ',ans)
# print('s: ',s)
for i in l:
    if s==[]:
      ans.append(-1)
    elif (s!=[] and s[-1]>i):
        ans.append(s[-1])
    elif (s!=[] and s[-1]<=i):
        while (s!=[] and s[-1]<=i):
            s.pop()
        if s==[]:
            ans.append(-1)
        else:
            ans.append(s[-1])
    s.append(i)
    # print('ans: ',ans)
    # print('s: ',s)
print(ans[::-1])