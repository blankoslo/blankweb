from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^jobb/(?P<posting_id>[\w-]+)', views.posting, name='posting'),
]
