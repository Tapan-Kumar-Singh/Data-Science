from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import *


def AllPosts(request):
    PostsList = Article.objects.all()
    context = {
        'all_posts': PostsList
    }
    return render(request, "dashboard/posts/all-posts.html", context)


def AddArticle(request):
    if request.method == 'POST':
        Lang = request.POST.get('language')
        ImageFb = request.FILES['fb-image']
        ImageWeb = request.FILES['story-img']
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
        # if request.FILES['fb-image'] == '':
        #     ArticleList.image_one = request.POST.get('facebook_image')
        # else:
        #     ArticleList.image_one = request.FILES['fb-image']
        # if request.FILES['story-img'] == '':
        #     ArticleList.image_two = 'BLANK IMAGE'
        # else:
        #     ArticleList.image_two = request.FILES['story-img']
        ArticleList.topic = request.POST.get('topic')
        ArticleList.title = request.POST.get('title')
        ArticleList.short_description = request.POST.get('short_des')
        ArticleList.highlight = request.POST.get('highlight')
        ArticleList.body = request.POST.get('body')
        ArticleList.category = request.POST.get('category')
        ArticleList.link = request.POST.get('urls_slog')
        ArticleList.authors = request.POST.get('author')
        ArticleList.article_source = request.POST.get('location')
        ArticleList.add_to = request.POST.get('add_to')
        ArticleList.published = request.POST.get('publish')
        ArticleList.meta_title = request.POST.get('meta_title')
        ArticleList.meta_description = request.POST.get('meta_description')
        ArticleList.article_source = request.POST.get('source')
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
