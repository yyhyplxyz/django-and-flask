from django.shortcuts import render, redirect

from firstapp.models import Article, Comment, Ticket, Document
from firstapp.forms import CommentForm, DocumentForm, FileDb

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import json
from django.core.management import call_command
from django.template.loader import get_template

# Create your views here.

def familytree(request):
    # Handle file upload
    output = open('233.json', 'w')  # Point stdout at a file for dumping data to.
    call_command('dumpdata', 'familymember', format='json', indent=3, stdout=output)
    output.close()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('tree')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'pro3.html',
        {'documents': documents, 'form': form}
    )
    # members = familymember.objects.all()
    return render(
        request,
        'pro3.html',
        {}
    )


def single_file(request, id):
    file = FileDb.objects.get(id=id)
    filename = file.source.read()
    # save edited file:
    if request.method == "POST":
        from django.core.files import File
        f = open(file.source.path, 'w')
        content = request.POST['content']
        f.write(content)
        f = File(f)
        file.source = f
        file.save()
    return render(
        request,
        'pro3.html',
        {'file': file, 'filename': filename}
    )
    return HttpResponse


def index(request):
    article_list = Article.objects.all()

    page_robot = Paginator(article_list, 5)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)

    context = {}
    context["article_list"] = article_list

    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)

    if request.method == "GET":
        form = CommentForm

    context = {}
    context["article"] = article
    context['form'] = form

    return render(request, 'detail.html', context)


def comment(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            comment = form.cleaned_data["comment"]
            article = Article.objects.get(id=id)
            c = Comment(name=name, comment=comment, belong_to=article)
            c.save()
            return redirect(to="detail", id=id)
    return redirect(to="detail", id=id)


def index_login(request):
    if request.method == "GET":
        form = AuthenticationForm

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="index")

    context = {}
    context['form'] = form

    return render(request, 'login.html', context)


def index_register(request):
    if request.method == "GET":
        form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')

    context = {}
    context['form'] = form

    return render(request, 'register.html', context)


def vote(request, id):
    # 未登录用户不允许投票，自动跳回详情页
    if not isinstance(request.user, User):
        return redirect(to="detail", id=id)

    voter_id = request.user.id

    try:
        # 如果找不到登陆用户对此篇文章的操作，就报错
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_this_article.choice = request.POST["vote"]
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, article_id=id, choice=request.POST["vote"])
        new_ticket.save()

    # 如果是点赞，更新点赞总数
    if request.POST["vote"] == "like":
        article = Article.objects.get(id=id)
        article.likes += 1
        article.save()

    return redirect(to="detail", id=id)
