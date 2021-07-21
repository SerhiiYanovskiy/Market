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
    print('2 Show products no more expensive than N')





