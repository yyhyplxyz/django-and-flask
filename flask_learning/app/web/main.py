from flask import render_template

from app.models.gift import Gift
from app.viewmodels.book import Book_viewmodel
from . import web


__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [Book_viewmodel(gift.book) for gift in recent_gifts]
    return render_template('index.html',recent=books)


@web.route('/personal')
def personal_center():
    pass
