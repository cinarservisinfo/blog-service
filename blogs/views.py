from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
# Create your views here.


def BlogList(request):
    items = Blog.objects.filter(is_active=True)
    context = {'items': items}
    return render(request, 'blog.html', context)


class BlogDetailView(APIView):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        seo_data = {
            'title': blog.caption,
            'description': blog.content[:150],  # İlk 150 karakter
            'image': blog.image.url if blog.image else None,
            'url': request.build_absolute_uri(),
        }
        serializer = BlogSerializer(blog,many=False,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

class MiniBlogListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        items= Blog.objects.filter(is_active=True)[:3]
        serializer = BlogSerializer(items,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
        
class BlogListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        items= Blog.objects.filter(is_active=True)
        serializer = BlogSerializer(items,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Blog.objects.filter(is_active=True)
        return queryset

class BlogSitemap(Sitemap):
    changefreq = "weekly"  # Bloglar haftalık olarak güncelleniyor
    priority = 0.6

    def items(self):
        return Blog.objects.filter(is_active=True)  # Aktif blogları döndür

    def lastmod(self, obj):
        return obj.updated  # Blog güncellenme tarihini döndür
# my_project/sitemaps.py



