# *Create a class for representing book with some attributes (author, owner, pages, price, current page)
# and behavior (change owner, increase price, change current page), create several books and perform operations on them

class Book:
    def __init__(self, author, owner, pages, price, currPage):
        self.author = author
        self.owner = owner
        self.pages = pages
        self.price = price
        self.currPage = currPage
    def change_owner(self, new_owner):
        self.owner = new_owner
        return self.owner
    def increase_price(self, pow):
        self.price = self.price * pow
        return self.price
    def change_curr_page(self, new_page):
        self.currPage = new_page
        return  self.currPage



the_shadow_of_the_wind = Book('Carlos Ruiz Zafon', 'Arina', 200, 80, 5)
the_lord_of_the_rings = Book('J.R.R. Tolkien', 'Hrayr', 360, 50, 150)
print('New price of the book the shadow of the wind is: ', the_shadow_of_the_wind.increase_price(2))
print('New Owner of the book the shadow of the wind is: ', the_shadow_of_the_wind.change_owner('Henrrik'))
print('New price of the book the lord of the rings is: ', the_lord_of_the_rings.increase_price(5))
print('Current page of the lord of the rings is: ', the_lord_of_the_rings.change_curr_page(66))