class Book:
    def __init__(self,id,name,description,page_count,issued,author,year):
        self.id=id
        self.name=name
        self.description=description
        self.page_count=page_count
        self.issued=issued
        self.author=author
        self.year=year
    def to_dict(self):
        dictionary={"id":self.id,"name":self.name,"description":self.description,
            "page_count":self.page_count,"issued":self.issued,"author":self.author,"year":self.year}
        return dictionary
        
book=Book(121,"Rich dad Poor dad","Business",300,"yes","Robert Kiyosaki and Sharon Lechter",2021)
print(book.to_dict())
