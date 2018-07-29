from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from worldcup_standings import views


urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^matches/', views.matches),
                  url(r'^match/', views.match),
                  url(r'^teams/', views.teams),
                  url(r'^team/', views.team),
                  url(r'^players/', views.players),
                  url(r'^player/', views.player),
                  url(r'^standing/', views.groupStanding),
                  url(r'^upcoming_matches/', views.upcoming_match),
                  url(r'^todays_matches/', views.todays_match),
                  url(r'^recent_matches/', views.recent_match),
                  url(r'^$', views.matches),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
