from user import User
from card import Card 

Aleksandr = User("Aleksandr")

Aleksandr.sayName()
Aleksandr.setAge(39)
Aleksandr.sayAge()

card = Card("4323 0003 3303 0003", "11/28", "Aleksandr B")

Aleksandr.addCard(card)
Aleksandr.getCard().pay(1000)


    