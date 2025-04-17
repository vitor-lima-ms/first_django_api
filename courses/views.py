"""Packages for the Courses API V1"""
from rest_framework import generics
from django.http import Http404

"""Packages for both V1 and V2"""
from courses.models import Course, Rating
from courses.serializers import CourseSerializer, RatingSerializer

"""Packages for the Courses API V2"""
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

"""API V1"""
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
        if self.kwargs.get('course_pk'): # O nome aqui tem que ser o mesmo utilizado na URL
            # Se course_pk estiver presente, filtra os ratings pelo curso correspondente
            return Rating.objects.filter(course_id=self.kwargs.get('course_pk'))
        # Caso contrário, retorna todos os ratings
        return Rating.objects.all()

class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_object(self):
        self.lookup_url_kwarg = 'rating_pk' # Aqui estamos sobrescrevendo o lookup_url_kwarg para usar o rating_pk na URL
        try:
            if self.kwargs.get('course_pk') and self.kwargs.get('rating_pk'):
                print('Entrei no if')
                # Se course_pk e rating_pk estiverem presentes, filtra os ratings pelo curso e pela avaliação correspondente
                return Rating.objects.get(course_id=self.kwargs.get('course_pk'), pk=self.kwargs.get('rating_pk'))
        except Rating.DoesNotExist:
            raise Http404("Rating not found")


"""API V2"""
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get']) # A URL para acessar essa ação será /api/v2/courses/{id}/ratings/
    def ratings(self, request, pk=None):
        self.pagination_class.page_size = 1 # Define o número de avaliações por página
        ratings = Rating.objects.filter(course_id=pk) # Filtra as avaliações pelo curso correspondente
        page = self.paginate_queryset(ratings) # Pagina as avaliações
        
        if page is not None:
            serializer = RatingSerializer(page, many=True) # Serializa as avaliações paginadas
            return self.get_paginated_response(serializer.data) # Retorna a resposta paginada

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer

# Podemos remover os mixins referentes às operações que não queremos permitir
class RatingViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer