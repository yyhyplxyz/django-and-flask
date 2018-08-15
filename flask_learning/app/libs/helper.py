def is_isbn_or_key(word):
    """
           q 普通关键字 isbn
           page
       :return:
       """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit():  # 耗资源的条件放在后面
        isbn_or_key = 'isbn'
    return isbn_or_key