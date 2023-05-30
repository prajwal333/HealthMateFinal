<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="healthapp"),
    path("about/", views.about, name="AboutUs"),
    path("ourdoctors/", views.ourdoctors, name="ourdoctors"),
    path("consultationform/", views.Consultationform, name="consultation"),
    path("blog/", views.blog, name="blog"),
    path("docview/<int:myid>",views.docview,name='ViewDoctorsProfile')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
from django.urls import path
from healthapp import views

urlpatterns = [
    path("",views.index,name="healthapp"),
    path("about/",views.about,name="AboutUs"),
    path("consultationform/",views.consultationform,name="consultationform"),
    path("blog/",views.blog,name="blog"),
    path("ourservices/",views.ourservices,name="ourservices"),
    path("ourdoctors/",views.ourdoctors,name="ourdoctors"),
    path("base/",views.base,name="base")
]
>>>>>>> 7b5d723d6a7abd818057f80f495b529a37c236e5
