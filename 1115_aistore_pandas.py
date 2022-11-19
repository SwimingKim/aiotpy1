import pandas as pd

class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products_num = products_num
        self.inventory = inventory

    def set_product(self, p_id, count, price):
        # if in 을 사용하기위해선 시리즈를 배열로 바꿔야할것 문서 참고
        # try 문사용 가능
        # 쿼리후 개수로 파악 가능
        if p_id in self.inventory["p_id"].values:
            df = self.inventory.copy()
            df.loc[df["p_id"] == p_id, "count"] += count
            df.loc[df["p_id"] == p_id, "price"] = price
            self.inventory = df
        else:
            self.products_num += 1
            self.inventory = pd.concat([self.inventory, pd.DataFrame([{
                "p_id": p_id,
                "count": count,
                "price": price,
                "s_id": self.s_id
            }])], ignore_index=True)

    def buy_product(self, p_id, count, amount):
        if not p_id in self.inventory["p_id"].values:
            print("상품이 존재하지 않습니다")
            return
        product = self.inventory[self.inventory["p_id"] == p_id].squeeze()
        if count > product["count"]:
            print("재고가 부족합니다")
            return
        total_price = product["price"] * count
        if total_price > amount:
            print("금액이 부족합니다")
            return
        changes = amount - total_price
        print("잔돈은 {}입니다".format(changes))
        df = self.inventory.copy()
        df.loc[df["p_id"] == p_id, "count"] -= count
        self.inventory = df

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num

    def show_products(self, p_df):
        # print(p_df)
        for index, item in self.inventory.iterrows():
            print("상품명:{} -  가격:{} (재고{}) id:{}".format(p_df.loc[item["p_id"]]["product"], item["price"], item["count"], item["p_id"]))

    def get_price(self, p_id):
        product =  self.inventory[self.inventory['p_id'] == p_id]
        if len(product) == 0:
            return None

        return product['price'].iloc[0]

    def update_data(self, s_df, iv_df):
        s_df.loc[s_df["s_id"] == self.s_id, "products_num"] = self.products_num
        for index, item in self.inventory.iterrows():
            p_id = item["p_id"]
            if iv_df[(iv_df["s_id"] == self.s_id) & (iv_df["p_id"] == p_id)].empty:
                iv_df.loc[len(iv_df)] = item
            else:
                iv_df[(iv_df["s_id"] == self.s_id) & (iv_df["p_id"] == p_id)] = item

def create_store():
    s_name = input('스토어 이름 입력: ')
    s_id = input('스토어 번호 입력: ')
    locate = input('스토어 위치 입력: ')

    if s_id in s_df["s_id"].values:
        return

    s_df.loc[len(s_df)] = {
        "s_id": s_id,
        "name": s_name,
        "locate": locate,
        "products_num": 0
    }
    store = s_df[s_df["s_id"] == s_id].squeeze()
    print('{} 스토어가 생성 되었습니다.'.format(store['name']))


def show_list():
    for index, store in s_df.iterrows():
        print("스토어이름:{} 스토어 아이디:{} 스토어 위치:{} 등록상품:{}".format(store["name"], store["s_id"], store["locate"], store["products_num"]))

def search_store(s_id):
    if s_id in s_df["s_id"].values:
        data = s_df[s_df["s_id"] == s_id].squeeze()
        inventory = iv_df[iv_df["s_id"] == s_id]
        store = AiStore(data["name"], data["s_id"], data["locate"], data["products_num"], inventory)
        return store
    return None

def show_store():
    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)
    if store == None:
        return
    print("스토어이름:{} 스토어 아이디:{} 스토어 위치:{} 등록상품:{}".format(store.get_name(), store.get_id(), store.get_locate(), store.get_products_num()))

def buy():
    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)
    if store == None:
        return
    store.show_products(p_df)

    p_id = input('상품 아이디 입력:')
    count = input('구매 개수 입력: ')
    count = int(count)
    total_price = count * store.get_price(p_id)
    print("필요한 금액은 {}입니다".format(total_price))
    price = input('가격 입력: ')
    store.buy_product(p_id, count, int(price))
    store.update_data(s_df, iv_df)

def manager_product():
    s_id = input('스토어 번호 입력: ')
    store = search_store(s_id)
    if store == None:
        return

    print("등록 가능 상품 {}".format(p_df))
    p_id = input('상품 아이디 입력: ')
    count = input('재고 개수 입력: ')
    price = input('상품 가격 입력: ')
    store.set_product(p_id, int(count), int(price))
    store.update_data(s_df, iv_df)

def save_to_csv():
    s_df.to_csv("stores.csv", encoding="utf-8", index=False)
    iv_df.to_csv("inventory.csv", encoding="utf-8", index=False)

import json
def products_counts():
    pc_df = pd.merge(p_df, iv_df, how="left", on="p_id")
    pc_df = pc_df[["product", "count"]].groupby(by="product").sum()
    print(pc_df)

if __name__ == '__main__':

    s_df = pd.read_csv('./stores.csv')
    s_df.set_index("s_id", inplace=False)
    print(s_df)
    p_df = pd.read_csv('./products.csv')
    p_df.set_index("p_id", inplace=True)
    print(p_df)
    iv_df = pd.read_csv('./inventory.csv')
    print(iv_df)

    print('1 - 스토어 생성')
    print('2 - 스토어 리스트 출력')
    print('3 - 스토어 정보 출력')
    print('4 - 상품 구매')
    print('5 - 상품 관리')
    print('6 - csv 파일로 스토어, 재고현황 파일 출력')
    print('7 - 상품명별 전체 재고 개수 출력')

    while True:
        print('--'*30)
        input1 = input('옵션을 입력해 주세요: ')
        if input1 == '1':
            create_store()
        elif input1 == '2':
            show_list()
        elif input1 == '3':
            show_store()
        elif input1 == '4':
            buy()
        elif input1 == '5':
            manager_product()
        elif input1 == '6':
            save_to_csv()
        elif input1 == '7':
            products_counts()
        else:
            print('존재하지 않는 명령어 입니다.')