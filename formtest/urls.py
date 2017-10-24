from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'thanks/$', views.thanks, name='thanks'),
        url(r'contact_us/$', views.contact_us, name='contact_us'),
        ]
