from django.urls import path
from courses.views import CourseAPIView, RatingAPIView, CoursesAPIView, RatingsAPIView

urlpatterns = [ # Endpoints
    path('courses/', CoursesAPIView.as_view(), name='courses'),

    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),

    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    
    path('ratings/<int:pk>/', RatingAPIView.as_view(), name='rating'),
]