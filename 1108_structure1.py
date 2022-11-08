"""
1번 문제
"""

users = {123:['최원칠','관악구'],
         124:['이서혁','구로구'],
         125:['새싹','용산구']}

products = {'a':'노트북',
            'b':'자전거',
            'c':'샴푸',
            'd':'셔츠',
            'e':'초코렛'}

orders = [{'user_id':123, 'products':['a','c']},
         {'user_id':125, 'products':['e']},
         {'user_id':124, 'products':['b','d','e']}]

delivery = []

for order in orders:
    user = users[order["user_id"]]
    for product in order["products"] :
        delivery.append({"name": user[0], "product": products[product], "locate": user[1]})

print(delivery)

"""
2번 문제
"""

users = {123:['최원칠','관악구'],
         124:['이서혁','구로구'],
         125:['새싹','용산구'],
         126:['aiot','용산구']}

products = {'a':{'name':'노트북', 'count':10},
            'b':{'name':'자전거', 'count':10},
            'c':{'name':'샴푸', 'count':10},
            'd':{'name':'셔츠', 'count':0},
            'e':{'name':'초코렛', 'count':10}}

orders = [{'user_id':123, 'products':['a','c']},
          {'user_id':125, 'products':['e']},
          {'user_id':124, 'products':['b','d','e']},
          {'user_id':126, 'products':['a']}]

delivery = {}

for order in orders:
    user = users[order["user_id"]]
    if user[1] not in delivery.keys() :
        delivery[user[1]] = []
    for product in order["products"]:
        item = products[product]
        p_count = item["count"]
        if p_count > 0:
            delivery[user[1]].append((user[0], item["name"]))
            item["count"] = p_count - 1

print(delivery)