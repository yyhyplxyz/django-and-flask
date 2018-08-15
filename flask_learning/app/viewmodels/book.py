

class Book_viewmodel:
    @classmethod
    def package_collection(cls,data, keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.cut_data(book) for book in data['books']]
        return returned

    @classmethod
    def package_single(cls,data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = cls.cut_data(data)
        return returned

    @classmethod
    def cut_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'author':'、 '.join(data['author']),
            'price':data['price'],
            'summary':data['summary'] or '',
            'image':data['image'],
            'pages':data['pages'] or '' #如果是空则返回空字符串
        }
        return book