#輸入幾個蘋果 一個多少錢 進多少個蘋果 輸出現在有多少個 賣多少個蘋果、應收多少錢
while True:
    x = input()
    x = int(x)
    if x ==1:
        num=input()
        num=int(num)
        money=input()
        print(num,'個蘋果一個',money,'元')
    elif x == 2:
        get = input()
        get = int(get)
        print('進',get,'個蘋果')
        print('現在有',get+num,'個蘋果')
    elif x == 3:
        sell = input()
        sell = int(sell)
        print('今天賣',sell,'個蘋果要收',sell*money,'元')
    #( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)
    elif x == 4:
        item = input()
        item = int(item)
        print("今天有",item,"筆交易分別賣",sell,'個蘋果共收',item*sell*money,"元")
    elif x == 5:
        print('剩',get+num-sell,'個蘋果')
    elif x == 6:
        break
#設定：最初有幾個蘋果、一個多少錢(V)
#進貨：進多少個蘋果(V)
#出貨：賣多少個蘋果、應收多少錢(V)
#營業額統計：今天有幾筆交易、分別賣多少個蘋果、共收多少錢
#庫存統計：剩多少個蘋果(V)
#離開系統
