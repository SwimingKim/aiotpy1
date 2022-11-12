class AiStore:

    def __init__(self, name, s_id, locate):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products = {'커피':10}
        self.prices = {'커피':1000}

    def set_product(self, product, count, price):
        if product in self.products.keys() :
            self.products[product] += count
            self.prices[product] = price
        else :
            self.products[product] = count
            self.prices[product] = price

    def buy_product(self, product, count, amount):
        if self.products[product] < count:
            print("재고가 부족합니다")
            return
        total_amount = self.prices[product] * count
        if amount < total_amount :
            print("금액이 부족합니다")
            return
        self.products[product] -= count
        changes = amount - total_amount
        print("잔돈은 {}입니다".format(changes))

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products(self):
        return self.products

    def get_prices(self):
        return self.prices

def create_store():
    s_name = input('스토어 이름 입력: ')
    s_id = input('스토어 아이디 입력: ')
    locate = input('스토어 위치 입력: ')
    store = AiStore(s_name, s_id, locate)
    print('{} 스토어가 생성 되었습니다.'.format(store.get_name()))
    return store

def show_list():
    for store in store_list:
        print('스토어 이름:{} 스토어 아이디:{} 스토어 위치:{}'
              .format(store.get_name(),
                      store.get_id(),
                      store.get_locate()
                      ))

def search_store(s_id):
    for store in store_list:
        if store.get_id() == s_id:
            return store

    print('스토어 아이디를 찾지 못했습니다.')
    return None

def show_store():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    if store is None:
        return

    print('{} 스토어 재고 현황: {}'
          .format(store.get_name(),
                  store.get_products()
                  ))
    print('{} 스토어 가격 현황: {}'
          .format(store.get_name(),
                  store.get_prices()
                  ))

def buy():
    s_id = input('스토어 아이디 입력: ')
    store = search_store(s_id)
    product = input('상품 입력:')
    if product not in store.get_products().keys():
        print("선택하신 상품이 없습니다")
        return
    count = input('구매 개수 입력: ')
    # 옵션 '총 가격은 {} 입니다.' 출력
    print("총 가격은 {} 입니다".format(store.get_prices()[product] * int(count)))
    price = input('가격 입력: ')
    store.buy_product(product, int(count), int(price))

def manager_product():

    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)

    product = input('상품 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')

    store.set_product(product, int(count), int(price))

def txt_to_store():
    file = open('stores.txt', 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    for item in data:
        obj = item.strip().split(" ")
        store = AiStore(obj[0], obj[1], "none")
        store_list.append(store)

import json
def store_to_json():
    list = []
    for store in store_list:
        dict = {}
        dict["name"] = store.get_name()
        dict["id"] = store.get_id()
        dict["locate"] = store.get_locate()
        dict["products"] = store.get_products()
        dict["prices"] = store.get_prices()
        list.append(dict)
    file = open('stores.json', 'w', encoding='utf-8')
    json.dump(list, file)
    file.close()

if __name__ == '__main__':
    store_list = []

    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - txt 파일로 스토어 생성')
    print('7 - json 파일로 스토어 정보 출력')

    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1':
            store = create_store()
            store_list.append(store)
        elif input1 == '2':
            show_list()
        elif input1 == '3':
            show_store()
        elif input1 == '4':
            buy()
        elif input1 == '5':
            manager_product()
        elif input1 == '6':
            txt_to_store()
        elif input1 == '7':
            store_to_json()
        else:
            print('존재하지 않는 명령어 입니다.')
