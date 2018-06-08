from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobb/stilling/(?P<posting_id>[\w-]+)', views.posting, name='posting'),
    url(r'^jobb/brukeropplevelse', views.team_design, name='team_design'),
    url(r'^jobb/teknologi', views.team_teknologi, name='team_teknologi'),
    url(r'^jobb/(?P<team>[\w]+)', views.team_postings, name='team_postings'),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow: /", content_type="text/plain"), name="robots_file"),
]
