from django.contrib import admin
from django.urls import path
from .views import home, landing, about, contact  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),  # Landing page as default
    path('home/', home, name='home'),  # Main homepage
    path('about/', about, name='about'),  # About page (optional)
    path('contact/', contact, name='contact'),  # Contact page (optional)
]
from django.contrib import admin
from django.urls import path
from mysite.views import home, landing, about, contact  # Use "mysite.views" if in the same directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
