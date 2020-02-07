from django.views.generic import TemplateView
from .models import News
import requests
from django.conf import settings

class HomeView(TemplateView):
    """ Home view
    """
    template_name = 'news/index.html'


class FetchNewsView(TemplateView):
    """ Fetch news from 'newsapi.org/v1/articles' api and save it db
    """
    template_name = 'news/fetch-news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = {
            'X-Api-Key': settings.API_KEY
        }
        url = 'https://newsapi.org/v1/articles?source=the-verge'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            context['isError'] = True
        else:
            response_data = response.json()
            news_objects = []
            for news in response_data['articles']:
                news_objects.append(
                    News(author=news['author'], title=news['title'], description=news['description'],
                         url=news['url'], urlToImage=news['urlToImage'], publishedAt=news['publishedAt'])
                )
            # Bulk create
            News.objects.bulk_create(news_objects)
            context['isError'] = False
        return context


class LatestNewsView(TemplateView):
    """ Show Latest 20 news View
    """
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newses'] = News.objects.filter().order_by('-publishedAt')[:20]
        return context
