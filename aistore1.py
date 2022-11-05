class AiStore:

    def __init__(self, s_name, s_id, locate):
        self.s_name = s_name
        self.s_id = s_id
        self.locate = locate
        self.count = 0
        self.price = 0

    def set_product(self, count, price):
        self.count = count
        self.price = price

    def buy_item(self, count, paid_money):
        if self.count < count :
            print('재고가 부족합니다')
            return
        total_price = count * self.price
        if paid_money < total_price :
            print('금액이 부족합니다')
            return
        self.count -= count
        changes = paid_money - total_price
        print('잔돈은 %i입니다' % changes)

    def get_name(self):
        return self.s_name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_count(self):
        return self.count

    def get_price(self):
        return self.price

if __name__ == '__main__':

    s_name = input('스토어 지점이름 입력: ')
    s_id = input('스토어 지점번호 입력: ')
    locate = input('스토어 위치 입력: ')
    store = AiStore(s_name, s_id, locate)
    print(store.get_name() + ' 스토어가 생성 되었습니다.')

    for i in range(10):

        print('스토어 조회는 1번, 구매는 2번, 상품 관리는 3번, 종료는 4번 을 눌러주세요')
        num = input()
        if num =='1':
            print("이름: %s / 번호 : %s / 위치 : %s / 재고 : %i / 가격 : %i" % (store.get_name(), store.get_id(), store.get_locate(), store.get_count(), store.get_price()))

        elif num == '2':
            count = int(input('구매할 상품 개수 입력: '))
            need_price = store.price * count
            amount = int(input(str(need_price) + ' 이상의 금액을 입력해 주세요: '))
            store.buy_item(count, amount)

        elif num == '3':
            count = int(input('상품 재고 입력: '))
            price = int(input('상품 가격 입력: '))
            store.set_product(count, price)

        elif num == '4':
            print('종료합니다')
            break
        else:
            print('잘못된 입력입니다')
