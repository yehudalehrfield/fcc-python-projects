from budget import Category, create_spend_chart

food = Category('food')
food.deposit(400, 'initial deposit')
food.withdraw(12.50, 'snacks')
food.withdraw(70, 'groceries')
food.deposit(5, 'a really long deposit message for a relatively small deposit')
food.withdraw(220.83, 'A hefty shopping')

toys = Category('toys')
food.transfer(50,toys)
toys.deposit(225, 'pump more money into toys')
toys.withdraw(5.509, 'PEZ dispensers')
toys.withdraw(100, 'Lego')

books = Category('books')
books.deposit(200.50, 'initial deposit')
books.withdraw(80,'a bunch of books')

clothes = Category('clothes')
clothes.deposit(300, 'initial deposit')
clothes.transfer(75, books)
clothes.withdraw(30, 'A new sweater')

print(food)
print(toys)
print(books)
print(clothes)

create_spend_chart([food, toys, books, clothes])