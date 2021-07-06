from const import STORE
from helpers import print_menu


def start_store():
    while True:
        print(print_menu())
        choice = int(input('Your choice'))
        if choice == 0:
            break
        if choice == 1:
            for item in STORE:
                print(item)
        if choice == 2:
            N = float(input("Enter price"))
            lis = [item for item in STORE if item[2] < N]
            print(lis)


if __name__ == '__main__':
    start_store()

