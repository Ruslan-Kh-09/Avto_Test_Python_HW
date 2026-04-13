from user import User
from card import Card

user_Alex = User('Alex')


user_Alex.sayName()
user_Alex.setAge(22)
user_Alex.sayAge()


card = Card('1233 3214 3215 8963', '11/28', 'Alex FF')


user_Alex.addCard(card)
user_Alex.getCard().pay (1000)