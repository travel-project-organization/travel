from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^map$', views.map),
    url(r'^regist$', views.regist),
    url(r'^login$', views.Login),
url(r'^arrange$', views.arrange)
    #url(r'^(\d+)/(\d+)$',views.detail),
    #url(r'^grades/$',views.grades),
    #url(r'^students/$',views.students),
    #url(r'^grades/(\d+)$',views.gradesStudents)
    #url(r'^regist/$',views.regist),
    #url(r'^login/$',views.login),
    #url(r'^logout/$',views.logout)
]