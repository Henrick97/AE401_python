score=[]
for i in range(1,6,1):
    x=input()
    x=int(x)
    score.append(x)
print(*score)
sum = 0
for i in range(0,5,1):
    sum=sum+score[i]
print(sum/5)
m=10
for i in range(0,5,1):
    if(m>score[i]):
        m = score[i]
print(m)
m = 0
for i in range(0,5,1):
    if(m<score[i]):
        m=score[i]
print(m)
