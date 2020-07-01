import requests
import re
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import CNet

# Create your views here.


def news(request):
    # CNet Scrapper
    cnetUrl = requests.get('https://www.cnet.com/news/').text
    cnetSoup = BeautifulSoup(cnetUrl, 'lxml')

    cnetArticle1 = cnetSoup.findAll('div', section='topStories|item-1')
    for article in cnetArticle1:
        title = article.find('a', class_="mainStory").text
        img = article.find('figure', class_="img").img['src']
        href = article.find('a', class_="mainStory")['href']
        content = article.find('div', class_="content").p.text
        if CNet.objects.filter(title='title'):
            pass
        else:
            CNet.objects.all().delete()
            cnet = CNet(title=title,
                        img=img,
                        href=href,
                        content=content)
            cnet.save()

            cnetArticle2 = cnetSoup.findAll('div', section='topStories|item-2')
            for article in cnetArticle2:
                title = article.find('a', class_="mainStory").text
                img = article.find('figure', class_="img").img['src']
                href = article.find('a', class_="mainStory")['href']
                content = article.find('div', class_="content").p.text
                cnet = CNet(title=title,
                            img=img,
                            href=href,
                            content=content)
                cnet.save()

            cnetArticle3 = cnetSoup.findAll('div', section='topStories|item-3')
            for article in cnetArticle3:
                title = article.find('a', class_="mainStory").text
                img = article.find('figure', class_="img").img['src']
                href = article.find('a', class_="mainStory")['href']
                content = article.find('div', class_="content").p.text
                cnet = CNet(title=title,
                            img=img,
                            href=href,
                            content=content)
                cnet.save()

    context = {
        'cnets': CNet.objects.order_by('-id')[0:5],
    }

    return render(request, 'home/home.html', context)
