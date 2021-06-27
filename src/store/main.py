lis = [["A0001", "тетрадь", 20.50], ["A0002", "ручка", 21.50], ["A0003", "дневник", 30.50],
       ["A0004", "портфель", 40.50], ["A0005", "ленейка", 15.20], ["A0006", "ластик", 18.10],
       ["A0007", "коректор", 12.50], ["A0008", "пенал", 8.50], ["A0009", "обложка", 1.50],
       ["A0010", "циркуль", 30.40]]

def start_store():

    while True:
        print('0. Exit')
        print('1. List of lis')

        choice = int(input('Your choice'))

        if choice == 0:
            break
        if choice == 1:
            for item in lis:
                print(item)


if __name__ == '__main__':
    start_store()