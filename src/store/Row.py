from Product import Product


class Row:
    def __init__(self, product: Product, n):
        self.product = product
        self.n = n

    def __str__(self):
        return f'{self.product} * {self.n} = {self.product.prise} * {self.n}'

    def increase_row_quantity(self,  q):
        self.n += q
