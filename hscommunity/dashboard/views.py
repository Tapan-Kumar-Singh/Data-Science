from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, "dashboard/welcome/index.html")


def user(request):
    UserList = AllUser.objects.all()
    context = {
        'user_list': UserList
    }
    return render(request, "dashboard/user/user.html", context)


def AddUser(request):
    if request.method == 'POST':
        FirstName = request.POST.get('first_name')
        LastName = request.POST.get('last_name')
        EmailId = request.POST.get('email_id')
        ContactNo = request.POST.get('contact_no')
        UserRole = request.POST.get('user_role')
        InsertUser = AllUser(first_name=FirstName, last_name=LastName, email_id=EmailId, contact_number=ContactNo,
                             roll=UserRole)
        InsertUser.save()
        return redirect('/dashboard/user')
    UserRoles = UserRoll.objects.all()
    context = {
        'UserRole': UserRoles,
    }
    return render(request, "dashboard/user/create-user.html", context)


def UpdateUser(request, id):
    UserList = AllUser.objects.get(id=id)
    if request.method == 'POST':
        UserList.first_name = request.POST.get('first_name')
        UserList.last_name = request.POST.get('last_name')
        UserList.email_id = request.POST.get('email_id')
        UserList.contact_number = request.POST.get('contact_no')
        UserList.roll = request.POST.get('user_role')
        UserList.save()
        return redirect('/dashboard/user')
    UserRoles = UserRoll.objects.all()
    context = {
        'UserRole': UserRoles,
        'user_list': UserList,
    }
    return render(request, "dashboard/user/update-user.html", context)


def DeleteUser(request, id):
    UserList = AllUser.objects.get(id=id)
    if request.method == 'POST':
        UserList.delete()
        return redirect('/dashboard/user')
    UserRoles = UserRoll.objects.all()
    context = {
        'UserRole': UserRoles,
        'user_list': UserList,
    }
    return render(request, "dashboard/user/user-delete.html", context)


def AllPosts(request):
    PostsList = Article.objects.all()
    context = {
        'all_posts': PostsList
    }
    return render(request, "dashboard/posts/all-posts.html", context)


def AddArticle(request):
    if request.method == 'POST':
        Lang = request.POST.get('language')
        ImageFb = request.POST.get('fb-image')
        ImageWeb = request.POST.get('story-img')
        Topic = request.POST.get('topic')
        Title = request.POST.get('title')
        ShortDescription = request.POST.get('short_des')
        HighLights = request.POST.get('highlight')
        Body = request.POST.get('body')
        Catg = request.POST.get('category')
        Slug = request.POST.get('urls_slog')
        Authors = request.POST.get('author')
        Locations = request.POST.get('location')
        AddTo = request.POST.get('add_to')
        Publish = request.POST.get('publish')
        MetaTitle = request.POST.get('meta_title')
        MetaDescription = request.POST.get('meta_description')
        Source = request.POST.get('source')
        InsertArticle = Article(language=Lang, image_one=ImageFb, image_two=ImageWeb, topic=Topic, title=Title,
                                short_description=ShortDescription, highlight=HighLights, body=Body, category=Catg,
                                link=Slug, authors=Authors, location=Locations, add_to=AddTo, published=Publish,
                                meta_title=MetaTitle, meta_description=MetaDescription, article_source=Source)
        InsertArticle.save()
        return redirect('/dashboard/posts/')
    LanguageList = Language.objects.all()
    CategoryList = Category.objects.all()
    SourceList = ArticleSource.objects.all()
    AuthorList = AllUser.objects.filter(roll='Author').values()
    context = {
        'Languages': LanguageList,
        'Authors': AuthorList,
        'categories': CategoryList,
        'sources': SourceList,
    }
    return render(request, "dashboard/posts/add-article.html", context)


def EditArticle(request, id):
    ArticleList = Article.objects.get(id=id)
    if request.method == 'POST':
        ArticleList.language = request.POST.get('language')
        ArticleList.image_one = request.POST.get('fb-image')
        # Article.image_two = request.POST.get('story-img')
        # Article.topic = request.POST.get('topic')
        # Article.title = request.POST.get('title')
        # Article.short_description = request.POST.get('short_des')
        # Article.highlight = request.POST.get('highlight')
        # Article.body = request.POST.get('body')
        # Article.category = request.POST.get('category')
        # Article.link = request.POST.get('urls_slog')
        # Article.authors = request.POST.get('author')
        # Article.article_source = request.POST.get('location')
        # Article.add_to = request.POST.get('add_to')
        # Article.published = request.POST.get('publish')
        # Article.meta_title = request.POST.get('meta_title')
        # Article.meta_description = request.POST.get('meta_description')
        # Article.article_source = request.POST.get('source')
        ArticleList.save()
        return redirect('/dashboard/posts')
    LanguageList = Language.objects.all()
    CategoryList = Category.objects.all()
    SourceList = ArticleSource.objects.all()
    AuthorList = AllUser.objects.filter(roll='Author').values()
    context = {
        'articles': ArticleList,
        'Languages': LanguageList,
        'Authors': AuthorList,
        'categories': CategoryList,
        'sources': SourceList,
    }
    return render(request, "dashboard/posts/edit-article.html", context)
