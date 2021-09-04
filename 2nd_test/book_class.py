class Book:
    def set(self,Library_name,book_name,author,pages):
        self.Lib_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
        print(self.Lib_name,self.book_name,self.author,self.pages)
bk=Book()
bk.set('library','abc','name',120)