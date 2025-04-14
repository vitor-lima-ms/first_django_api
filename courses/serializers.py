from rest_framework import serializers
from courses.models import Course, Rating

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        
        fields = '__all__' # Campos que serão exibidos

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}, # Email não será exibido. Será exigido apenas para se cadastrar
        }
        
        model = Rating
        
        fields = '__all__'