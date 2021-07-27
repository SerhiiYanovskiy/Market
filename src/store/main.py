from const import STORE
from helpers import print_menu
from helpers import print_product_list


def start_store():
    while True:
        print_menu()
        choice = int(input('Your choice'))
        if choice == 0:
            break

        if choice == 1:
            print_product_list(STORE)
        if choice == 2:
            N = float(input("Yore price"))
            print_product_list([item for item in STORE if item.prise < N])


if __name__ == '__main__':
    start_store()

