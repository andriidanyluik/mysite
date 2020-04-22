from django.shortcuts import render

# Create your views here.
from .models import Article, Kateg

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	return render(
		request,
        'index.html',
        context={'latest_articles_list': latest_articles_list}
    )

def detail(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404("Статтю не знайдено!")