from Row import Row



class Receipt:

    def __init__(self, datetime, client):
        self.datetime = datetime
        self.client = client
        self.rows = []

    def add_row(self, r: Row):
        self.rows.append(r)

    def check_article_in_receipt(self, article):

        current_row = [item for item in self.rows if item.product.article == article]
        if len(current_row) > 0:
            return True
        else:
            return False

    def increase_quantity(self, article, quantity):
        current_row = [item for item in self.rows if item.current_product.article == article][0]

        current_row.increase_row_quantity(quantity)




