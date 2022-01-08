a={}
while True:
    flag=int(input('繼續輸入1 離開輸入0 列出請輸入2 查詢單字輸入3 測驗請按4'))
    if flag==0:
        break
    elif flag==1:
        english=input('請輸入英文單字')
        chinese=input('請輸入中文解是')
        a[english]=chinese
        print(a)
    elif flag==2:
        print(a)
    elif flag==3:
        enlgish = input('請輸入英文單字')
        if english in a:
            print(a[english])
        else:
            print('此單字未包含在內')
    elif flag==4:
        print('題目共有',len(a),'題,一題一分')
        sum = 0;
        for k,v in a.items():
            print('題目為',k)
            ans = input('在此輸入你的答案')
        if v == ans :
            print('答對了,加一分')
            sum+=1
        else:
            print('答錯了,扣一分')
        print('你獲得分數為',sum,'分','總分為',len(a),'分')
