while True:
    print('음료목록 1.오렌지주스(100원), 2.커피(200원), 3.콜라(300원)')
    coin = int(input('동전을 넣으세요.'))
    drink = int(input('음료를 고르세요.\n'))

    if drink == 1:
        remain = coin - 100
        drink_str = "오렌지주스"
    elif drink == 2:
        remain = coin - 200
        drink_str = "커피"
    elif drink == 3:
        remain = coin - 300
        drink_str = "콜라"
    else:
        print('없는 메뉴입니다. 다시 입력해주세요.')
        continue

    if remain >= 0:
        print(f'{drink_str} 제공 중! 거스름돈: {remain}원')
    else:
        print('잔액이 부족합니다.')




