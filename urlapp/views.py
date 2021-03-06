from django.shortcuts import render
from django.http import HttpResponse
from .models import Urls
from urllib.parse import urlparse
from django.views.decorators.http import require_http_methods
from bs4 import BeautifulSoup
import requests
import time

def getSeo ():
    data = Urls.objects.all()
    for i, url in enumerate(data):
        if url.url_thumb == 'default.jpg':
            try :
                r = requests.get(url.url)
                soup = BeautifulSoup(r.content, "html.parser")
                links = soup.select("link[rel*='icon']")
                data[i].title = soup.title.string
                links = links[:1][0]['href']

                if not links.startswith("http", 0):
                    parsed = urlparse(url.url)
                    port = ''
                    if parsed.port: port = ':' + parsed.port
                    data[i].links = parsed.scheme + "://" + parsed.netloc + port + "/" + links
                else :
                    data[i].links = links
            except :
                
                data[i].title = "None"
                data[i].links = "https://placehold.it/150x80?text=IMAGE"
                
            url.url_thumb = data[i].links
            url.url_title = data[i].title
            url.save()
        else :
            data[i].links = url.url_thumb
            data[i].title = url.url_title
            
    return data

def Index (request):
    data = getSeo()
    return render(request, 'urlapp/index.html', {'data': data})
# Create your views here.

@require_http_methods(["POST"])
def geturl(request):
    data = request.POST.copy();
    del data['csrfmiddlewaretoken']
    data = { x: y for x, y in data.items() }
    Urls(**data).save()
    return render(request, 'urlapp/get.html', {'r': request.POST})


@require_http_methods(["GET"])
def deleteUrl(request, tid):
    tid = Urls.objects.get(id = tid)
    info = tid.url
    tid.delete()
    return HttpResponse("URL '{}' has been DELETED SUCCESSFULLY....<script> setTimeout(()=>window.location.href='http://localhost:8000/urlsaver/', 5000) </script>".format(info))