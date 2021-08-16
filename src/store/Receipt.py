from Row import Row



class Receipt:

    def __init__(self, datetime, client):
        self.datetime = datetime
        self.client = client
        self.rows = []



    def add_row(self, r: Row):
        self.rows.append(r)


    def check_article_in_receipt(self, article):

        corent.row = [item for item in self.rows if item.product.article == article][0]
        return True

    def increase_quantity(self, article):
        corent.row = [item for item in self.rows if item.product.article == article][0]
        corent.row.increase_quantity(q)




