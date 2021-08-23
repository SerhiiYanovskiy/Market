class Product:
    def __init__(self, article, title, price):
        self._article = article
        self._title = title
        self._prise = price

    def __str__(self):
        return f' {self._article}  {self._title}  {self._prise}'

    @property
    def article(self):
        return self._article

    @property
    def prise(self):
        return self._prise

















