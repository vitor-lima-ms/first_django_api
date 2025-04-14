from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)
    active = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        abstract = True

class Course(Base):
    title = models.CharField(verbose_name='Título', max_length=200)
    url = models.URLField(verbose_name='URL', unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.title

class Rating(Base):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    name = models.CharField(verbose_name='Nome', max_length=200)
    email = models.EmailField(verbose_name='Email')
    rating = models.DecimalField(verbose_name='Avaliação', max_digits=3, decimal_places=2)
    comment = models.TextField(verbose_name='Comentário', blank=True, null=True, default='')

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ('course', 'email') # Não permite que o mesmo email possa avaliar o mesmo curso mais de uma vez

    def __str__(self):
        return f'{self.name} - {self.course} - {self.rating}'
    
    
    
