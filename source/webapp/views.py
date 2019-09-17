from django.shortcuts import render, get_object_or_404, redirect
from django.utils.safestring import mark_safe

from webapp.models import Article


def todo_view(request, *args, **kwargs):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_add.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')
        article = Article.objects.create(title=title, description=description, status=status, date=date)
        return redirect('article_view', pk=article.pk)


def article_delete_view(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'article_update.html', context={'article': article})
    elif request.method == 'POST':
        article.title = request.POST.get('title')
        article.description = request.POST.get('description')
        article.status = request.POST.get('status')
        article.date = request.POST.get('date')
        article.save()
        return redirect('article_view', pk=article.pk)


def article_delete_checked_view(request):
    if request.method == 'POST':
        delete = request.POST.getlist('delete')
        for i in delete:
            article = get_object_or_404(Article, pk=i)
            article.delete()
        return redirect('index')
