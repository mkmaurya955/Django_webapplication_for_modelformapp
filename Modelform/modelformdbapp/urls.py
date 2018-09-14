from django.conf.urls import url
from . import views
app_name='modelformdbapp'
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^reg$',views.reg,name='reg'),
    url(r'^Login$',views.Login,name='login'),
]
