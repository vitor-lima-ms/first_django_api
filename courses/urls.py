from django.urls import path
from courses.views import CourseAPIView, RatingAPIView

urlpatterns = [ # Endpoints
    path('courses/', CourseAPIView.as_view(), name='courses'),

    path('ratings/', RatingAPIView.as_view(), name='ratings'),
]