class Author:

    all = []
    
    def __init__(self, name):
        if type(name) == str:
            self.name = name
            Author.all.append(self)

        else:
            raise TypeError("Name must be a string")
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total_royalties = sum(self._royalties.values())
        return total_royalties



class Book:
    
    all = []

    def __init__(self, title):
        if type(title) == str:
            self.title = title
            Book.all.append(self)
        
        else:
            raise TypeError("Title should be a string")
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, name):
        if  not isinstance(name, Author):
            raise TypeError("Author must be of type Author")
        self._author = name
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, name):
        if not isinstance(name, Book):
            raise TypeError("Book must be of type Book")
        self._book = name
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, day):
        if type(day) == str:
            self._date = day
        else:
            raise TypeError("Date must be a string")
    
    @property
    def royalties(self):
        return self._royalties 
    
    @royalties.setter
    def royalties(self, num):
        if type(num) == int:
            self._royalties = num
        else:
            raise TypeError("Royalties should be an integer")
        
    @classmethod
    def contracts_by_date(cls, date):
        contract_count = {}
        for contract in cls.all:
            # date = contract.date
            contract_count[date] = contract_count.get(date, 0) + 1
        return contract_count

        