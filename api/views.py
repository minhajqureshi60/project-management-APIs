from django.shortcuts import render
from rest_framework import viewsets
from api.models import Project,Employee
from api.serializers import ProjectSerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class=ProjectSerializer
    
    #companies/{projectId}/emplyees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            project=Project.objects.get(pk=pk)
            emps=Employee.objects.filter(project=project)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Project might not exists !! Error'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer