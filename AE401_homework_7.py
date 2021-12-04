score=[['a',1],['b',3],['c',0]]
m = 0
m_index = 0 
for i in range(0,3,1):
    if(m<score[i][1]):
        m_index = i
        m = score[i][1]
print(score[m_index][0],m)
m = 123467
m_index = 0 
for i in range(0,3,1):
    if(m>score[i][1]):
        m_index = i
        m = score[i][1]
print(score[m_index][0],m)
