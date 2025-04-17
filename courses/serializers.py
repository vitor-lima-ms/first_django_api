from rest_framework import serializers
from courses.models import Course, Rating

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}, # Email não será exibido. Será exigido apenas para se cadastrar
        }
        
        model = Rating
        
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    # ratings = RatingSerializer(many=True, read_only=True) # Nested relashionship --> Permite exibir as avaliações no request de exibe os cursos. Muito bom para relacionamentos One to One
    ratings = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rating-detail') # Hyperlinked relashionship --> Permite exibir as avaliações no request de exibe os cursos. Muito bom para relacionamentos One to Many. Modo mais recomendado para API's REST. O nome tem que ser exatamente o nome do modelo-detail
    # ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # PrimaryKey relashionship --> Apresente a PK das avaliações no request de exibe os cursos. Mais performática.

    class Meta:
        model = Course
        
        fields = '__all__' # Campos que serão exibidos