
class Book_viewmodel:
    def __init__(self,book):
        self.title = book['title']
        self.author = book['author']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']
        self.publisher = book['publisher']


class Book_collection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushubook, keyword):
        self.total = yushubook.total
        self.keyword = keyword
        self.books = [Book_viewmodel(book) for book in yushubook.books]

# class Book_viewmodel:
#     @classmethod
#     def package_collection(cls,data, keyword):
#         returned = {
#             'books':[],
#             'total':0,
#             'keyword':keyword
#         }
#         if data:
#             returned['total'] = data['total']
#             returned['books'] = [cls.cut_data(book) for book in data['books']]
#         return returned
#
#     @classmethod
#     def package_single(cls,data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = 1
#             returned['books'] = cls.cut_data(data)
#         return returned
#
#     @classmethod
#     def cut_data(cls,data):
#         book = {
#             'title':data['title'],
#             'publisher':data['publisher'],
#             'author':'、 '.join(data['author']),
#             'price':data['price'],
#             'summary':data['summary'] or '',
#             'image':data['image'],
#             'pages':data['pages'] or '' #如果是空则返回空字符串
#         }
#         return book