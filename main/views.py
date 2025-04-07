from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'main/mainpage.html') 

def secondpage(request):
    return render(request, 'main/secondpage.html') 

# Django가 templates 폴더에서 mainpage.html을 찾도록 설정되어 있음.