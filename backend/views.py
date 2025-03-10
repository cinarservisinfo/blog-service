from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.sitemaps import Sitemap  # new


@api_view(['GET'])
def Home(request):
    return render(request, 'index.html',)

@api_view(['GET'])
def About(request):
    return render(request, 'hakkimizda.html')


# backend/views.py
from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /users/",
        "Allow: /",        
        "Allow: /bolgeler/",
        "Allow: /markalar/",
        "Allow: /servisler/",
        "Sitemap: https://cinarservis.com/sitemap.xml",

        # Diğer disallow kuralları ekleyin
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

class AboutSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['hakkimizda']  # Hakkımızda sayfasının adı

    def location(self, item):
        return '/hakkimizda/'  # Hakkımızda sayfasının URL'si

class HomeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return ['index']  # Anasayfa sayfasının adı

    def location(self, item):
        return ''  # Anasayfa sayfasının URL'si

