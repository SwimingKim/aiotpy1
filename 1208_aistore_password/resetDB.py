from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('sqlite:///tmp/aistore.db', convert_unicode=True)

# stores.csv 데이터프레임으로 불러온 후 sql stores 테이블로 저장
# products.csv 데이터프레임으로 불러온 후 sql products 테이블로 저장
# inventory.csv 데이터프레임으로 불러온 후 sql inventory 테이블로 저장

s_df = pd.read_csv('./static/stores.csv')
s_df.to_sql('stores', con=engine, if_exists='replace', index= False)
p_df = pd.read_csv('./static/products.csv')
p_df.to_sql('products', con=engine, if_exists='replace', index=False)
iv_df = pd.read_csv('./static/inventory.csv')
iv_df.to_sql('inventory', con=engine, if_exists='replace', index=False)

