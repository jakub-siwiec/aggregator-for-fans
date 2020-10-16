from django.urls import path

from . import views

app_name = "persons"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('persons/<slug:slug>/', views.DetailView.as_view(), name='detail'),
]
