import pandas as pd

class Library:
    data=pd.DataFrame()
    
    def add_book(self, name:str, author: str, year: int, genre: str):
        data_dictionary={"Назва":name, "Автор": author, "Рік": year, "Жанр": genre}
        self.data=self.data.append(data_dictionary, ignore_index=True)
        print(self.data)
    def delete_book(self, book_id: int):
        if len(self.data) == 0:
            print("Книг в библиотеке нет")
        else:
            self.data=self.data.drop(book_id)
            print(self.data)

    def find_book(self, book_id: int):
        all_indexes = self.data.head()
        for i in all_indexes.index:
            if all_indexes.index[i] == book_id:
                print(pd.DataFrame(self.data.iloc[book_id]))     
l=Library()
l.add_book("Мастер и Маргарита","Михаил Булгаков",1929,"Роман")
l.add_book("Мёртвые души","Николай Гоголь",1842,"Проза")

or1 = int(input("Ви хочете додати книгу до бібліотеки? (1 - Так, 2 - Ні) :"))
if or1 == 1:
    rang1 = int(input("Введіть кількість кних, яких ви хочете додати :"))
    for i in range(rang1):
        name = input("Назва:")
        author = input("Автор:")   
        year = input("Рік:")
        genre = input("Жанр:")
        l.add_book(name, author, year, genre)
else:
    exit
    
del1 = int(input("Чи бажаєте видалити книгу з бібліотеки? (1 - Так, 2 - Ні):"))
if del1 == 1:
    ch = int(input("Який номер книги ви хочете видалити? :"))
    l.delete_book(ch)
else:
    exit

find = int(input("Чи бажаєте знайти книгу за номером?(1 - Так, 2 - Ні) :"))
if find == 1:
    ch2 = int(input("Введіть номер книги :"))
    l.find_book(ch2)
else: 
    exit
