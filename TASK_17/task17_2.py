class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.author = []

    counter = 0
    def new_book(self, name, year, author):
        inst_book = Book(name, year, author)
        self.books.append({'Book': name, 'Year': year, 'Author': author})
        Library.counter += 1


    def group_author(self, author):
        group_author_list = []
        for i in self.books:
            if i == author:
                group_author_list.append(i)
        return f'{sorted(group_author_list, key=lambda j: j['Author'])}'


    def group_year(self, year):
        group_year_list = []
        for i in self.books:
            if i == year:
                group_year_list.append(i)
        return f'{sorted(group_year_list, key=lambda j: j['Year'])}'



    def __str__(self):
        return f'Now works {self.name}'

    def __repr__(self):
        return self.__str__()


class Author:
    def __init__(self, name, country, birthday, books):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f'Now works {self.name}'

    def __repr__(self):
        return self.__str__()


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'Now works {self.name}'

    def __repr__(self):
        return self.__str__()

