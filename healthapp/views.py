from django.shortcuts import render
from django.http import HttpResponse
from .models import doctor
from .models import consultationform
from math import ceil

# Create your views here.


def index(request):
<<<<<<< HEAD
    return render(request, 'healthapp/index.html')


def about(request):
    return render(request, 'healthapp/about.html')


def ourdoctors(request):
    allDocs = []
    departdocs = doctor.objects.values('department', 'id')
    cats = {item['department'] for item in departdocs}
    for cat in cats:
        doc = doctor.objects.filter(department=cat)
        n = len(doc)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allDocs.append([doc, range(1, nSlides), nSlides])
    params = {'allDocs': allDocs}
    return render(request, 'healthapp/ourdoctors.html', params)
    # doctors = doctor.objects.all()
    # n = len(doctors)
    # nSlides = n//4 + ceil((n/4) + (n//4))
    # #   params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'doctor': doctors}
    # allDocs = [[doctors, range(1, nSlides), nSlides], [
    #     doctors, range(1, nSlides), nSlides]]
    # params = {'allDocs': allDocs}


def Consultationform(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        department = request.POST.get('department','')
        date = request.POST.get('date','')
        time = request.POST.get('time','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        # print(name,email,phone,department,date,time,city,state)
        Consultationform=consultationform(name=name,email=email,phone=phone,department=department,date=date,time=time,city=city,state=state)
        Consultationform.save()
        return HttpResponse('Thank you for filling appointment.We will reach you ASAP')

    return render(request, 'healthapp/consultationform.html')


def blog(request):
    return render(request, 'healthapp/blog.html')
=======
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
>>>>>>> 7b5d723d6a7abd818057f80f495b529a37c236e5

def docview(request,myid):
    # Fetching using id
    doc= doctor.objects.filter(id=myid)

    return render(request, 'healthapp/docview.html',{'doctors':doc[0]})
