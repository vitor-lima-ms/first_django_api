from rest_framework import generics
from courses.models import Course, Rating
from courses.serializers import CourseSerializer, RatingSerializer

class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RatingAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer