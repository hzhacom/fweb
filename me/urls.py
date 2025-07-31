"""me 的 URL 配置"""

from django.urls import path
from django.views.generic import TemplateView

from. import views

app_name = 'me'

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', views.error, name='error'),
    path("about/", TemplateView.as_view(template_name="me/404.html"),name='about'),
    path("mynote", views.NoteView.as_view(), name='mynote'),
    path("debug/", views.debug, name='debug'),
]