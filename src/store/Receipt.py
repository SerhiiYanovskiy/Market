from Row import Row


class Receipt:

    def __init__(self, client):
        self.datatime = None
        self.client = client
        self.rows = []

    def add_row(self, r: Row):
        self.rows.append(r)