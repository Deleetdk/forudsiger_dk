from django.conf.urls import url

from . import views

urlpatterns = [

    #danish
    url(r'^$', views.index, name='index'),
    url(r'^forudsig$', views.make_prediction, name='make_prediction'),
    url(r'^forudsigelser$', views.predictions, name='predictions'),
    url(r'^begivenheder$', views.events, name='events'),
    url(r'^begivenhed-(?P<begivenhed_id>\d+)$', views.event, name='event'),
    url(r'^toplisten$', views.leaderboard, name='leaderboard'),
    url(r'^log_ind', views.login_page, name='login_page'),
    url(r'^fejl$', views.error_page, name='error_page'),
    #url(r'^ny_bruger$', views.new_user, name='ny_bruger'),
]
