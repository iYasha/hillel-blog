from django.shortcuts import render, redirect

from article.forms import MemberForm
from article.models import Article


def get_home(request):
	context = {
		'main_article': Article.objects.order_by('created_at').first(),
		'articles': Article.objects.order_by('created_at').all()[1:],
		'most_popular_articles': Article.objects.order_by('-view_count')[:4]
	}
	return render(request, 'home.html', context)


def get_article(request, article_id):
	article = Article.objects.get(id=article_id)
	article.view_count += 1
	article.save()

	content = ''.join([f'<p>{x.strip()}</p>' for x in article.description.split('\n') if x.strip()])

	context = {
		'article': article,
		'text': content,
		'member_form': MemberForm(),
	}

	return render(request, 'article.html', context)


def add_member(request):
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(request.headers.get('Referer'))
