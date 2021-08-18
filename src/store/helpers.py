from const import STORE


def find_product_by_article(article):
    corent_product = [item for item in STORE if item.article == article][0]
    return corent_product

















def receipt_menu():
    print('0. Exit')
    print('1. Write article and quantity')

def decor(func):
    def menu():
        print("================")
        func()
        print("+++++++++++++++++")
    return menu


@decor
def print_menu():
    print('0. Exit')
    print('1. List of STORE')
    print('2. Show products no more expensive than N')
    print('3. Yore receipt')


def print_product_list(S):
    for idx, item in enumerate(S):
        print(f'{idx}) {item}')










