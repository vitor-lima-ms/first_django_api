from rest_framework import generics
from courses.models import Course, Rating
from courses.serializers import CourseSerializer, RatingSerializer
from django.http import Http404

class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        if self.kwargs['course_pk']: # O nome aqui tem que ser o mesmo utilizado na URL
            # Se course_pk estiver presente, filtra os ratings pelo curso correspondente
            return Rating.objects.filter(course_id=self.kwargs['course_pk'])
        # Caso contrário, retorna todos os ratings
        return Rating.objects.all()

class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        self.lookup_url_kwarg = 'rating_pk' # Aqui estamos sobrescrevendo o lookup_url_kwarg para usar o rating_pk na URL
        try:
            if self.kwargs['course_pk'] and self.kwargs['rating_pk']:
                print('Entrei no if')
                # Se course_pk e rating_pk estiverem presentes, filtra os ratings pelo curso e pela avaliação correspondente
                return Rating.objects.get(course_id=self.kwargs['course_pk'], pk=self.kwargs['rating_pk'])
        except Rating.DoesNotExist:
            raise Http404("Rating not found")     