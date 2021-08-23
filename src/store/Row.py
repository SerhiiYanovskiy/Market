from Product import Product


class Row:
    def __init__(self, product: Product, n):
        self.product = product
        self.n = n
        self.prise1 = self.product.prise * float(n)

    def __str__(self):
        return f'{self.product} * {self.n} = {self.prise1}'

    def increase_row_quantity(self,  q):
        self.n += q
