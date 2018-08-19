from collections import namedtuple

from app.viewmodels.book import Book_viewmodel

Mygift = namedtuple('MyGIFT', ['id','book','count'])


class Mywishes:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        #私有变量
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()
#尽量不在方法中去修改实例变量,
#nametuple和字典是类似的
    def __parse(self):
        tem_gifts = []
        for gift in self.__gifts_of_mine:
            tem_gifts.append(self.__matching(gift))
        return tem_gifts


    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        my_gift = Mygift(gift.id, Book_viewmodel(gift.book), count)
        return my_gift


