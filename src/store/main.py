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


if __name__ == '__main__':
    start_store()

