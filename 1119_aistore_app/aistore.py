import pandas as pd

s_df = pd.read_csv('./static/stores.csv')
s_df = s_df.set_index('s_id', drop=False)
p_df = pd.read_csv('./static/products.csv')
p_df = p_df.set_index('p_id', drop=False)
iv_df = pd.read_csv('./static/inventory.csv')

class AiStore:

    def __init__(self, name, s_id, locate, products_num, inventory):
        self.name = name
        self.s_id = s_id
        self.locate = locate
        self.products_num = products_num
        self.inventory = inventory

    def set_product(self, p_id, count, price):
        pass


    def is_product(self, p_id):
        pass
    def buy_product(self, p_id, count, amount):
        pass

    def get_name(self):
        return self.name

    def get_id(self):
        return self.s_id

    def get_locate(self):
        return self.locate

    def get_products_num(self):
        return self.products_num

    def get_inventory(self):
        return self.inventory
    def get_menu(self, p_df):
        # {'p_name': p_name, 'price': int(price), 'count': int(count), 'p_id':p_id} 이 여러개
        pass

    def get_price(self, p_id):
        pass

    def update_data(self, s_df, iv_df):
        pass

def create_store(s_id, s_name, locate):

    store = {'s_id': s_id, 'name': s_name,
             'locate': locate,
             'products_num': 0,}

    s_df.loc[s_id] = store
    print('{} 스토어가 생성 되었습니다.'.format(store['name']))


def show_list(s_id = None):
    if s_id is None:
        return s_df.values.tolist()
    else:
        return s_df[s_df["s_id"] == s_id].values.tolist()

def search_store(s_id):
    print(s_id)
    if s_id in s_df.index:
        store = s_df.loc[s_id]
        inventory = iv_df[iv_df['s_id'] == s_id]
        return AiStore(store['name'],
                       store['s_id'],
                       store['locate'],
                       store['products_num'],
                       inventory)
    else:
        print('스토어를 찾지 못했습니다.')
        return None

def get_products():
    return p_df.to_dict('records')

def get_menu(s_id):
    pass
    return

def update_product(p_id, price, count, s_id):
    pass

def add_product(p_id, price, count, s_id ):
    pass

def update(s_id):
    pass




def bucket(s_id, p_id, count):
    store = search_store(s_id)
    if store is None:
        return