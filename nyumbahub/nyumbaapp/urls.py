
from django.contrib import admin
from django.urls import path
from nyumbaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agent'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('services/', views.services, name='services'),
    path('propertysingle/<int:id>', views.property_single, name='propertysingle'),
    path('servicedetails/', views.service_details, name='servicedetails'),
    path('starterpage/', views.starterpage, name='starterpage'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('addhouse/', views.addhouse, name='addhouse'),

]
