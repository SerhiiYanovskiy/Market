from const import STORE
from helpers import print_menu, receipt_menu, find_product_by_article, print_product_list
from Singletone import Store
from Receipt import Receipt
import datetime
from Row import Row
from Product import Product



def start_store():
    my_store = Store()
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
        if choice == 3:
            name = input("Yore name")
            current_receipt = Receipt(datetime.datetime.now(), name)
            while True:
                try:
                    receipt_menu()
                    choice = int(input(''))
                    if choice == 0:
                        break
                    if choice == 1:

                        article = input("1. Write article")
                        quantity = input("2. Write quantity")
                        if current_receipt.check_article_in_receipt(article) == True:
                            current_receipt.increase_quantity(find_product_by_article(article), quantity)

                        else:
                            current_product = find_product_by_article(article)
                            current_row = Row(current_product, quantity)
                            current_receipt.add_row(current_row)
                except IndexError:
                    error_menu()
                    pass
                my_store.add_receipt(current_receipt)
        if choice == 4:
            article = input('write artical')
            titele = input('wrire titele')
            price = input('write prise')
            import csv
            with open("prod.csv", "a", newline='') as w_file:
                file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                file_writer.writerow([article, titele, price])




if __name__ == '__main__':
    start_store()

