from django.conf.urls import url
from home import views
urlpatterns = [
    url(r'^$',views.userLogin,name='userLogin'),
    url(r'^login/$',views.userLogin,name='userLogin'),
    url(r'^logout/$',views.userLogout,name='userLogout'),
]