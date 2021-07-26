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
            for item in STORE:
                lis.append(item)
        if choice == 2:
            N = float(input("Yore price"))
            lis1 = [item for item in STORE if item.prise < N]
            for item in lis1:
                lis.append(item)

        def choice_1(S):
            for item in S:
                print(item)

        choice_1(lis)


if __name__ == '__main__':
    start_store()

