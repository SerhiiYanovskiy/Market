from const import STORE
from helpers import print_menu


def start_store():
    while True:
        print_menu()
        choice = int(input('Your choice'))
        if choice == 0:
            break
        lis = []
        if choice == 1:
            lis.append(STORE)
        if choice == 2:
            N = float(input("Yore price"))
            lis1 = [item for item in STORE if item.prise < N]
            lis.append(lis1)

        def print_product_list(S):
            for item in S:
                for i in item:
                    print(i)

        print_product_list(lis)


if __name__ == '__main__':
    start_store()

