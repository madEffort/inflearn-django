from django.urls import path

from shortener import views, apis

urlpatterns = [
    # django
    path("", views.HomeView.as_view(), name="home"),
    path("short-urls/", views.ShortURLCreateView.as_view(), name="shorten_url"),
    path("<str:code>/", views.ShortURLDetailView.as_view(), name="short_url_detail"),

    # drf
    path("api/short-urls/", apis.ShortURLsAPIView.as_view(), name="short_urls_api"),
    path("api/short-urls/<str:code>/", apis.ShortURLAPIView.as_view(), name="short_url_api"),
]
