from const import STORE




def find_product_by_article(article):
    corent_product = [item for item in STORE if item._article == article][0]
    return corent_product


def error_menu():
    print("Article not found")


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
    print('4. Add product')
    print('5. Print check')


def print_product_list(S):
    for idx, item in enumerate(S):
        print(f'{idx}) {item}')





def print_check(i):
    print(i)





