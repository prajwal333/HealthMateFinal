from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contactus(request):
    return HttpResponse("This is contact us")
def consultationform(request):
    return render(request, 'consultationform.html')
def blog(request):
    return render(request, 'blog.html')
def ourservices(request):
    return render(request, 'ourservices.html')
def ourdoctors(request):
    return render(request, 'ourdoctors.html')
def base(request):
    return render(request, 'base.html')

