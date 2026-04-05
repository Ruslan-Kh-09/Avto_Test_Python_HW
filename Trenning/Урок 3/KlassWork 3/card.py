class Card:
    number = '0000 1111 2222 3333'
    validate = '01/99'
    holder = 'unknown'

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.validate = date

    def pay(self, amount):
        print('с карты ', self.number, 'списали ', amount)
