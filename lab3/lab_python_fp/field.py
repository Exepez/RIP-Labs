goods = [
    {'title': 'Ковер', 'price': 3000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стул', 'price': None, 'color': 'green'},
    {'title': None, 'price': None, 'color': 'green'},
]


def field(items,*args):
    assert len(args) > 0, 'Не переданы аргументы полей словаря'
    if len(args) == 1:
        for i in range(len(items)):
            if (items[i].get(args[0])!=None):
                yield items[i].get(args[0])
    else:
        for i in range(len(items)):
            d={}
            for j in range(len(args)):
                if (items[i].get(args[j])!=None):
                    d.update({args[j]: items[i].get(args[j])})
            if (d!={}):
                yield d

def main():
    f=field(goods, 'title')
    for i in f:
        print(i, end=';  ')
    print('\n',end='')
    f=field(goods, 'title', 'price')
    for i in f:
        print(i, end=';  ')

if __name__ == "__main__":
   main()