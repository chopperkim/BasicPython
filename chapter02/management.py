
food_list = []

# 메뉴
while True:
    print("-"*52)
    print('1. 목록 출력 | 2. 추가 | 3. 변경 | 4. 삭제 | 5. 종료')
    print("-"*52)
    menu = int(input('관리 메뉴를 선택하세요.> '))
    if menu == 1:
        print(food_list)
    elif menu == 2:
        food = input('추가할 식재료를 입력하시오: ')
        food_list.append(food)
    elif menu == 3:
        exchanging_food = input('교환할 식재료를 입력하시오: ')
        if exchanging_food in food_list:
            idx = food_list.index(exchanging_food)
            new_food = input('새로운 식재료를 입력하시오: ')
            food_list[idx] = new_food
        else:
            print('식재료 재고 없음')
    elif menu == 4:
        deleting_food = input('삭제할 식재료를 입력하시오: ')
        if deleting_food in food_list:
            food_list.remove(deleting_food)
        else:
            print('식재료 재고 없음')
    elif menu == 5:
        print('프로그램을 종료합니다.')
        break
    else:
        print('선택하신 메뉴는 존재하지 않습니다.')

