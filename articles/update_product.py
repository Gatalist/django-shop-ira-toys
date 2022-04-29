# from products.models import Product
# from articles.models import UpdateStatusView
import pandas as pd


# def split_elem(elem):
#     elem_str = str(elem)
#     elem_split = elem_str.split('.')
#     return elem_split[0]

# def parseTable(dataset):
# 	for index, row in dataset.iterrows():
# 		yield row


# files = pd.read_excel('21.21.21.xlsx', sheet_name = 'Страница 0')

# all_rows = parseTable(files)

# num = 2
# for elem in all_rows:
#     articl = split_elem(elem[5])
#     count = split_elem(elem[7])
#     print(num, articl, count)
#     num += 1



def parser(files):
    excel_data = pd.read_excel(files)
    data = pd.DataFrame(excel_data)
    datdset = {}
    
    for rowws, index in data.iterrows():
        n = 0
        key = None
        val = None
        for i in index:
            print(i)
            if n == 5:
                if float(i):
                    
                # key = i
                    print(str(i))
            if n == 7:
                if float(i):
                    print(str(i))

            n += 1
                
parser('21.21.21.xlsx')