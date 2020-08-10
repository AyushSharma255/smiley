from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("browse/", views.browse, name="browse"),
    path("browse/hot/<int:page>", views.browseHot, name="browseHot"),
    path("browse/top/<int:page>", views.browseTop, name="browseTop"),
    path("browse/recent/<int:page>", views.browseRecent, name="browseRecent"),
    path("detail/<pk>/", views.detail, name="detail")
]
