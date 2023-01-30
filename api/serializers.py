from rest_framework import serializers
from api.models import Project,Employee


#create serializers here
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Project
        fields="__all__"
        
        
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=Employee
        fields="__all__"