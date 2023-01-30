from django.contrib import admin
from django.urls import path,include
from api.views import ProjectViewSet,EmployeeViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [    
    path('',include(router.urls))
      
]
