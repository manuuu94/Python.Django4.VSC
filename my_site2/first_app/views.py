from django.shortcuts import render
#import httpresponse
from django.http.response import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
#reverse function
from django.urls import reverse

# Create your views here.

#create dictionary to use as index or guide
articles = {
    'sports':'Sports page',
    'finance':'Finance page',
    'politics':'Politics page'
}


def simple_view(request):
#render returns httprequest,templatename & context (what is passed back to the template file)
   return render(request,'first_app/example.html')

def sports_view(request):
    return HttpResponse(articles['sports'])

def finance_view(request):
    return HttpResponse("Finance Page")

#dynamic solution. use the topic variable to use in the httpresponse and in the urls too. Searches the key to display its content.
def news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "no page found"
        #return HttpResponseNotFound(result)
        raise Http404(result)


#define integers as dynamic in the url
def add_view(request,num1,num2):
    result = num1 + num2
    return HttpResponse(str(result))

#to redirect from an int in the url instead of the key 
def num_page_view(request,num_page):
    topics_list = list(articles.keys()) #creates a list from the dictionary
    topic = topics_list[num_page]

    return HttpResponseRedirect(reverse('topic-page',args=[topic]))