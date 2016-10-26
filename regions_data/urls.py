from django.conf.urls import url
from regions_data import views


urlpatterns = [
    url(r'^parse/$', views.parse, name='parse'),
    url(r'^success/$', views.success, name='success'),
    url(r'^select_region/$', views.select_region, name='select_region'),
    url(r'^$', views.show, name='show'),
]
