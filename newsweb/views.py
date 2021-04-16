from django.shortcuts import render

# Create your views here.
def home(request):
    import requests 
    import json
    news_api_request=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=2bb67e74320b4d48b82458fe61192a62cd ")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api}) 

# Create your views here.
def home(request):
    import requests 
    import json
    news_api_request=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=2bb67e74320b4d48b82458fe61192a62")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})

def business(request):
    import requests 
    import json
    news_api_request=requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=56d19e12cd3c4967bb5390ba0c47782b")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})

def tech(request):
    import requests 
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=56d19e12cd3c4967bb5390ba0c47782b")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})

def entertainment(request):
    import requests 
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=56d19e12cd3c4967bb5390ba0c47782b")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})

def health(request):
    import requests 
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=2bb67e74320b4d48b82458fe61192a62")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})

def sports(request):
    import requests 
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=2bb67e74320b4d48b82458fe61192a62")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})

def science(request):
    import requests 
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=2bb67e74320b4d48b82458fe61192a62")
    api=json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})
      
