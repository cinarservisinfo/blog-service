from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogList,BlogListView,BlogDetailView,MiniBlogListView

urlpatterns = [
    path('blog/',BlogList,name='blog'),
    path('blog-list/',BlogListView.as_view()),
    path('mini-blog-list/',MiniBlogListView.as_view()),
    path('blog-detail/<slug>/',BlogDetailView.as_view(),name='blog-detail'),
    
]
