from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobb/stilling/(?P<posting_id>[\w-]+)', views.posting, name='posting'),
    url(r'^jobb/(?P<team>[\w]+)', views.team_postings, name='team_postings'),

]
