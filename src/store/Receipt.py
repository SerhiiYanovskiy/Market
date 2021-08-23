from Row import Row



class Receipt:

    def __init__(self, datetime, client):
        self.datetime = datetime
        self.client = client
        self.rows = []


    def __str__(self):
            return f'CHECK\n' \
                   f' date  {self.datetime}\n ' \
                   f'client  {self.client}\n' \
                   f'  {self.rows[0]}'


    def add_row(self, r: Row):
        self.rows.append(r)

    def check_article_in_receipt(self, article):

        current_row = [item for item in self.rows if item.product._article == article]
        if len(current_row) > 0:
            return True
        else:
            return False

    def increase_quantity(self, article, quantity):
        current_row = [item for item in self.rows if item.product._article == article][0]

        current_row.increase_row_quantity(quantity)




