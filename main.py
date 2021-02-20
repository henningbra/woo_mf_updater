import pandas as pd


df = pd.read_excel('book.xlsx', index_col=None)
print(df)
dct = df.to_dict('records')
print(dct)

if __name__ == '__main__':
    pass