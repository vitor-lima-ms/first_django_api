from django.urls import path
from courses.views import CourseAPIView, RatingAPIView, CoursesAPIView, RatingsAPIView

urlpatterns = [ # Endpoints
    path('courses/', CoursesAPIView.as_view(), name='courses'),

    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'), # Não precisamos sobrescrever nenhum método dessa view, logo podemos usar apenas pk na URL

    path('courses/<int:course_pk>/ratings/', RatingsAPIView.as_view(), name='course_ratings'),

    path('courses/<int:course_pk>/ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='course_rating'), # Aqui temos que diferenciar entre as pks do curso e da avaliação, então usamos course_pk e rating_pk na URL

    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    
    path('ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='rating'), # Como já vamos sobrescrever a view, também podemos mudar de pk para rating_pk, assim como fizemos na URL acima
]