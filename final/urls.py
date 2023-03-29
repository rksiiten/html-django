from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('survey/', views.create_view, name = 'create'),
    path('list/', views.list_view, name = 'list'),
    path('list/update/<int:id>/', views.update_view, name = 'update'),
    path('list/delete/<int:id>/', views.delete_view, name = 'delete'),
    path('list/search/', views.search_view, name = 'search'),

    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('survey/', views.survey, name = 'survey'),
    path('us/', views.us, name = 'us'),

]
